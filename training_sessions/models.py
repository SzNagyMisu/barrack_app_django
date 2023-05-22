from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    class Gender(models.IntegerChoices):
        MALE = 0
        FEMALE = 1

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.IntegerField(choices=Gender.choices)
    height_in_cm = models.IntegerField()
    weigt_in_kg = models.IntegerField()
    phone = models.CharField(max_length=15)
    motivation = models.TextField()


class Balance(models.Model):
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_text = models.TextField()
    commentable_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    commentable_id = models.PositiveIntegerField()
    commentable = GenericForeignKey("commentable_type", "commentable_id")

    class Meta:
        indexes = [
            models.Index(fields=("commentable_type", "commentable_id"))
        ]


class Trainer(models.Model):
    name = models.CharField(max_length=255)


class TrainingSession(models.Model):
    code = models.CharField(max_length=6)
    start_time = models.DateTimeField()
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
