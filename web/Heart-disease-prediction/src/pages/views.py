from django.conf import settings
from django.conf.urls.static import static

from django.shortcuts import render
from django.http import HttpResponse
from .models import  userInfoModel
from .forms import UserInfoForm
import pickle
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect


# Create your views here.

def home_view(request, *args, **kwargs):
    print("static url=", settings.STATIC_URL)
    return render(request, 'home.html', {}) #string of html code

def user_heart_info_view(request, *args, **kwargs):
    return render(request, 'user_heart_info.html', {})

def result_view(request, *args, **kwargs):
    return render(request, 'result.html', {})

def footer_view(request, *args, **kwargs):
    return render(request, 'footer.html', {})


def header_view(request, *args, **kwargs):
    return render(request, 'header.html', {})


def get_predictions(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    with open('model_pickle.pickle', 'rb') as f:
        mp = pickle.load(f)
    # patient1 = mp.predict([[39, 0, 1, 135, 208, 0, 0, 171, 0, 1.5, 2, 0, 2]])
    # print(patient1[0])
    prediction = mp.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    if prediction[0] == 0:
        return 'no'
    elif prediction[0] == 1:
        return 'yes'
    else:
        return 'error'


def prediction_page_view(request, *args, **kwargs):
    try:
        my_form = UserInfoForm()
        if request.method == 'POST':
            my_form = UserInfoForm(request.POST)
            values = request.POST
            age = int(request.POST['age'])
            sex = int(request.POST['sex'])
            cp = int(request.POST['cp'])
            trestbps = int(request.POST['trestbps'])
            chol = int(request.POST['chol'])
            fbs = int(request.POST['fbs'])
            restecg = int(request.POST['restecg'])
            thalach = int(request.POST['thalach'])
            exang = int(request.POST['exang'])
            oldpeak = float(request.POST['oldpeak'])
            slope = int(request.POST['slope'])
            ca = int(request.POST['ca'])
            thal = int(request.POST['thal'])

        result = get_predictions(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
        print("result=", result)
        context = {
            'obj': result,
            'object': values
        }
        return render(request, 'prediction.html', context)
    except:
        context = {
            'message' : "Try again"
        }
        return redirect("/", context)

def user_heart_info_save_display_view(request, *args, **kwargs):
    user = request.GET.get('user')
    context = {'user': user}
    return render(request, 'user_heart_info_save_display.html', context)