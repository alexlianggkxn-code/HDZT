from django.contrib import admin
from django.utils import timezone

from .models import ContactLead, SearchDocument

admin.site.site_header = "沪东智体后台管理"
admin.site.site_title = "沪东智体后台"
admin.site.index_title = "内容与咨询管理"


@admin.register(SearchDocument)
class SearchDocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "weight", "is_published", "updated_at")
    list_filter = ("category", "is_published")
    search_fields = ("title", "summary", "body")
    ordering = ("-weight", "-created_at")
    list_per_page = 20
    fieldsets = (
        ("基础内容", {"fields": ("title", "summary", "body", "url")}),
        ("分类与发布", {"fields": ("category", "tags", "weight", "is_published")}),
    )


@admin.register(ContactLead)
class ContactLeadAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "organization_display",
        "contact",
        "interest",
        "message_preview",
        "submitted_at",
    )
    list_filter = ("interest", "created_at")
    search_fields = ("name", "organization", "contact", "message")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
    list_per_page = 20
    date_hierarchy = "created_at"
    fieldsets = (
        ("联系人信息", {"fields": ("name", "organization", "contact")}),
        ("咨询内容", {"fields": ("interest", "message")}),
        ("系统记录", {"fields": ("created_at",)}),
    )

    @admin.display(description="机构/公司", ordering="organization")
    def organization_display(self, obj: ContactLead) -> str:
        return obj.organization or "未填写"

    @admin.display(description="留言摘要")
    def message_preview(self, obj: ContactLead) -> str:
        if len(obj.message) <= 28:
            return obj.message
        return f"{obj.message[:28]}..."

    @admin.display(description="提交时间", ordering="created_at")
    def submitted_at(self, obj: ContactLead) -> str:
        return timezone.localtime(obj.created_at).strftime("%Y-%m-%d %H:%M")
