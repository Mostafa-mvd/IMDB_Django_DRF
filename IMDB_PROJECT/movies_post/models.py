from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

from . import enums


class Movie(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True
    )

    lang = models.CharField(
        max_length=25,
        choices=[(tag, tag.value) 
                    for tag in enums.LanguageChoice]
    )

    date_posted = models.DateTimeField(auto_now_add=True)

    story_line = models.TextField(
        max_length=500
    )

    genre = models.CharField(
        max_length=25,
        choices=[(movie_genre, movie_genre.value)
                 for movie_genre in enums.GenreChoice]
    )

    released_date = models.DateField()

    poster = models.ImageField(upload_to='static/movies/%Y/%m/%d/')

    duration_hour = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)]
    )

    duration_min = models.IntegerField(
        validators=[MaxValueValidator(59)]
    )

    def __str__(self) -> str:
        return self.title
    
    def get_avg_rating(self):
        return self.review_set.aggregate(
            models.Avg("rating")
        ).get("rating__avg", 0)


class Review(models.Model):
    commenter = models.ForeignKey(
        to=get_user_model(), 
        on_delete=models.CASCADE)

    reviewed_movie = models.ForeignKey(
        to=Movie, 
        on_delete=models.CASCADE)

    content = models.TextField(
        max_length=250)

    rating = models.FloatField(
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0)])
    
    def __str__(self) -> str:
        return str(self.commenter)
    
    class Meta:
        unique_together = (
            'commenter', 'reviewed_movie'
        )


class Person(models.Model):
    first_name = models.CharField(
        max_length=50
    )

    last_name = models.CharField(
        max_length=50
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class MovieCast(models.Model):
    # It is our junction model
    # Model contains records of each person in a movie as a actors member

    #each person has relation with many movies
    person_name = models.ForeignKey(
        to=Person,
        on_delete=models.PROTECT
    )

    #one movie has many actors
    movie = models.ForeignKey(
        to=Movie,
        on_delete=models.PROTECT
    )

    character_name = models.CharField(
        max_length=50
    )

    def __str__(self) -> str:
        return f"{str(self.person_name)} -> {str(self.movie)}"

    class Meta:
        verbose_name_plural = "MoviesCast"
        unique_together = ("person_name", "movie", "character_name")


class MovieCrew(models.Model):
    # It is our junction model
    # Model contains records of each person in a movie as a crew member like director, photogragher, writer, etc

    person_name = models.ForeignKey(
        to=Person,
        on_delete=models.PROTECT
    )

    movie = models.ForeignKey(
        to=Movie,
        on_delete=models.PROTECT
    )

    job = models.CharField(
        max_length=25,
        choices=[(movie_job, movie_job.value)
                 for movie_job in enums.MovieCrewChoice]
    )

    def __str__(self) -> str:
        return f"({str(self.person_name)}, {str(self.job)}) -> {str(self.movie)}"

    class Meta:
        verbose_name_plural = "MoviesCrew"
        unique_together = ("person_name", "movie", "job")
