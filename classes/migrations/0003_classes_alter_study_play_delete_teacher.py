# Generated by Django 4.1.2 on 2022-10-20 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("classes", "0002_study_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Classes",
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
                ("date", models.DateField()),
                ("description", models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name="study",
            name="play",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="classes.classes"
            ),
        ),
        migrations.DeleteModel(
            name="Teacher",
        ),
    ]