from django.contrib import admin
from final_exam_2023.web.models import ProfileModel, FruitModel


@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    pass


@admin.register(FruitModel)
class ProfileModelAdmin(admin.ModelAdmin):
    pass
