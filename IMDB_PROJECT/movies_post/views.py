from rest_framework.generics import ListAPIView
from . import models
from . import serializers


class MovieListView(ListAPIView):
    serializer_class = serializers.MoviesListSerializer
    queryset = models.Movie.objects.all()
    model = models.Movie
