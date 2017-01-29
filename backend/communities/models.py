from django.db import models
from django.utils.translation import ugettext_lazy as _


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

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return _("VK Request Task %(type)s #%(id)d") % {'type': self.type, 'id': self.id }
