from rest_framework.serializers import ModelSerializer
from .models import Ticket, Guest, Movie

class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ['id']

class GuestSerializer(ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'
        read_only_fields = ['id']

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ['id']
        