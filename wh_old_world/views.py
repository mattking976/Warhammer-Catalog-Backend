from rest_framework.views import APIView
from rest_framework.response import Response
from .models import OldWorld
from .models import OldWorldFactions
from .serializer import OldWorldSerializer
from .serializer import OldWorldFactionsSerializer

class OldWorldView(APIView):
    serializer = OldWorldSerializer

    def get(self, request, faction_id):
        old_worlds = OldWorld.objects.filter(faction_id=faction_id)
        serializer = self.serializer(old_worlds, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class OldWorldFactionsView(APIView):
    serializer = OldWorldFactionsSerializer

    def get(self, request):
        old_world_factions = OldWorldFactions.objects.all()
        serializer = self.serializer(old_world_factions, many=True)
        return Response(serializer.data)
