from datetime import datetime
import hashlib
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from django.conf import settings


"""Clase para listar Comics"""
class Comics(APIView):
    
    """generador de hash en base a la hora actual"""
    def HashGenerator(self):

        str2hash = str(datetime.timestamp(datetime.now())) + settings.PRIVATE_KEY + settings.PUBLIC_KEY
        result = hashlib.md5(str2hash.encode('utf-8'))
        return result.hexdigest()

    def get(self, request):

        params = {
            'apikey': settings.PUBLIC_KEY,
            'hash': self.HashGenerator(),
            'ts': datetime.timestamp(datetime.now())
        }
        response = requests.get(
            url='https://gateway.marvel.com:443/v1/public/comics',
            params=params
        )
        json = response.json()
        result = [{
            'titulo': i['title'],
            'imagen': i['images'],
            'creadores': i['creators'],
            'series': i['series'],
            'fecha_creacion': i['dates']} for i in json['data']['results']]
        result = sorted(result, key=lambda comic : comic['titulo'])

        return Response(result, status=status.HTTP_200_OK)
