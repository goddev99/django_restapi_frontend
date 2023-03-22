from django.core import validators
from django.db import models


class Project(models.Model):
    key = models.CharField(max_length=32, unique=True, validators=(
        validators.RegexValidator(
            regex=r"^[a-z0-9_]*$", message='Allowed characters: "a-z", "0-9", "_"'
        ),
    ), )
    name = models.CharField(max_length=512, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
