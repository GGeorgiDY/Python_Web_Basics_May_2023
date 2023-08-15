from django import forms
from exam_june_2023.web.models import Profile, Fruit


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'password', )

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'password': forms.TextInput(
                attrs={
                    'placeholder': 'Password'
                }
            ),
        }


class ProfileCreateForm(ProfileBaseForm):
    # така махам лейбълите
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = ""
        self.fields['last_name'].label = ""
        self.fields['email'].label = ""
        self.fields['password'].label = ""


class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url', 'age', )


class ProfileDeleteForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ()

    # тук ще напишем логиката за изтриване на профила. Save метода при формите взима един параметър commit, който има две
    # възможни стойности True и False. Ако е True, това означава че трябва да се персистне към базата, а ако е False обратното.
    def save(self, commit=True):
        if commit:
            Fruit.objects.all().delete()
            self.instance.delete()
        return self.instance  # това е попълнената инстанция, която model формата е направила


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'

        widgets = {
            'fruit_name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name'
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Full Image URL'
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
    # така махам лейбълите
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fruit_name'].label = ""
        self.fields['image_url'].label = ""
        self.fields['description'].label = ""
        self.fields['nutrition'].label = ""


class FruitEditForm(FruitBaseForm):
    pass


class FruitDeleteForm(FruitBaseForm):
    class Meta:
        model = Fruit
        fields = ('fruit_name', 'image_url', 'description',)

    # тук ще си направим две методчета, които да ни направят полетата disabled - сиреч да не може да ги променяме
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for _, field in self.fields.items():  # тук fields идва от django и то е речник и за това казваме .items()
            field.widget.attrs['readonly'] = 'readonly'

    # тук ще напишем логиката за изтриване на албума. Save метода при формите взима един параметър commit, който има две
    # възможни стойности True и False. Ако е True, това означава че трябва да се персистне към базата, а ако е False обратното.
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance  # това е попълнената инстанция, която model формата е направила
