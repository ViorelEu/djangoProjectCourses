# Generated by Django 4.2.5 on 2023-09-21 17:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0003_course_subscriptions"),
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="courses",
            field=models.ManyToManyField(related_name="orders", to="courses.course"),
        ),
        migrations.AddField(
            model_name="order",
            name="order_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="order",
            name="total_price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.DeleteModel(
            name="OrderItem",
        ),
    ]
