from django.contrib import admin
from final_exam.web.models import ProfileModel, EventModel


@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(EventModel)
class AlbumAdmin(admin.ModelAdmin):
    pass
