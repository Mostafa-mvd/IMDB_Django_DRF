from django.db import models


class LanguageChoice(models.TextChoices):
    DE = "German"
    EN = "English"
    CN = "Chinese"
    ES = "Spanish"


class GenreChoice(models.TextChoices):
    SF = "Science_Fiction"
    DR = "Drama"
    AC = "Action"
    HO = "Horror"

class MovieCrewChoice(models.TextChoices):
    Director = "Director"
    Writer = "Writer"
    Cinematographer = "Cinematographer"
