from django.contrib import admin
from .models import ControlLog, Recommendation

@admin.register(ControlLog)
class ControlLogAdmin(admin.ModelAdmin):
    list_display = ('log_id', 'user_id', 'device_id', 'create_time', 'update_time', 'status')  # Customize as needed
    search_fields = ('log_id', 'user_id__username', 'device_id__device_id')  # Adjust based on related fields

@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('user', 'time', 'recommendation')  # Customize as needed
    search_fields = ('user__username', 'recommendation')  # Adjust based on related fields