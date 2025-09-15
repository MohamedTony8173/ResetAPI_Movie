from rest_framework.serializers import ModelSerializer
from .models import Ticket, Guest, Movie

class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields ='__all__'
        read_only_fields = ['id']

class GuestSerializer(ModelSerializer):
    class Meta:
        model = Guest
        fields = ('name', 'email', 'phone','tickets')
        read_only_fields = ['id']

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'description', 'duration', 'genre', 'release_date','tickets')
        read_only_fields = ['id']
        