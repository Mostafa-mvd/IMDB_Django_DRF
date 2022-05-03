from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


from rest_framework import serializers
from . import models


class MoviesListSerializer(serializers.HyperlinkedModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name='movies_ns:movie_detail', format='html')

    class Meta:
        model = models.Movie
        fields = ('title', 'detail',)


class MovieDetailSerializer(serializers.HyperlinkedModelSerializer):
    show_reviews = serializers.HyperlinkedIdentityField(
        view_name='movies_ns:showing_movie_review', format='html')

    send_review = serializers.HyperlinkedIdentityField(
        view_name='movies_ns:sending_movie_review', format='html')
    
    def to_representation(self, instance):
        result = super().to_representation(instance)
        rating = instance.get_avg_rating()

        if rating:
            result['avg_rating'] = round(rating, 2)
        else:
            result['avg_rating'] = 0

        result['movie_duration'] = f"{result['duration_hour']}h{result['duration_min']}min"

        del result['duration_hour']
        del result['duration_min']

        return result

    class Meta:
        model = models.Movie
        fields = (
            'show_reviews', 'send_review', 
            'title', 'lang', 'date_posted',
            'story_line', 'genre',
            'released_date', 'poster',
            'duration_hour', 'duration_min',
        )
        

class SendReviewSerializer(serializers.ModelSerializer):
    commenter = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    def create(self, validated_data):
        pk = self.context['pk']
        movie_obj = get_object_or_404(klass=models.Movie, pk=pk)
        validated_data['reviewed_movie'] = movie_obj

        return models.Review.objects.create(**validated_data)


    class Meta:
        model = models.Review
        fields = ('commenter', 
                  'content', 
                  'rating')


class ListReviewsSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        result = super().to_representation(instance)

        commenter_pk = result['commenter']
        user_model = get_user_model()
        commenter_obj = user_model.objects.get(pk=commenter_pk)

        result["commenter"] = commenter_obj.username

        return result

    class Meta:
        model = models.Review
        fields = (
            'rating',
            'content',
            'commenter',
        )
