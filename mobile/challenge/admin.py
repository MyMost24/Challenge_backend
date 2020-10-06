from django.contrib import admin
from challenge.models import Challenge, Video
# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'video', 'image')

class VideoInline(admin.TabularInline):
    model = Video

class ChallengeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image']
    inlines = [
        VideoInline
    ]

admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(Video, VideoAdmin)