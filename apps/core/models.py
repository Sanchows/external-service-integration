from django.db import models


class APIEndpoint(models.Model):
    url = models.URLField(
        verbose_name="Полный путь до эндпоинта",
        primary_key=True)
    title = models.CharField("Имя эндпоинта", max_length=50)

    def __str__(self):
        return f"{self.title} {self.url}"


class Authorization(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    endpoint = models.OneToOneField(
        APIEndpoint,
        on_delete=models.CASCADE,
        related_name="authorization",
        blank=True,
        null=True
        )

    def __str__(self):
        return f"{self.endpoint}"


class Parameter(models.Model):
    name = models.CharField(verbose_name="Параметр", max_length=50)
    value = models.CharField(verbose_name="Значение", max_length=300)
    endpoint = models.ForeignKey(APIEndpoint, on_delete=models.CASCADE, related_name="parameters")

    def __str__(self):
        return f"{self.name}={self.value} || ({self.endpoint})"
