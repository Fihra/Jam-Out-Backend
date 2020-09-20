from jams.api.views import JamViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', JamViewSet, basename='jams')
urlpatterns = router.urls

# from django.urls import path

# from .views import (
#     JamListView, 
#     JamDetailView,
#     JamCreateView,
#     JamUpdateView,
#     JamDeleteView
# )

# urlpatterns = [
#     path('', JamListView.as_view()),
#     path('create/', JamCreateView.as_view()),
#     path('<pk>', JamDetailView.as_view()),
#     path('<pk>/update/', JamUpdateView.as_view()),
#     path('<pk>/delete/', JamDeleteView.as_view()),
# ]