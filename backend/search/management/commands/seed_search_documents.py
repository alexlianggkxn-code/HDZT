from django.core.management.base import BaseCommand

from search.models import SearchDocument


SEED_DOCUMENTS = [
    {
        "title": "脑电大模型智能体建设",
        "summary": "围绕脑电相关数据处理、任务记录和智能体流程编排开展研发。",
        "body": "沪东智体围绕脑电相关数据处理、多模态任务记录和智能体流程编排开展研发，探索脑电数据在机器人训练和交互研究中的工程化应用。",
        "category": SearchDocument.Category.AGENT,
        "tags": ["脑电数据", "智能体流程", "人机交互"],
        "url": "/#agent",
        "weight": 50,
    },
    {
        "title": "机器人训练动态标签",
        "summary": "结合语音、视频、动作和脑电相关记录，辅助机器人训练数据标注。",
        "body": "围绕机器人训练，系统整理语音、视频、动作和脑电相关记录，辅助形成动态标签、过程说明和复盘材料，提升训练数据的可追溯性。",
        "category": SearchDocument.Category.TRAINING,
        "tags": ["机器人训练", "动态标签", "训练数据"],
        "url": "/#training",
        "weight": 40,
    },
    {
        "title": "机器人陪伴内容",
        "summary": "面向陪伴机器人整理场景化对话、内容脚本和交互反馈素材。",
        "body": "沪东智体关注陪伴机器人的场景化对话、用户偏好记录和交互反馈整理，让陪伴机器人在家庭、展厅和服务场景中的表达更自然稳定。",
        "category": SearchDocument.Category.COMPANION,
        "tags": ["机器人陪伴", "内容建设", "场景对话"],
        "url": "/#companion",
        "weight": 35,
    },
    {
        "title": "沪东智体公司信息",
        "summary": "沪东智体人工智能科技（上海）有限公司，税号 91310116MAEKJPKT70。",
        "body": "沪东智体人工智能科技（上海）有限公司关注脑电相关数据处理、机器人训练数据和陪伴机器人内容建设方向。公司税号：91310116MAEKJPKT70。",
        "category": SearchDocument.Category.COMPANY,
        "tags": ["公司信息", "沪东智体", "税号"],
        "url": "/#top",
        "weight": 30,
    },
    {
        "title": "如何维护官网搜索内容？",
        "summary": "首版通过 Django Admin 维护站内搜索内容，支持分类、标签、权重和发布状态。",
        "body": "管理员可以登录 Django Admin 新增或编辑 SearchDocument。未发布内容不会出现在 API 搜索结果中。",
        "category": SearchDocument.Category.FAQ,
        "tags": ["FAQ", "Django Admin", "内容维护"],
        "url": "/#search",
        "weight": 20,
    },
]


class Command(BaseCommand):
    help = "Seed first-version website search documents."

    def handle(self, *args, **options):
        created = 0
        updated = 0

        for item in SEED_DOCUMENTS:
            _, was_created = SearchDocument.objects.update_or_create(
                title=item["title"],
                defaults=item,
            )
            if was_created:
                created += 1
            else:
                updated += 1

        self.stdout.write(
            self.style.SUCCESS(f"Seeded search documents: {created} created, {updated} updated.")
        )
