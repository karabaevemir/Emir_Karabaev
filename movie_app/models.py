from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    @property
    def movie_count(self):
        return self.movies.all().count()


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.TextField(max_length=300)
    director = models.ForeignKey(Director, on_delete=models.SET_DEFAULT, default='Неизвестно', related_name='movies')

    def rating(self):
        count = self.reviews.all().count()
        stars = sum([i.stars for i in self.reviews.all()])
        return stars // count

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(max_length=500)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(default=5, choices=((1, 'Bad (1)'), (2, 'So so (2)'), (3, 'Good (3)'), (4, 'Nice (4)'),
                                                    (5, 'Great (5)')))
