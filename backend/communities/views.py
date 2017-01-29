from django.http import HttpResponse
import simplejson as json
from .models import VkRequestTask
from .forms import VkRequestTaskReportForm


def get_next_task(request):
    next_task = VkRequestTask.create_task()
    data = json.dumps(next_task.to_dict()),
    return HttpResponse(data, content_type='application/json')


def report_task_result(request):
    form = VkRequestTaskReportForm(request.GET or None)
    if form.is_valid():
        result = VkRequestTask.handle_task_results(**form.cleaned_data)
    else:
        result = False
    data = json.dumps({'result': result}),
    return HttpResponse(data, content_type='application/json')
