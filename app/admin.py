from app.models import Contact
from django.contrib import admin

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contact, ContactAdmin)

