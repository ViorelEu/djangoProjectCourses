# Generated by Django 4.2.5 on 2023-09-14 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Trainer",
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
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("course", models.CharField(max_length=40)),
                ("email", models.EmailField(max_length=40)),
                (
                    "department",
                    models.CharField(
                        choices=[
                            ("Backend", "backend"),
                            ("Frontend", "frontend"),
                            ("Network", "networtk"),
                        ],
                        max_length=8,
                        null=True,
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                ("profile", models.ImageField(null=True, upload_to="profile/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
