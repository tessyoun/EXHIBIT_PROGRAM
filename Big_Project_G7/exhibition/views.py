from django.shortcuts import render, redirect
from .models import exbooth_1st, exbooth_2nd, exbooth_3rd, exbooth_4th
from django.contrib.auth.decorators import login_required
from .models import Exhibition
from .forms import ExhibitionForm
from accounts.models import Profile
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse, HttpResponse
import json
import requests
import base64

AI_API_URL = 'https://8rgyr184rzf1v9-8080.proxy.runpod.net/generate'

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
def create_exhibition(request):
    if request.method == 'POST':
        form = ExhibitionForm(request.POST)
        if form.is_valid():
            exhibition = form.save(commit=False)
            exhibition.host_id = request.user.profile.name  # 로그인한 사용자의 아이디를 설정
            exhibition.save()
            api_data = create_json(form)
            try:
                response = requests.post(
                    AI_API_URL,
                    data = api_data,
                    headers={'Content-type':'application/json'},
                    timeout=200
                )
                response.raise_for_status()
                if response.status_code == 200:
                    image = base64.b64encode(response.content).decode('utf-8')
                    return render(request, 'layout2.html', {'image_url': image})

                image_response = requests.get(AI_API_URL)
                image_data = image_response.json().get('image')
                # image_url = AI_API_URL
                # return render(request, 'layout2.html', {'image_url': image_url})
                return render(request, 'layout2.html', {'image_url' : image_data})
            except requests.exceptions.RequestException as E:
                return JsonResponse({'error': str(E)}, status=500)
            
            # print(response.headers)
            # return redirect('create_exhibition')
        else:
            print(form.errors) # 폼에러 확인
    else:
        form = ExhibitionForm()
    return render(request, 'layout2.html', {'form': form})

def change_perm(request):
    if request.method == 'POST':
        user = request.user
        user.is_staff = True
        user.save()
        return redirect('create_exhibition')
    
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
