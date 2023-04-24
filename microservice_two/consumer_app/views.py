from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from kafka import KafkaProducer
# Create your views here.
class Handshake_MicroserviceOne_View(APIView):
    def post(self,request):
        data=request.data
        print(data)
        b_data=bytes(data,encoding='utf-8')
        produce=KafkaProducer(bootstrap_servers='localhost:9092')
        produce.send('topicOne',key=None,value=b_data)
        produce.flush()
        return Response('Done')
    
class GreetingsView(APIView):
    def get(self,request):
        return Response('Greetings,welcome to Microservice Two')