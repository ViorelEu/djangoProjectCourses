# Generated by Django 4.2.5 on 2023-09-14 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("instructor", models.CharField(max_length=50)),
                ("start_date", models.DateField()),
                ("active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(default="2023-12-12")),
                ("duration_in_weeks", models.PositiveIntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
