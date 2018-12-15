from django.db import models
from django.core.validators import validate_comma_separated_integer_list


class Lists(models.Model):
    lists = models.CharField(max_length=200)

    def __str__(self):
        return self.lists

class Result(models.Model):
	result= models.CharField(max_length=400)

	def __str__(self):
		return self.result