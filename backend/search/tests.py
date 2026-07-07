from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import ContactLead, SearchDocument


class SearchDocumentModelTests(TestCase):
    def test_string_representation_uses_title(self):
        document = SearchDocument.objects.create(
            title="脑电大模型智能体建设",
            summary="摘要",
            body="正文",
            category=SearchDocument.Category.AGENT,
            tags=["脑电大模型"],
            url="/#agent",
        )

        self.assertEqual(str(document), "脑电大模型智能体建设")


class ContactLeadModelTests(TestCase):
    def test_string_representation_uses_name_and_interest(self):
        lead = ContactLead.objects.create(
            name="张三",
            organization="测试机构",
            contact="zhangsan@example.com",
            interest=ContactLead.Interest.TRAINING,
            message="希望了解机器人训练动态标签合作。",
        )

        self.assertEqual(str(lead), "张三 - 机器人训练")


class HealthApiTests(TestCase):
    def test_health_api_returns_ok(self):
        response = self.client.get(reverse("health"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")
        self.assertEqual(response.json()["service"], "hudongzhiti-api")


class AdminLoginCaptchaTests(TestCase):
    def test_admin_login_page_includes_captcha(self):
        response = self.client.get(reverse("admin:login"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="id_captcha"')
        self.assertIn("admin_login_captcha", self.client.session)

    def test_admin_login_accepts_matching_captcha(self):
        User = get_user_model()
        User.objects.create_superuser(username="admin", password="admin", email="")
        self.client.get(reverse("admin:login"))
        captcha = self.client.session["admin_login_captcha"]

        response = self.client.post(
            reverse("admin:login"),
            {
                "username": "admin",
                "password": "admin",
                "captcha": captcha,
                "next": reverse("admin:index"),
            },
        )

        self.assertEqual(response.status_code, 302)


class SearchApiTests(TestCase):
    def setUp(self):
        SearchDocument.objects.create(
            title="脑电大模型智能体建设",
            summary="面向机器人训练与陪伴交互的脑电大模型智能体能力。",
            body="脑电信号理解、多模态任务编排、智能体工作流。",
            category=SearchDocument.Category.AGENT,
            tags=["脑电大模型", "智能体", "机器人"],
            url="/#agent",
            weight=30,
        )
        SearchDocument.objects.create(
            title="机器人训练动态标签",
            summary="用脑电大模型为语音视频训练数据生成动态标签。",
            body="机器人训练、语音视频、动态标签、训练反馈。",
            category=SearchDocument.Category.TRAINING,
            tags=["机器人训练", "动态标签"],
            url="/#training",
            weight=20,
        )
        SearchDocument.objects.create(
            title="未发布内部材料",
            summary="不应出现在搜索结果中。",
            body="脑电",
            category=SearchDocument.Category.COMPANY,
            tags=[],
            url="/internal",
            is_published=False,
            weight=100,
        )

    def test_search_returns_published_chinese_keyword_matches(self):
        response = self.client.get(reverse("search"), {"q": "脑电"})

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["query"], "脑电")
        self.assertEqual(payload["count"], 2)
        self.assertNotIn("未发布内部材料", [item["title"] for item in payload["results"]])

    def test_search_filters_by_category(self):
        response = self.client.get(reverse("search"), {"category": "training"})

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["count"], 1)
        self.assertEqual(payload["results"][0]["title"], "机器人训练动态标签")

    def test_empty_query_returns_recommended_content(self):
        response = self.client.get(reverse("search"))

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["count"], 2)
        self.assertEqual(payload["results"][0]["title"], "脑电大模型智能体建设")

    def test_no_results_returns_empty_list(self):
        response = self.client.get(reverse("search"), {"q": "不存在的关键词"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["results"], [])


class ContactLeadApiTests(TestCase):
    def test_contact_api_creates_lead(self):
        response = self.client.post(
            reverse("contact"),
            data={
                "name": "李四",
                "organization": "机器人实验室",
                "contact": "lisi@example.com",
                "interest": "companion",
                "message": "希望了解陪伴机器人内容能力合作方案。",
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(ContactLead.objects.count(), 1)
        self.assertEqual(ContactLead.objects.get().interest, ContactLead.Interest.COMPANION)
        self.assertEqual(response.json()["message"], "咨询已提交，我们会尽快联系您。")

    def test_contact_api_validates_required_message_length(self):
        response = self.client.post(
            reverse("contact"),
            data={
                "name": "李四",
                "contact": "12345",
                "interest": "agent",
                "message": "太短",
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(ContactLead.objects.count(), 0)
        self.assertIn("message", response.json())
