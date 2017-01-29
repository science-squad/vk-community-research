from django import forms


class VkRequestTaskReportForm(forms.Form):
    type = forms.CharField(label='task type', max_length=100)
    id = forms.IntegerField(label='task id')
    result = forms.CharField(label='result')