from django.contrib import admin
from .models import VkCommunity, VkPerson, VkRequestTask

@admin.register(VkCommunity)
class VkCommunityAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'vk_id', 'estimated_members_count', 'member_list_length', 'is_valid', 'created_at', 'updated_at')
    readonly_fields = ('member_list_length', 'vk_id', 'estimated_members_count', 'member_list_length', 'is_valid', 'member_list')


@admin.register(VkPerson)
class VkPersonAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'vk_id', 'first_name', 'last_name', 'sex', 'created_at', 'updated_at')
    readonly_fields = ('vk_id', 'first_name', 'last_name', 'sex')
    list_filter = ('sex',)


@admin.register(VkRequestTask)
class VkRequestTaskAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'start_vk_id', 'stop_vk_id', 'type', 'created_at', 'updated_at')
    readonly_fields = ('start_vk_id', 'stop_vk_id', 'type')
    list_filter = ('type',)
