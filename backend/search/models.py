from django.db import models


class SearchDocument(models.Model):
    class Category(models.TextChoices):
        AGENT = "agent", "脑电大模型智能体"
        TRAINING = "training", "机器人训练"
        COMPANION = "companion", "机器人陪伴"
        COMPANY = "company", "公司信息"
        FAQ = "faq", "FAQ"

    title = models.CharField("标题", max_length=120)
    summary = models.TextField("摘要")
    body = models.TextField("正文")
    category = models.CharField("分类", max_length=32, choices=Category.choices)
    tags = models.JSONField("标签", default=list, blank=True)
    url = models.CharField("链接", max_length=200)
    weight = models.PositiveIntegerField("排序权重", default=0)
    is_published = models.BooleanField("是否发布", default=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        ordering = ["-weight", "-created_at"]
        indexes = [
            models.Index(fields=["is_published", "category", "-weight"]),
            models.Index(fields=["title"]),
        ]
        verbose_name = "搜索内容"
        verbose_name_plural = "搜索内容"

    def __str__(self) -> str:
        return self.title


class ContactLead(models.Model):
    class Interest(models.TextChoices):
        AGENT = "agent", "脑电大模型智能体"
        TRAINING = "training", "机器人训练"
        COMPANION = "companion", "机器人陪伴"
        GENERAL = "general", "综合咨询"

    name = models.CharField("姓名", max_length=80)
    organization = models.CharField("机构/公司", max_length=120, blank=True)
    contact = models.CharField("联系方式", max_length=120)
    interest = models.CharField("咨询方向", max_length=32, choices=Interest.choices, default=Interest.GENERAL)
    message = models.TextField("需求描述")
    created_at = models.DateTimeField("创建时间", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "合作咨询"
        verbose_name_plural = "合作咨询"

    def __str__(self) -> str:
        return f"{self.name} - {self.get_interest_display()}"
