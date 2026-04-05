from django.db import models
from django.conf import settings

class Transaction(models.Model):
    Type_choices=[
        ('income','Income'),
        ('expense','Expense'),
    ]

    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    amount=models.FloatField()
    type=models.CharField(max_length=10,choices=Type_choices)
    category=models.CharField(max_length=50)
    date=models.DateField()
    description=models.TextField(blank=True)

    def __str__(self):
        return f"{self.type} - {self.amount}"
