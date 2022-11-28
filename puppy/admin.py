from django.contrib import admin
from .models import VisitorsModel, OurTeamModel, PetsModel


admin.site.register(PetsModel)


@admin.register(VisitorsModel)  # Обертка для регистрации админки
class PetProjectAdmin(admin.ModelAdmin):
    """Ициализируем класс админки для постоянных посетителей"""
    list_display = ['name', 'surname', 'comments', 'image']
    list_editable = ['surname', 'comments', 'image']
    ordering = ["name"]
    list_per_page = 10


@admin.register(OurTeamModel)  # Обертка для регистрации админки
class PetProjectAdmin(admin.ModelAdmin):
    """Ициализируем класс админки для работников ветклиники"""
    list_display = ['name', 'surname', 'role', 'image']
    list_editable = ['surname', 'role', 'image']
    ordering = ["name"]
    list_per_page = 10
