from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Professor

class ProfessorSearchView(APIView):
    def get(self, request):
        domain = request.GET.get('domain', '')
        profs = Professor.objects.filter(domain__icontains=domain)
        data = [{"name": p.name, "webpage": p.webpage, "department": p.department} for p in profs]
        return Response(data)
