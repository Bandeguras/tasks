# Generated by Django 4.1.3 on 2022-11-10 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_task_description_alter_task_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completion_at',
            field=models.DateField(blank=True, max_length=30, null=True, verbose_name='Дата выполнения'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(blank=True, max_length=3000, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')], default='new', max_length=30, verbose_name='СТАТУС'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.TextField(max_length=30, verbose_name='Название'),
        ),
    ]
