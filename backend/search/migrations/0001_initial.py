import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SearchDocument",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=120, verbose_name="标题")),
                ("summary", models.TextField(verbose_name="摘要")),
                ("body", models.TextField(verbose_name="正文")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("agent", "脑电大模型智能体"),
                            ("training", "机器人训练"),
                            ("companion", "机器人陪伴"),
                            ("company", "公司信息"),
                            ("faq", "FAQ"),
                        ],
                        max_length=32,
                        verbose_name="分类",
                    ),
                ),
                ("tags", models.JSONField(blank=True, default=list, verbose_name="标签")),
                ("url", models.CharField(max_length=200, verbose_name="链接")),
                ("weight", models.PositiveIntegerField(default=0, verbose_name="排序权重")),
                ("is_published", models.BooleanField(default=True, verbose_name="是否发布")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="创建时间")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="更新时间")),
            ],
            options={
                "verbose_name": "搜索内容",
                "verbose_name_plural": "搜索内容",
                "ordering": ["-weight", "-created_at"],
            },
        ),
        migrations.AddIndex(
            model_name="searchdocument",
            index=models.Index(fields=["is_published", "category", "-weight"], name="search_sear_is_publ_97bd4e_idx"),
        ),
        migrations.AddIndex(
            model_name="searchdocument",
            index=models.Index(fields=["title"], name="search_sear_title_1fe871_idx"),
        ),
    ]

