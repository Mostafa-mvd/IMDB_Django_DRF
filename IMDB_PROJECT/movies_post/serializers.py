from rest_framework import serializers
from . import models


class MoviesListSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        result = super().to_representation(instance)
        rating = instance.get_avg_rating()
        result['avg_rating'] = round(rating, 2)
        result['movie_duration'] = f"{result['duration_hour']}h{result['duration_min']}min"

        del result['duration_hour']
        del result['duration_min']

        return result

    class Meta:
        model = models.Movie
        fields = '__all__'
