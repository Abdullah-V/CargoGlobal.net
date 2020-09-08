from django.contrib import admin
from .models import elan
# Register your models here.


class filtre(admin.ModelAdmin):
    list_display = ['cixis_yeri','catma_yeri']
    list_filter = ['catma_vaxti','cixis_vaxti']
    search_fields = ['cixis_yeri','catma_yeri']
    list_display_links = ['cixis_yeri','catma_yeri']

    class Meta:
        model = elan


admin.site.register(elan,filtre)



