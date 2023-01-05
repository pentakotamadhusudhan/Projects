from rest_framework import generics
from .serialzers import *
from rest_framework.response import Response


class timeview(generics.GenericAPIView):
    serializer_class = TimeSerializer

    def post(self, request, *args, **kwargs):
        a = TimeSerializer(data=request.data)
        a.is_valid(raise_exception=True)
        user = a.save()
        return Response(TimeSerializer(user).data)