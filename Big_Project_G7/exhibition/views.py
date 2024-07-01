from django.shortcuts import render
from .models import exbooth_1st, exbooth_2nd, exbooth_3rd, exbooth_4th


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