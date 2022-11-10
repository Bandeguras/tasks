from django.db import models

# Create your models here.
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]
class Task(models.Model):
    title = models.TextField(max_length=50, null=False, blank=False, verbose_name="Название")
    description = models.CharField(max_length=50, null=True, blank=True, verbose_name="Описание")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], verbose_name="СТАТУС")
    completion_at = models.DateField(max_length=20, null=True, blank=True, verbose_name="Дата выполнения")

