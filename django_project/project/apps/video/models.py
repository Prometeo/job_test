from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            null=False, blank=False)

    class Meta:
        db_table = 'categories'
        ordering = ['name']


class Course(models.Model):
    title = models.CharField(max_length=120, blank=False, null=False)
    category = models.ForeignKey(
        Category, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'courses'
        ordering = ['title']


class Registration(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'regsitrations'


class VideoProgress(models.Model):
    dialy_minutes = models.PositiveSmallIntegerField()
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    day = models.DateField()

    class Meta:
        db_table = 'video_progress'
        indexes = [
            models.Index(fields=['user']),
        ]
