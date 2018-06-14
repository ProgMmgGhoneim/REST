from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('bucketlist', CreateView.as_view() ,name='create'),
    path('bucketlist/<int:pk>',
        DetailsView.as_view(), name="details")
]
urlpatterns = format_suffix_patterns(urlpatterns)
