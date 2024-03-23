from django.shortcuts import render
from django.template import loader
# from django import Response
from rest_framework.response import Response
from rest_framework import viewsets

# Create your views here.
def index(request):
    print('here')
    return render(request, 'base.html', {})

fake_data = [
    {
        "name": 'Host 1'
    },
    {
        "name": 'Host 2'
    },
    {
        "name": 'Host 3'
    },
    {
        "name": 'Host 4'
    }
]
metrics_port = 9100

class HostViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response(fake_data)

class TargetsViewSet(viewsets.ViewSet):
    def list(self, request):
        host_groups = [
            {
                'targets': [f'{h["name"]}:{metrics_port}' for h in fake_data],
                'labels': []
            }
        ]

        return Response(host_groups)
