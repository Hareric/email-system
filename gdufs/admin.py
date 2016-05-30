from django.contrib import admin
from .models import Person, Email
# Register your models here.


class EmailAdmin(admin.ModelAdmin):
    list_display = ('title', 'to_ID_number', 'time')


admin.site.register(Person)
admin.site.register(Email, EmailAdmin)

