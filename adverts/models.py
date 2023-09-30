from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Advert(models.Model):
    ADVERT_TYPES = (
        ('RE', 'Rent'),
        ('SE', 'Sell'),
    )
    type = models.CharField(max_length=2, choices=ADVERT_TYPES)
    title = models.CharField(max_length=200, default='Заголовок')

    def __str__(self):
        return self.title

    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number_of_rooms = models.PositiveSmallIntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    price = models.DecimalField(max_digits=12, decimal_places=2)
    area = models.DecimalField(max_digits=5, decimal_places=2)
    thumbnail = models.ImageField(null=True, blank=True)


