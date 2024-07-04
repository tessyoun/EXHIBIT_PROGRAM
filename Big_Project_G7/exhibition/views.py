from django.shortcuts import render, redirect
from .models import exbooth_1st, exbooth_2nd, exbooth_3rd, exbooth_4th
from django.contrib.auth.decorators import login_required
from .models import Exhibition
from .forms import ExhibitionForm
from accounts.models import Profile
from .forms import Exbooth1stForm, Exbooth2ndForm, Exbooth3rdForm, Exbooth4thForm
from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse, HttpResponse
import json
import requests
import base64

PORT = 5000
# AI_API_URL = 'https://8rgyr184rzf1v9-' + str(PORT) + '.proxy.runpod.net/generate/once'
AI_API_URL = 'https://8rgyr184rzf1v9-' + str(PORT) + '.proxy.runpod.net/generate'

def getExhidb(exhi):
    exhibition = exhi.objects.all() # 1전시
    # exhi_2nd = exbooth_2nd.objects.all() # 2전시
    # exhi_3rd = exbooth_3rd.objects.all() # 3전시
    # exhi_4th = exbooth_4th.objects.all() # 4전시
    return exhibition

exhi_1st = getExhidb(exbooth_1st)
exhi_2st = getExhidb(exbooth_2nd)
exhi_3rd = getExhidb(exbooth_3rd)
exhi_4th = getExhidb(exbooth_4th)

@login_required
def change_perm(request):
    if request.method == 'POST':
        user = request.user
        user.is_staff = True
        user.save()
        request.session['data'] = {}
        return redirect('create_exhibition')
    
@login_required
def create_exhibition(request):
    if request.method == 'POST':
        form = ExhibitionForm(request.POST)
        if form.is_valid():
            exhibition = form.save(commit=False)
            exhibition.host_id = request.user.profile.name  # 로그인한 사용자의 아이디를 설정
            exhibition.save()
            request.session['data'] = create_json(form)
        elif not request.session['data']:
            print(form.errors) # 폼에러 확인

        response, images = get_image_from_server(request.session['data'])
        if response.status_code == 200:
            return render(request, 'layout2.html', {'image_url': images})
        else:
            return response
    else:
        form = ExhibitionForm()
    return render(request, 'layout2.html', {'form': form})

def get_image_from_server(data:json):
    try:
        response = requests.post(
            AI_API_URL,
            data = data,
            headers={'Content-type':'application/json'},
            timeout=200
        )

        if response.status_code == 200:
            images = response.json()
            return response, images
        else:
            return JsonResponse({'Image generation failed'}, status=500), None
    
    except requests.exceptions.RequestException as E:
        return JsonResponse({'error': str(E)}, status=500), None

def create_json(form):
    form_data = {
        'exhibition_name': form.cleaned_data['exhibition_name'] ,
        'hall': form.cleaned_data['hall'] ,
        'start_date':form.cleaned_data['start_date'] ,
        'end_date': form.cleaned_data['end_date'] ,
        'number_of_booths': form.cleaned_data['number_of_booths'] ,
    }
    json_data = json.dumps(form_data, cls=DjangoJSONEncoder, ensure_ascii = False)
    return json_data

@login_required
def update_booths(request):
    user_name = request.user.profile.name  # Assuming 'Profile' model has a 'name' field and is related to User

    booths_1st = exbooth_1st.objects.filter(group=user_name).first()
    booths_2nd = exbooth_2nd.objects.filter(group=user_name).first()
    booths_3rd = exbooth_3rd.objects.filter(group=user_name).first()
    booths_4th = exbooth_4th.objects.filter(group=user_name).first()

    if request.method == 'POST':
        form1 = Exbooth1stForm(request.POST, instance=booths_1st)
        form2 = Exbooth2ndForm(request.POST, instance=booths_2nd)
        form3 = Exbooth3rdForm(request.POST, instance=booths_3rd)
        form4 = Exbooth4thForm(request.POST, instance=booths_4th)

        if form1.is_valid() and booths_1st:
            form1.save()
        if form2.is_valid() and booths_2nd:
            form2.save()
        if form3.is_valid() and booths_3rd:
            form3.save()
        if form4.is_valid() and booths_4th:
            form4.save()

        messages.success(request, '부스 정보가 업데이트되었습니다.')
        return redirect('index')

    else:
        form1 = Exbooth1stForm(instance=booths_1st) if booths_1st else None
        form2 = Exbooth2ndForm(instance=booths_2nd) if booths_2nd else None
        form3 = Exbooth3rdForm(instance=booths_3rd) if booths_3rd else None
        form4 = Exbooth4thForm(instance=booths_4th) if booths_4th else None

    return render(request, 'boothinfo.html', {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
    })
