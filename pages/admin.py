from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Theme

class ThemeAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Theme
        fields = "__all__"

class ThemeAdmin(admin.ModelAdmin):
    form = ThemeAdminForm

admin.site.register(Theme, ThemeAdmin)