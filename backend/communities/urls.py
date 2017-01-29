from django.conf.urls import url
from .views import get_next_task

urlpatterns = [
    url(r'^get_next_task/', get_next_task)
]