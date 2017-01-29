from django.http import HttpResponse
import simplejson as json
from .models import VkRequestTask


def get_next_task(request):
    next_task = VkRequestTask.create_task()
    data = json.dumps(next_task.to_dict()),
    return HttpResponse(data, content_type='application/json')
