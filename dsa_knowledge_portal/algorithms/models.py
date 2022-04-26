from unittest.util import _MAX_LENGTH
from django.db import models

class AlgorithmType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.type}'

class Algorithms(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    time_complexity = models.CharField(max_length=100, default='O(n)')
    space_complexity = models.CharField(max_length=100, default='O(1)')
    algorithm_type = models.ForeignKey(AlgorithmType, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.name}'

