from django.contrib import admin
from .models import Food,Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('time',)

admin.site.register(Food)
admin.site.register(Profile,ProfileAdmin)

