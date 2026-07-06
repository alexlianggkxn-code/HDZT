from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import SearchDocument
from .serializers import ContactLeadSerializer, SearchDocumentSerializer


class HealthView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return Response(
            {
                "status": "ok",
                "service": "hudongzhiti-api",
                "company": "沪东智体人工智能科技（上海）有限公司",
            }
        )


class SearchView(APIView):
    def get(self, request):
        query = request.query_params.get("q", "").strip()
        category = request.query_params.get("category", "").strip()

        documents = SearchDocument.objects.filter(is_published=True)

        if category:
            documents = documents.filter(category=category)

        if query:
            documents = documents.filter(
                Q(title__icontains=query)
                | Q(summary__icontains=query)
                | Q(body__icontains=query)
                | Q(tags__icontains=query)
            )

        documents = documents.order_by("-weight", "-created_at")[:20]
        serializer = SearchDocumentSerializer(documents, many=True)

        return Response(
            {
                "query": query,
                "count": len(serializer.data),
                "results": serializer.data,
            }
        )


class ContactLeadView(APIView):
    def post(self, request):
        serializer = ContactLeadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        lead = serializer.save()

        return Response(
            {
                "id": lead.id,
                "message": "咨询已提交，我们会尽快联系您。",
            },
            status=status.HTTP_201_CREATED,
        )
