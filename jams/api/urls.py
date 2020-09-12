from django.urls import path

from .views import JamListView, JamDetailView

urlpatterns = [
    path('', JamListView.as_view()),
    path('<pk>', JamDetailView.as_view()),
]