from django import forms
from exam_prep.web.models import Profile, Album


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    # тук ще си направим две методчета, които да ни направят полетата hidden - сиреч да не се показват
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def __set_hidden_fields(self):
        for _, field in self.fields.items():   # тук fields идва от django и то е речник и за това казваме .items()
            field.widget = forms.HiddenInput()

    # тук ще напишем логиката за изтриване на профила и всички албуми, които има профила. Save метода при формите взима
    # един параметър commit, който има две възможни стойности True и False. Ако е True, това означава че трябва да се
    # персистне към базата, а ако е False обратното.
    def save(self, commit=True):
        if commit:
            Album.objects.all().delete()
            self.instance.delete()
        return self.instance  # това е попълнената инстанция, която model формата е направила


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name'
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description'
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price'
                }
            ),
        }


class AlbumCreateForm(AlbumBaseForm):
    pass


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(AlbumBaseForm):
    # тук ще си направим две методчета, които да ни направят полетата disabled - сиреч да не може да ги променяме
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for _, field in self.fields.items():   # тук fields идва от django и то е речник и за това казваме .items()
            field.widget.attrs['readonly'] = 'readonly'

    # тук ще напишем логиката за изтриване на албума. Save метода при формите взима един параметър commit, който има две
    # възможни стойности True и False. Ако е True, това означава че трябва да се персистне към базата, а ако е False обратното.
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance    # това е попълнената инстанция, която model формата е направила



