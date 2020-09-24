from django.contrib import admin
from django.forms import Textarea
from django.db.models.fields import TextField

from . import models

# Register your models here.
class SamochodInLine(admin.TabularInline):
    model = models.Samochod
    fields = ['nazwa', 'paliwo', 'ile_litrow_pali_na_100_km']
    extra = 2
    max_num = 10


@admin.register(models.Zespol)
class ZespolAdmin(admin.ModelAdmin):
    exclude = ('autor',)
    inlines = [SamochodInLine]
    search_fields = ['nazwa']
    list_per_page = 15
    formfield_overrides = {
        TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100})},
    }

    def save_model(self, request, obj, form, change):
        if not change:
            obj.autor = request.user
        obj.save()
