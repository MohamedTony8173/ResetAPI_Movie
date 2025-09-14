from django.db import models

class Ticket(models.Model):
    date = models.DateField()
    time = models.TimeField()
    seat = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE,related_name='tickets')
    guest = models.ForeignKey('Guest', on_delete=models.CASCADE,related_name='tickets')

    def __str__(self):
        return f"{self.movie.title} - {self.date} - {self.time} - {self.seat} - {self.price} - {self.guest.name} "

class Guest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    genre = models.CharField(max_length=50)
    release_date = models.DateField()


    def __str__(self):
        return self.title