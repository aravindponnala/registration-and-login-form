from django import forms
class RegistrationForm(forms.Form):
    first_name=forms.CharField(
        label="enter your first name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your first name',
            }
        )
    )
    last_name=forms.CharField(
        label="enter your last name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your last name'
            }
        )

    )
    mobile=forms.IntegerField(
        label="enter your last name",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your mobile no'
            }
        )

    )
    email=forms.EmailField(
        label="enter your email id",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'your email id'
            }
        )

    )
    usernamerf=forms.CharField(
        label="enter your user name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your user_name'
            }
        )

    )
    password1=forms.CharField(
        label="enter your password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'your password'
            }
        )

    )
    password2=forms.CharField(
        label="enter conformation password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'your conformation password'
            }
        )

    )


class LoginForm(forms.Form):
    usernamel=forms.CharField(
        label="enter username",
        widget=forms.TextInput(
            attrs={
                'class':'forms-control',
                'placeholder':'your username'
            }
        )
    )
    password11=forms.CharField(
        label="enter password",
        widget=forms.PasswordInput(
            attrs={
                'class':'forms-control',
                'placeholder':'your password'
            }
        )
    )