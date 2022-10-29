from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import InternSerializer

from .models import Intern


@api_view(['GET'])
def endpoints(request):
    data = ['/interns']
    return Response(data)


class InternList(APIView):

    def get(self, request):

        data = {'slackUsername': 'String','backend': 'Boolean','age':'28','bio':'String'}
        return Response(data)
