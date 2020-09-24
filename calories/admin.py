from django.contrib import admin
from .models import Food,Profile,PostFood
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Food)
admin.site.register(Profile)
admin.site.register(PostFood)

