from django.urls import path
from .views import ListCreateSongsView, SongsDetailView, ArtistDetailView, ArtistListCreateView


urlpatterns = [
    path('artists/', ArtistListCreateView.as_view(), name="artists-list-create"),
    path('artists/<int:pk>/', ArtistDetailView.as_view(), name="song-list-create"),
    path('artists/<int:pk>/songs/', ListCreateSongsView.as_view(), name="song-list-create"),
    path('songs/<int:pk>/', SongsDetailView.as_view(), name="song-detail-view"),
]