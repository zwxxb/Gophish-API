from django.shortcuts import render
from requests.api import delete
from requests.models import Response
from django.http import JsonResponse, response
from django.views import View
import requests

API_KEY = "9c970ce3eb7aea82695fbb23e69de0ffc19bc0d639a5b575fc5c655b234a2f17"
GOPHISH_URI = "https://127.0.0.1:3333/"

class Reset(View):
    def post(self, request):
        data = request.POST
        response = requests.post(GOPHISH_URI + "api/reset", data=data, headers={"Authorization": API_KEY})
        return render(response.json, 'setting.html')

class SendingProfiles(View):
    def get(self, request, *args, **kwargs):
        response = requests.get(GOPHISH_URI + "api/smtp/"+kwargs['id'], headers={"Authorization": API_KEY})
        print(response.json())
        return render(response.json(), 'Users.html')

    def post(self, request):
        data = request.POST
        response = requests.post(GOPHISH_URI + "/api/smtp/", data=data, headers={"Authorization": API_KEY})
        return render(response.json(), 'Users.html')

    def put(self, request, id):
        data = request.PUT
        response = requests.put(GOPHISH_URI + "/api/smtp/" + id, data=data, headers={"Authorization": API_KEY})
        return render(response.json(), 'Users.html')

    def delete(self, request, id):
        response = requests.delete(GOPHISH_URI + "/api/smtp/" + id, headers={"Authorization": API_KEY})
        return render(response.json(), 'Users.html')

class Templates(View):
    def get(self, request):
        response = requests.get(GOPHISH_URI + "api/template/", headers={"Authorization": API_KEY})
        return render(response.json(), 'Templates.html')
    def get(self, request, id):
        response = requests.get(GOPHISH_URI + "api/template/" + id, headers={"Authorization": API_KEY})
        return render(response.json(), 'Templates.html')
    def post(self, request):
        data = request.POST
        response = requests.post(GOPHISH_URI + "/api/template/", data=data, headers={"Authorization": API_KEY})
        return render(response.json(), 'Templates.html')
    def post(self, request, id):
        data = request.POST
        response = requests.post(GOPHISH_URI + "/api/template/" + id, data=data, headers={"Authorization": API_KEY})
        return render(response.json(), 'Templates.html')
    def put(self, request, id):
        data = request.PUT
        response = requests.put(GOPHISH_URI + "/api/template/" + id, data=data, headers={"Authorization": API_KEY})
        return render(response.json(), 'Templates.html')
    def delete(self, request, id):
        response = requests.delete(GOPHISH_URI + "/api/template/" + id, headers={"Authorization": API_KEY})
        return render(response.json(), 'Templates.html')

class Pages(View):
    def get(self, request):
        response = requests.get(GOPHISH_URI + "api/pages/", headers={"Authorization": API_KEY})
        return render(response.json(), 'Pages.html')
    def get(self, request, id):
        response = requests.get(GOPHISH_URI + "api/pages/" + id, headers={"Authorization": API_KEY})
        return render(response.json(), 'Pages.html')
    def post(self, request):
        data = request.POST
        response = requests.post(GOPHISH_URI + "/api/pages/", data=data, headers={"Authorization": API_KEY})
        render(response.json(), 'Pages.html')
    def put(self, request, id):
        data = request.PUT
        response = requests.put(GOPHISH_URI + "/api/pages/" + id, data=data, headers={"Authorization": API_KEY})
        return render(response.json(), 'Pages.html')
    def delete(self, request, id):
        response = requests.delete(GOPHISH_URI + "/api/pages/" + id, headers={"Authorization": API_KEY})
        return render(response.json(), 'Pages.html')

class Groups(View):
    def get(self, request):
        response = requests.get(GOPHISH_URI + "api/group/", headers={"Authorization": API_KEY})
        return render(response.json(), 'Groups.html')
    def get(self, request, id):
        response = requests.get(GOPHISH_URI + "api/group/" + id, headers={"Authorization": API_KEY})
        return render(response.json(), 'Groups.html')
    def get(self, request):
        response = requests.get(GOPHISH_URI + "api/group/summary", headers={"Authorization": API_KEY})
        return render(response.json(), 'Groups.html')
    def get(self, request, id):
        response = requests.get(GOPHISH_URI + "api/group/" + id + "summary", headers={"Authorization": API_KEY})
        return render(response.json(), 'Groups.html')
    def post(self, request):
        data = request.POST
        response = requests.post(GOPHISH_URI + "/api/group/", data=data, headers={"Authorization": API_KEY})
        return render(response.json(), 'Groups.html')
    def put(self, request, id):
        data = request.PUT
        response = requests.put(GOPHISH_URI + "/api/group/" + id, data=data, headers={"Authorization": API_KEY})
        return render(response.json(), 'Groups.html')
    def delete(self, request, id):
        response = requests.delete(GOPHISH_URI + "/api/group/" + id, headers={"Authorization": API_KEY})
        return render(response.json(), 'Groups.html')

class Campaigns(View):
    def get(self, request):
        response = requests.get(GOPHISH_URI + "api/campaigns/", headers={"Authorization": API_KEY})
        return render(response.json(), 'Campaigns.html')

    def get(self, request, id):
        response = requests.get(GOPHISH_URI + "api/campaigns/" + str(id), headers={"Authorization": API_KEY})
        return render(response.json(), 'Campaigns.html')

    def post(self, request):
        data = request.POST
        response = requests.post(GOPHISH_URI + "/api/campaigns/", data=data, headers={"Authorization": API_KEY})
        return render(response.json(), 'Campaigns.html')
    def post(self, request, id):
        data = request.POST
        response = requests.post(GOPHISH_URI + "/api/campaigns/" + id + "/results", data=data, headers={"Authorization": API_KEY})
        return render(response.json(), 'Campaigns.html')
    def post(self, request, id):
        data = request.POST
        response = requests.post(GOPHISH_URI + "/api/campaigns/" + id + "/summary", data=data, headers={"Authorization": API_KEY})
        return render(response.json(), 'Campaigns.html')
    def get(self, request, id):
        response = requests.get(GOPHISH_URI + "api/campaigns/" + id + "/results", headers={"Authorization": API_KEY})
        return render(response.json(), 'Campaigns.html')
    def delete(self, request, id):
        response = requests.delete(GOPHISH_URI + "/api/campaigns/" + id, headers={"Authorization": API_KEY})
        return render(response.json(), 'Campaigns.html')

class Users(View):
    def get(self, request):
        response = requests.get(GOPHISH_URI + "api/user/", headers={"Authorization": API_KEY})
        return render(response.json(), 'Users.html')
    def get(self, request, id):
        response = requests.get(GOPHISH_URI + "api/user/" + id, headers={"Authorization": API_KEY})
        return render(response.json(), 'Users.html')
    def post(self, request):
        data = request.POST
        response = requests.post(GOPHISH_URI + "/api/user/", data=data, headers={"Authorization": API_KEY})
        return render(response.json(), 'Users.html')
    def put(self, request, id):
        data = request.PUT
        response = requests.put(GOPHISH_URI + "/api/user/" + id, data=data, headers={"Authorization": API_KEY})
        return render(response.json(), 'Users.html')
    def delete(self, request, id):
        response = requests.delete(GOPHISH_URI + "/api/user/" + id, headers={"Authorization": API_KEY})
        return render(response.json(), 'Users.html')