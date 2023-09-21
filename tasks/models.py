from django.db import models

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ('NS', 'Not Started'),
        ('IP', 'In Progress'),
        ('C', 'Completed'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='NS',
    )
    due_date = models.DateField()


    def __str__(self):
        return self.title
