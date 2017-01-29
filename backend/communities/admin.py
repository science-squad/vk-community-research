from django.contrib import admin
from .models import VkCommunity

@admin.register(VkCommunity)
class VkCommunityAdmin(admin.ModelAdmin):
    readonly_fields = ('member_list_length',)
    list_display = ('id', '__str__', 'vk_id', 'estimated_members_count', 'member_list_length', 'is_valid')
