from django import forms
from final_exam.web.models import ProfileModel, EventModel


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ('email', 'profile_picture', 'password', )


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class ProfileDeleteForm(ProfileBaseForm):
    class Meta:
        model = ProfileModel
        fields = ()

    def save(self, commit=True):
        if commit:
            EventModel.objects.all().delete()
            self.instance.delete()
        return self.instance


class EventBaseForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = '__all__'


class EventCreateForm(EventBaseForm):
    pass


class EventEditForm(EventBaseForm):
    pass


class EventDeleteForm(EventBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
