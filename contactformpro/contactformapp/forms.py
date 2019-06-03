from django import forms

class ContactForm(forms.Form):
    first_name=forms.CharField(
        label="Enter Your First Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'First Name',
                'class':'form-control'
            }
        )
    )
    last_name=forms.CharField(
        label="Enter Your Last Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Last Name',
                'class':'form-control'
            }
        )
    )
    username=forms.CharField(
        label="Enter Your UserName",
        widget=forms.TextInput(
            attrs={
                'placeholder':'UserName',
                'class':'form-control'
            }

        )
    )
    password=forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password',
                'class':'form-control'
            }
        )
    )
    email=forms.EmailField(
        label="Enter Your Email ID",
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Email ID',
                'class':'form-control'
            }
        )
    )
    mobile=forms.IntegerField(
        label="Enter Your Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Mobile Number',
                'class':'form-control'
            }
        )
    )