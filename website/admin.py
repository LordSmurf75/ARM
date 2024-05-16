from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.models import Group, User
from .models import Bestyrelse, Spillested, Koncert, Frivillig 

# Unregister Group.
admin.site.unregister(Group)

class KoncerterSpillet(Koncert):
    class Meta:
        proxy = True
        verbose_name_plural = "Koncerter spillet"

class KoncerterSpilletAdmin(admin.ModelAdmin):
    list_display = ('navn', 'spillested', 'dato')
    
    def get_queryset(self, request):
        # Get the current date and time
        current_datetime = timezone.now()
        
        # Filter out upcoming concerts
        queryset = super().get_queryset(request).filter(dato__lt=current_datetime)
        
        return queryset

class KoncertAdmin(admin.ModelAdmin):
    list_display = ('navn', 'spillested', 'dato')
    
    def get_queryset(self, request):
        # Get the current date and time
        current_datetime = timezone.now()
        
        # Filter out concerts that have already passed
        queryset = super().get_queryset(request).filter(dato__gte=current_datetime)
        
        return queryset

admin.site.register(Bestyrelse)
admin.site.register(Spillested)
admin.site.register(Koncert, KoncertAdmin)
admin.site.register(KoncerterSpillet, KoncerterSpilletAdmin)
admin.site.register(Frivillig)
