from django.db import models
class india(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    mobile=models.BigIntegerField()
    def __str__(self):
        return self.name
    

