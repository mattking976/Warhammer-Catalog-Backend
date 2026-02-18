from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ForceOrg
from .models import Factions
from .serializer import ForceOrgSerializer
from .serializer import FactionsSerializer

class ForceOrgView(APIView):
    serializer = ForceOrgSerializer

    def get(self, request, faction_id):
        force_orgs = ForceOrg.objects.filter(faction_id=faction_id)
        serializer = self.serializer(force_orgs, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class FactionsView(APIView):
    serializer = FactionsSerializer

    def get(self, request):
        factions = Factions.objects.all()
        serializer = self.serializer(factions, many=True)
        return Response(serializer.data)
