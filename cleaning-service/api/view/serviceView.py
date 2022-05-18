from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import Service
from api.serializers import ServiceSerializer


class ServiceAPIView(APIView):
    def get(self, request):
        s = Service.objects.all()
        return Response({'posts': ServiceSerializer(s, many=True).data})


    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({'post': serializer.data})

    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT is not allowed"})

        try:
            instance = Service.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serializer = ServiceSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE is not allowed"})

        try:
            instance = Service.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({"error": "Object does not exist"})

        return Response({"post": "delete post " + str(pk)})