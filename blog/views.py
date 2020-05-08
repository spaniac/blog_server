from datetime import datetime

from blog.models import User
from blog.serializers import UserSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return User.objects.all()

    def filter_queryset(self, queryset):
        return queryset.filter(is_deleted=False)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        result = self.get_serializer(self.get_object(), data=request.data, partial=True)
        result.is_valid(raise_exception=True)
        result.save()
        return Response(result.data)

    def destroy(self, request, *args, **kwargs):
        self.perform_destroy(self.get_object())
        return Response('success delete', status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.deleted_at = datetime.now()
        instance.save()
