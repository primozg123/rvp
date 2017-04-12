from django.contrib import admin
from arhivator.models import *
# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):

    # search_fields = ('name', 'slug' )
    list_display = ('id', 'ime', 'priimek', 'datum_rojstva')
