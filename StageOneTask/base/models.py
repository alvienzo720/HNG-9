from django.db import models

class Intern(models.Model):
    slackUsername = models.CharField(max_length=200, null=True)
    backend = models.BooleanField(null=True)
    age = models.IntegerField(null=True)
    bio = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.slackUsername