from django.db import IntegrityError
from rest_framework.generics import (ListAPIView, 
                                     CreateAPIView, 
                                     RetrieveAPIView)
from rest_framework import permissions

from . import custom_exceptions
from . import models
from . import serializers


class MoviesListView(ListAPIView):
    serializer_class = serializers.MoviesListSerializer
    queryset = models.Movie.objects.all()
    model = models.Movie


class MovieDetailView(RetrieveAPIView):
    serializer_class = serializers.MovieDetailSerializer
    queryset = models.Movie.objects.all()
    model = models.Movie


class MovieReviewView(CreateAPIView):
    model = models.Review
    serializer_class = serializers.MovieReviewSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def create(self, request, *args, **kwargs):
        # if users want to add another review and rating for movie we have duplicate record so
        # don't want to add duplicate review for one movie by users
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            raise custom_exceptions.DuplicateReviewException

    def get_serializer_context(self):
        serializer_context = super().get_serializer_context()
        serializer_context['pk'] = self.kwargs.get("pk", None)
        return serializer_context
