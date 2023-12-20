from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TopicPageRelatedLink
from wagtail.documents.models import Document

class DocumentsOfAPageAPIView(APIView):
    def get(self, request, pk):
        try:
            topic_page_links = TopicPageRelatedLink.objects.filter(page_id=pk)
            documents = []
            for link in topic_page_links:
                document = link.document
                documents.append({'document_id': document.id, 'document_name': document.title})
                # Add more fields as needed

            return Response({'documents': documents}, status=status.HTTP_200_OK)
        except TopicPageRelatedLink.DoesNotExist:
            return Response({'error': 'TopicPageRelatedLink not found'}, status=status.HTTP_404_NOT_FOUND)
