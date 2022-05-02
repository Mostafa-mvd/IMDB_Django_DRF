from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


app_name = "movies"


urlpatterns = [
    path('list/', views.MovieListView.as_view(), name='movies_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
