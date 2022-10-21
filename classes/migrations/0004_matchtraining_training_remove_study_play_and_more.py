# Generated by Django 4.1.2 on 2022-10-21 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("person", "0001_initial"),
        ("classes", "0003_classes_alter_study_play_delete_teacher"),
    ]

    operations = [
        migrations.CreateModel(
            name="MatchTraining",
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
                ("status", models.BooleanField(default=False)),
                (
                    "study",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="person.study"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Training",
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
                ("name", models.CharField(max_length=255)),
                ("date", models.DateField()),
                ("description", models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name="study",
            name="play",
        ),
        migrations.DeleteModel(
            name="Classes",
        ),
        migrations.DeleteModel(
            name="Study",
        ),
        migrations.AddField(
            model_name="matchtraining",
            name="training",
            field=models.ManyToManyField(to="classes.training"),
        ),
    ]
