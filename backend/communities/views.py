from django.http import HttpResponse
import simplejson as json
from django.conf import settings
from .models import VkRequestTask


def get_next_task(request):
    start = VkRequestTask.get_next_task_start_id()
    stop = start + int(settings.VK_COMMUNITY_STEP)
    data = json.dumps({'start': start, 'stop': stop}),
    return HttpResponse(data, content_type='application/json')
