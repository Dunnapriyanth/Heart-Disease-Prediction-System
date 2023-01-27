from django import forms
from .models import userInfoModel


# creating a form
# class UserForm(forms.ModelForm):
#     # create meta class
#     class Meta:
#         # specify model to be used
#         model = userModel
#         fields = '__all__'
#         # # specify fields to be used
#         # fields = [
#         #     "email",
#         #     "username",
#         #     "password",
#         # ]

class UserInfoForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = userInfoModel
        fields = '__all__'
