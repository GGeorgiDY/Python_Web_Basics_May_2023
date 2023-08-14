from django import forms
from final_exam_2023.web.models import ProfileModel, FruitModel


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ('first_name', 'last_name', 'email', 'password')

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email'

                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password'
                }
            ),
        }

        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = ProfileModel
        fields = ('first_name', 'last_name', 'email', 'age')


class ProfileDeleteForm(ProfileBaseForm):
    class Meta:
        model = ProfileModel
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Fruit Image URL'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Fruit Description'

                }
            ),
            'nutrition': forms.Textarea(
                attrs={
                    'placeholder': 'Nutrition Info'
                }
            ),
        }


class FruitCreateForm(FruitBaseForm):
    class Meta:
        model = FruitModel
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Fruit Image URL'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Fruit Description'

                }
            ),
            'nutrition': forms.Textarea(
                attrs={
                    'placeholder': 'Nutrition Info'
                }
            ),
        }

        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }


class FruitEditForm(FruitBaseForm):
    pass


class FruitDeleteForm(FruitBaseForm):
    class Meta:
        model = FruitModel
        fields = ('name', 'image_url', 'description')

    # тук ще си направим две методчета, които да ни направят полетата disabled - сиреч да не може да ги променяме
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for _, field in self.fields.items():    # тук fields идва от django и то е речник и за това казваме .items()
            field.widget.attrs['readonly'] = 'readonly'

    # тук ще напишем логиката за изтриване на албума. Save метода при формите взима един параметър commit, който има две
    # възможни стойности True и False. Ако е True, това означава че трябва да се персистне към базата, а ако е False обратното.
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance                       # това е попълнената инстанция, която model формата е направила
