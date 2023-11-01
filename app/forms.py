from django import forms
from django.contrib.auth.models import User
from .models import Question, Answer, Vote


class UserRegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["placeholder"] = "Enter First Name"
        self.fields["last_name"].widget.attrs["placeholder"] = "Enter Last Name"
        self.fields["email"].widget.attrs["placeholder"] = "Enter Email Address"
        self.fields["username"].widget.attrs["placeholder"] = "Enter Username"
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Enter Password"
        }
    ))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Confirm Password"
        }
    ))
    username = forms.CharField()

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password",)

    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        password = cleaned_data["password"]
        confirm_password = cleaned_data["confirm_password"]

        if password != confirm_password:
            raise forms.ValidationError(
                message="Password does not match!"
            )

    def save(self, commit=True):
        instance = super(UserRegisterForm, self).save(commit=False)
        instance.set_password(self.cleaned_data["password"])
        if commit:
            instance.save()
        return instance


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     first_name = forms.CharField(max_length=20)
#     last_name = forms.CharField(max_length=20)

#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2",)


class QuestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields["content"].widget.attrs["placeholder"] = "Ask your question"
        self.fields["content"].widget.attrs["class"] = "form-control"

    class Meta:
        model = Question
        fields = ("content", )


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ("content",)


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ("answer",)

