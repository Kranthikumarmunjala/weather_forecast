from django.db import models

# Create your models here.


class State(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return str(self.name)

class District(models.Model):
    TYPE=[
        ('heavy','heavy'),
        ('moderate','moderate'),
        ('low','low')
    ]
    state=models.ForeignKey(State,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    rainfall_type=models.CharField(max_length=255, null=True,blank=True,choices=TYPE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)