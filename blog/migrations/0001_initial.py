# Generated by Django 4.1.5 on 2023-01-26 12:19

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250, verbose_name="Заголовок")),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False, populate_from="title", verbose_name="Слуг"
                    ),
                ),
                ("content", models.TextField(verbose_name="Содержание")),
                (
                    "preview",
                    models.ImageField(
                        blank=True, null=True, upload_to="image/", verbose_name="Превью"
                    ),
                ),
                (
                    "created_date",
                    models.DateField(auto_now_add=True, verbose_name="Дата создания"),
                ),
                (
                    "published",
                    models.BooleanField(default=False, verbose_name="Опубликовано"),
                ),
                (
                    "views_cntr",
                    models.IntegerField(default=0, verbose_name="Кол-во просмотров"),
                ),
            ],
            options={"verbose_name": "Запись", "verbose_name_plural": "Записи",},
        ),
    ]
