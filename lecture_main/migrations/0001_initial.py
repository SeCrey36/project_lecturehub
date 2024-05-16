# Generated by Django 5.0.1 on 2024-02-08 18:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(blank=True, choices=[('ag', 'Алгебра и Геометрия'), ('matan', 'Математический анализ'), ('vvpd', 'ВВПД'), ('com', 'Деловая коммункация'), ('eng', 'Иностранный язык'), ('inf', 'Информатика'), ('his', 'История России'), ('op', 'Основы программирования'), ('pravo', 'Правоведение'), ('proj', 'Проектная деятельность'), ('phys', 'Физика'), ('dmat', 'Дискретная математика')], default='ag', help_text='Предмет (категория)', max_length=5)),
                ('description', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=200)),
                ('likes', models.IntegerField()),
                ('views', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]