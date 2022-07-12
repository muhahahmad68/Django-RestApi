from django.db import models

# Create your models here.


class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    date_enrolled = models.DateTimeField(auto_now=True)

    class Meta:
         verbose_name_plural = 'Students'

    def __str__(self):
        return self.name
