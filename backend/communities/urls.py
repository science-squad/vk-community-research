from django.conf.urls import url
from .views import get_next_task, report_task_result

urlpatterns = [
    url(r'^get_next_task/', get_next_task),
    url(r'^report_task_result/', report_task_result),
]