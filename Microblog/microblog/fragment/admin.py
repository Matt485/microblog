from django.contrib import admin

from .models import TextPost, AudioPost, Blog

# Register the custom models
admin.site.register(TextPost)
admin.site.register(AudioPost)
admin.site.register(Blog)
