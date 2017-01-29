from django.http import HttpResponse
import simplejson as json


def get_next_task(request):
    data = json.dumps({'start': 100, 'stop': 1000}),
    return HttpResponse(data, content_type='application/json')
