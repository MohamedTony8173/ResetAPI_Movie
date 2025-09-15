from django.urls import path
from .views import (
    GuestViewSerializer,
    GuestUpdateDeleteView,
    MixinTicketsList,
    MixinTicketUpdateDelete,
    GenericMovieList,
    GenericMovieUpdateDelete,
    find_movie,
    reservationMovie
)


urlpatterns = [
    path("", GuestViewSerializer.as_view()),
    path("<int:pk>/", GuestUpdateDeleteView.as_view()),
    path("tickets/", MixinTicketsList.as_view()),
    path("tickets/<int:pk>/", MixinTicketUpdateDelete.as_view()),
    path("movie/", GenericMovieList.as_view()),
    path("movie/<int:pk>/", GenericMovieUpdateDelete.as_view()),
    path("movie/find/", find_movie),
    path("ticket/create/", reservationMovie),
]
