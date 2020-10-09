from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TestSerializer
from rest_framework import permissions


class TestView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        return Response({"Method": "GET"})

    def post(self, request, format=None):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data.get('text'))
        return Response(serializer.errors)
