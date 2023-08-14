from django import forms


class PersonForm(forms.Form):
    OCCUPANCIES = (
        (1, 'Child'),
        (2, 'High school student'),
        (3, 'Student'),
        (4, 'Adult'),
    )

    your_name = forms.CharField(
        max_length=30,
        help_text='Enter your name',
        widget=forms.TextInput(
            # This corresponds to HTML attributes
            attrs={
                'placeholder': 'Enter name',
                'class': 'form-control',
            },
        ),
    )

    age = forms.IntegerField(
        required=False,
        label='Your age',
        initial=0,
    )

    # story = forms.CharField(
    #     widget=forms.Textarea(),
    # )
    #
    # email = forms.CharField(
    #     widget=forms.EmailInput(),
    # )
    #
    # url = forms.CharField(
    #     widget=forms.URLInput(),
    # )
    #
    # secret = forms.CharField(
    #     widget=forms.PasswordInput(),
    # )
    #
    occupancy = forms.ChoiceField(
        choices=OCCUPANCIES,
        widget=forms.Select,  # This is the default for 'ChoiceField'
    )
    #
    # occupancy2 = forms.ChoiceField(
    #     choices=OCCUPANCIES,
    #     widget=forms.RadioSelect(),
    # )
    #
    # occupancy3 = forms.ChoiceField(
    #     choices=OCCUPANCIES,
    #     widget=forms.SelectMultiple(),
    # )