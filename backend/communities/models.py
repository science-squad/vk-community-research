from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Max
from django.conf import settings
import simplejson as json


class VkCommunity(models.Model):

    class Meta:
        verbose_name = _('vk community')
        verbose_name_plural = _('vk communities')

    vk_id = models.PositiveIntegerField(verbose_name=_('vk id'))
    estimated_members_count = models.PositiveIntegerField(verbose_name=_('estimated members count'), null=True)
    member_list = models.TextField(blank=True, null=True)
    member_list_length = models.PositiveIntegerField(verbose_name=_('loaded member list length'), null=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return _("Group #%d") % self.vk_id

    @property
    def is_valid(self):
        return self.member_list_length == self.estimated_members_count


class VkPerson(models.Model):

    class Meta:
        verbose_name = _('vk person')
        verbose_name_plural = _('vk persons')

    vk_id = models.PositiveIntegerField(verbose_name=_('vk id'))
    first_name = models.CharField(verbose_name=_('first name'), max_length=255, blank=True, null=True)
    last_name = models.CharField(verbose_name=_('last name'), max_length=255, blank=True, null=True)
    sex = models.IntegerField(verbose_name=_('sex'), null=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


VK_REQUEST_TASK_TYPE_CHOICES = (
    ('ecmc', _('estimate communities member count')),
    ('rcml', _('request communities member list')),
)


class VkRequestTask(models.Model):

    class Meta:
        verbose_name = _('vk request task')
        verbose_name_plural = _('vk request task')

    start_vk_id = models.PositiveIntegerField(verbose_name=_('start vk id'))
    stop_vk_id = models.PositiveIntegerField(verbose_name=_('stop vk id'))
    type = models.CharField(choices=VK_REQUEST_TASK_TYPE_CHOICES, max_length=10)

    is_done = models.BooleanField(verbose_name=_('is done'), default=False)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return _("VK Request Task %(type)s #%(id)d") % {'type': self.type, 'id': self.id }

    @classmethod
    def create_task(cls):
        start = (cls.objects.all().aggregate(Max('stop_vk_id'))['stop_vk_id__max'] or 0) + 1
        stop = start + int(settings.VK_COMMUNITY_STEP)
        new_task = cls(start_vk_id=start, stop_vk_id=stop, type='ecmc')
        new_task.save()
        return new_task

    @classmethod
    def handle_task_results(cls, id, type, result):
        task = cls.objects.get(id=id)
        if task.type != type:
            return False
        if cls.handle_specific_task_type_result(type, result):
            task.is_done = True
            task.save()
            return True
        else:
            return False

    @classmethod
    def handle_specific_task_type_result(cls, type, result):
        if type != 'ecmc':
            return False
        # ] result is a JSON dictionary { gid: count_of_members, ... }
        result = json.loads(result)
        for gid in result:
            # fail if id mismatch
            c = VkCommunity(vk_id=gid, estimated_members_count=result[gid])
            c.save()
        return True

    def to_dict(self):
        return {
            'start': self.start_vk_id,
            'stop': self.stop_vk_id,
            'id': self.id,
            'type': self.type
        }