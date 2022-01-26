from django.urls import path
from .views import RoomView

# URLConf
urlpatterns = [
    path('home/', RoomView.as_view()) # as_view means take this class and give me view
]