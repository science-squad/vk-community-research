from django.db import models
from django.utils.translation import ugettext_lazy as _


class VkCommunity(models.Model):

    class Meta:
        verbose_name = _('vk model')
        verbose_name_plural = _('vk models')

    vk_id = models.PositiveIntegerField(verbose_name=_('vk id'))
    estimated_members_count = models.PositiveIntegerField(verbose_name=_('estimated members count'), null=True)
    member_list = models.TextField(blank=True, null=True)
    member_list_length = models.PositiveIntegerField(verbose_name=_('loaded member list length'), null=True)

    def __str__(self):
        return _("Group #%d") % self.vk_id

    @property
    def is_valid(self):
        return self.member_list_length == self.estimated_members_count

