from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of content in admin
    """
    summernote_fields = ('content',)

# Note: CollaborateRequest model is not present in `about.models`.
# The migration `0002_collaboraterequest.py` exists (historical),
# so we avoid registering the model here to prevent import errors.