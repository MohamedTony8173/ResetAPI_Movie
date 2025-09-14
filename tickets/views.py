from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import GuestSerializer, ModelSerializer, TicketSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


from tickets.models import Guest


class GuestViewSerializer(APIView):
    def get(self, request):
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.date,status=status.HTTP_400_BAD_REQUEST)
        

class GuestUpdateDeleteView(APIView):
    
    def get_object(self,pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    
    def put(self,request,pk):
        guest = Guest.objects.get(pk=pk)    
        serializer = GuestSerializer(guest,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        guest = Guest.objects.get(pk=pk)  
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    