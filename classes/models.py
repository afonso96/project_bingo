from django.db import models



class Training(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class MatchTraining(models.Model):
    study = models.ForeignKey("person.Study", on_delete=models.CASCADE )
    training = models.ManyToManyField(Training)
    status = models.BooleanField(default=False)
