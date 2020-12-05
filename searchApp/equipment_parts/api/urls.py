from django.urls import path
from .views import DetailsDetailView, DetailsListView, DetailsDestroyView

urlpatterns = [
    path('<pk>', DetailsDetailView.as_view()),
    path('', DetailsListView.as_view()),
    path('destroy/<pk>', DetailsDestroyView.as_view()),
]