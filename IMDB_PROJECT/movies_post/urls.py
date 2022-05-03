from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


app_name = "movies"

urlpatterns = [
    path('list/', views.MoviesListView.as_view(), name='movies_list'),
    path('<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('<int:pk>/review/', views.MovieReviewView.as_view(), name='movie_review'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
