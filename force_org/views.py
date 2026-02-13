from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ForceOrg
from .serializer import ForceOrgSerializer

class ForceOrgView(APIView):
    serializer = ForceOrgSerializer

    def get(self, request):
        force_orgs = ForceOrg.objects.all()
        serializer = self.serializer(force_orgs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

