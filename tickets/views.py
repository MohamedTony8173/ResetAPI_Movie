from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import GuestSerializer, MovieSerializer, TicketSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.generics import mixins, GenericAPIView
from rest_framework import generics
from rest_framework.decorators import api_view


from tickets.models import Guest, Ticket, Movie


class GuestViewSerializer(APIView):
    def get(self, request):
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.date, status=status.HTTP_400_BAD_REQUEST)


class GuestUpdateDeleteView(APIView):

    def get_object(self, pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest)
        return Response(serializer.data)

    def put(self, request, pk):
        guest = Guest.objects.get(pk=pk)
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        guest = Guest.objects.get(pk=pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MixinTicketsList(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class MixinTicketUpdateDelete(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get(self, request, pk):
        return self.retrieve(request)

    def put(self, request, pk):
        return self.update(request)

    def delete(self, request, pk):
        return self.destroy(request)


class GenericMovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class GenericMovieUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


@api_view(['GET'])
def find_movie(request):
    movies = Movie.objects.filter(
        title = request.data['title'],
        genre = request.data['genre']
    ) 
    serializer = MovieSerializer(movies,many=True)     
    return Response(serializer.data)  

@api_view(['POST'])
def reservationMovie(request):
    movie = Movie.objects.get(
        title = request.data['title'],
    )

    guest = Guest()
    guest.name = request.data['name']
    guest.email = request.data['email']
    guest.phone = request.data['phone']
    guest.save()
    
    ticket = Ticket()
    ticket.date = request.data['date']
    ticket.time = request.data['time']
    ticket.seat = request.data['seat']
    ticket.price = request.data['price']
    ticket.movie = movie
    ticket.guest = guest
    ticket.save()
    return Response(status=status.HTTP_201_CREATED)
    
