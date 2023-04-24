from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from kafka import KafkaProducer
# Create your views here.

class Handshake_MicroserviceTwo_View(APIView):
    def post(self,request):
        data=request.data
        print(data)
        b_data=bytes(data,encoding='utf-8')
        produce=KafkaProducer(bootstrap_servers='localhost:9092')
        produce.send('topicTwo',key=None,value=b_data)
        produce.flush()
        return Response('Done')