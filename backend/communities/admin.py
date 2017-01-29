from django.contrib import admin
from .models import VkCommunity, VkPerson

@admin.register(VkCommunity)
class VkCommunityAdmin(admin.ModelAdmin):
    readonly_fields = ('member_list_length', 'vk_id', 'estimated_members_count', 'member_list_length', 'is_valid', 'member_list')
    list_display = ('id', '__str__', 'vk_id', 'estimated_members_count', 'member_list_length', 'is_valid')


@admin.register(VkPerson)
class VkPersonAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'vk_id', 'first_name', 'last_name', 'sex')
    readonly_fields = ('vk_id', 'first_name', 'last_name', 'sex')
    list_filter = ('sex',)
