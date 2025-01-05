import os
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Document
from .serializers import DocumentSerializer

class DocumentUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file uploaded'}, status=400)

        # Save the uploaded file
        document = Document(file=file)
        document.save()

        # Parse the content of the uploaded file
        file_path = document.file.path
        document.content = self.parse_file(file_path)
        document.save()

        return Response({'message': 'File uploaded successfully', 'document_id': document.id, 'content': document.content}, status=201)

    def parse_file(self, file_path):
        # Handle plain text files for now
        if file_path.endswith('.txt'):
            with open(file_path, 'r') as f:
                return f.read()
        return "Unsupported file format"

class QueryView(APIView):
    def post(self, request, *args, **kwargs):
        query = request.data.get('query')
        document_id = request.data.get('document_id')

        if not query or not document_id:
            return Response({'error': 'Query or document ID missing'}, status=400)

        # Retrieve the document
        try:
            document = Document.objects.get(id=document_id)
        except Document.DoesNotExist:
            return Response({'error': 'Document not found'}, status=404)

        # Process the query with Google Gemini API
        answer = self.get_answer_from_gemini(query, document.content)

        return Response({'answer': answer})

    def get_answer_from_gemini(self, query, document_content):
        # Replace YOUR_API_KEY with your actual API key
        url = 'https://gemini.googleapis.com/v1/models/flash:model'
        headers = {
            'Authorization': 'Bearer YOUR_API_KEY',
            'Content-Type': 'application/json',
        }
        payload = {
            "input_text": query,
            "context": document_content,
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json().get('output_text', 'No answer found')
        else:
            return "Error fetching response from Google Gemini API"
