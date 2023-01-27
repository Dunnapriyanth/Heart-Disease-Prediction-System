from django import forms

from .models import predictionInfo

class predictionInfoForm(forms.ModelForm):
    class Meta:
        model = predictionInfo
        fields = [
            'age', 'sex', 'HR', 'BloodSugar', 'chestPainType', 'RestingECG'
        ]

class row_predictionInfoForm(forms.ModelForm):
    class Meta:
        model = predictionInfo
        fields = [
            'age', 'sex', 'HR', 'BloodSugar', 'chestPainType', 'RestingECG'
        ]
