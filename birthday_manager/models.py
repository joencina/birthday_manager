from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.name}: {self.birthday.month}/{self.birthday.day}"
