from django.db import models
from webapp.validators import MinLengthValidator, prohibited_word
from django.contrib.auth import get_user_model


class Project(models.Model):
    user = models.ManyToManyField(get_user_model(), related_name='projects',
                                    verbose_name='Пользователь', db_table='projects_users', blank=True, null=True)
    start_date = models.DateField(null=False, blank=False,
                                  verbose_name='Дата начала')
    finish_date = models.DateField(null=True, blank=True,
                                   verbose_name='Дата окончания')
    title = models.CharField(max_length=120, null=False, blank=False,
                             verbose_name='Название')
    description = models.TextField(max_length=3000, null=True, blank=True,
                                   verbose_name='Описание')
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        permissions = [
            ('add_or_delete_user', 'Редактировать пользователей')
        ]


class Task(models.Model):
    summary = models.CharField(max_length=120, null=False, blank=False,
                               verbose_name='Краткое описание',
                               validators=[MinLengthValidator(5),
                                           prohibited_word])
    description = models.TextField(max_length=1000, null=True, blank=True,
                                   verbose_name='Полное описание',
                                   validators=[MinLengthValidator(20),
                                               prohibited_word])
    statuses = models.ForeignKey('webapp.Status', related_name='tasks',
                                 on_delete=models.PROTECT,
                                 verbose_name='Статус')
    types = models.ManyToManyField('webapp.Type', related_name='tasks',
                                    verbose_name='Тип', db_table='tasks_types')
    project = models.ForeignKey('webapp.Project', related_name='tasks',
                                on_delete=models.CASCADE, null=False,
                                blank=False, verbose_name='Проект', default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.id}. {self.summary}: {self.statuses}'


class Status(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False,
                            verbose_name='Название')

    class Meta:
        db_table = 'statuses'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return f'{self.name}'


class Type(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False,
                            verbose_name='Название')

    class Meta:
        db_table = 'types'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return f'{self.name}'
