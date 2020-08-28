from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .form import *
from fullstack.serializer import  imageSerializer
import json
import requests

# Create your views here.
def index(request):
    return render(request,'cctech.html')

# def fetch(request):

def submitUser(request):
    img = request.GET['img']
    

    url = "http://127.0.0.1:8000/admin/fullstack/image/"

    payload = { "img":img}
    payload = json.dumps(payload)
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    data = response.text
