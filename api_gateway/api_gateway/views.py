from django.shortcuts import redirect
from rest_framework.views import APIView

class MicroserviceOneView(APIView):
    def get(self,request):
        #Access microservice one on port 8002
        return redirect('http://127.0.0.1:8002/greetings/')

class MicroserviceTwoView(APIView):
    def get(self,request):
        #Access microservice two on port 8003
        return redirect('http://127.0.0.1:8003/greetings/')