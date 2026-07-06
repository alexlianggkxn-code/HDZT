from rest_framework import serializers

from .models import ContactLead, SearchDocument


class SearchDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchDocument
        fields = ("id", "title", "summary", "category", "tags", "url")


class ContactLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactLead
        fields = ("id", "name", "organization", "contact", "interest", "message", "created_at")
        read_only_fields = ("id", "created_at")

    def validate_name(self, value):
        value = value.strip()
        if len(value) < 2:
            raise serializers.ValidationError("请填写至少 2 个字符的姓名。")
        return value

    def validate_contact(self, value):
        value = value.strip()
        if len(value) < 5:
            raise serializers.ValidationError("请填写有效联系方式。")
        return value

    def validate_message(self, value):
        value = value.strip()
        if len(value) < 10:
            raise serializers.ValidationError("需求描述至少需要 10 个字符。")
        return value
