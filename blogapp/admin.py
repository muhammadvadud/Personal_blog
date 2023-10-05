from django.contrib import admin
from .models import Experience,Education,Setting,Portfolio,Blog,Contact,About
from django.contrib.admin import ModelAdmin


class SettingsView(ModelAdmin):
    list_display = ("key","value")

admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Setting,SettingsView)
admin.site.register(Portfolio)
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(About)


