from django import forms
from django.core.exceptions import ValidationError

from forms_part_2_demos.web.model_validators import validate_max_todos_per_person
from forms_part_2_demos.web.models import ToDo, Person
from forms_part_2_demos.web.validators import validate_text, ValueInRangeValidator


class TodoForm(forms.Form):
    text = forms.CharField(
        validators=(
            validate_text,
        ),
    )
    is_done = forms.BooleanField(
        required=False,
    )

    priority = forms.IntegerField(
        validators=(
            # validate_priority,
            # MinValueValidator(1),
            # MaxValueValidator(10),
            ValueInRangeValidator(1, 10),
        ),
    )


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = '__all__'

    def clean(self):
        return super().clean()

    # the next one is used to transform data into desired format and for validation
    def clean_text(self):
        return self.cleaned_data['text'].lower()

    # for validation
    # def clean_assignee(self):
    #     assignee = self.cleaned_data['assignee']
    #     validate_max_todos_per_person(assignee)
    #     return assignee

    # for transforming data
    def clean_assignee(self):
        assignee = self.cleaned_data['assignee']

        try:
            validate_max_todos_per_person(assignee)
        except ValidationError:
            assignee = Person.objects.get(name='Unassigned')
        return assignee


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def clean_profile_image(self):
        profile_image = self.cleaned_data['profile_image']
        profile_image.name = self.cleaned_data['name']
        return profile_image

    # def clean(self):
    #     super().clean()   # After this, all values are in 'cleaned_data'
    #     profile_image = self.cleaned_data['profile_image']
    #     profile_image.name = self.cleaned_data['name']


