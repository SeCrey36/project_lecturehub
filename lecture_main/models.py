from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    subjects = (
        ('ag', 'Алгебра и Геометрия'),
        ('matan', 'Математический анализ'),
        ('vvpd', 'ВВПД'),
        ('com', 'Деловая коммункация'),
        ('eng', 'Иностранный язык'),
        ('inf', 'Информатика'),
        ('his', 'История России'),
        ('op', 'Основы программирования'),
        ('pravo', 'Правоведение'),
        ('proj', 'Проектная деятельность'),
        ('phys', 'Физика'),
        ('dmat', 'Дискретная математика')
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=5, choices=subjects, 
                              blank=True, default='ag', help_text='Предмет (категория)')
    description = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    
    