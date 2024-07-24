from django.shortcuts import render, redirect
import requests


def base(request):
    return render(request, "happy/base.html")

def json_img(request):
    response = requests.get('https://api.thedogapi.com/v1/images/search')
    outer_json = response.json()
    img_json = outer_json[0]

    return render(request, 'happy/base.html', {'img_json':img_json})
