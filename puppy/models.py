from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator


class VisitorsModel(models.Model):
    """Модель постоянных посетителей"""
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    comments = models.TextField()
    image = models.FileField(upload_to='gallery')

    def get_url(self):
        """Функция возращает url объекта (в данном случае обращение по id)"""
        return reverse("about_page", args=[self.id])


class OurTeamModel(models.Model):
    """Модель членов команды ветклиники"""
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    image = models.FileField(upload_to='gallery')

    def get_url(self):
        """Функция возращает url объекта (в данном случае обращение по id)"""
        return reverse("about_page", args=[self.id])


class PetsModel(models.Model):
    NEED_HELP = 'N'
    ON_THERAPY = 'T'
    HEALTHY = 'H'
    """Статус здоровья питомца"""
    STATUS_PET = [
        (NEED_HELP, 'Need help'),
        (ON_THERAPY, 'Now on therapy'),
        (HEALTHY, 'Healthy'),
    ]
    BOY = 'B'
    GIRL = 'G'
    """Гендерная принадлежности питомца"""
    GENDER_PET = [
        (BOY, 'boy'),
        (GIRL, 'girl'),
    ]
    """Модель питомцев доставленных в приют"""
    name = models.CharField(max_length=50)
    age_old_years = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1)])
    age_old_months = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1)])
    age_old_days = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1)])
    image = models.FileField(upload_to='gallery')
    species = models.CharField(max_length=40)
    gender = models.CharField(max_length=1, choices=GENDER_PET, default=BOY)
    status = models.CharField(max_length=1, choices=STATUS_PET, default=HEALTHY)

    def get_url(self):
        """Функция возращает url объекта (в данном случае обращение по id)"""
        return reverse("about_page", args=[self.id])

    def save(self, *args, **kwargs):
        """Функция преобразует имя питомца в slug-поле"""
        self.slug = slugify(self.name)
        super(PetsModel, self).save(*args, **kwargs)


class GetInTouchModel(models.Model):
    """Модель для обращения в ветклинику"""
    message = models.TextField(max_length=300, validators=[MinLengthValidator(1)])
    name = models.CharField(max_length=50, validators=[MinLengthValidator(1)])
    email = models.EmailField(max_length=80, validators=[MinLengthValidator(1)])
    subject = models.CharField(max_length=100, validators=[MinLengthValidator(1)])

    def get_url(self):
        """Функция возращает url объекта (в данном случае обращение по id)"""
        return reverse("contact_page", args=[self.id])


