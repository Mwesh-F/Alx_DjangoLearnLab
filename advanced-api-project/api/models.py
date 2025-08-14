
"""
Models for the API app.

Author: Represents a book author with a name.
Book: Represents a book with a title, publication year, and a foreign key to Author.
The relationship is one-to-many: one Author can have many Books.
"""
from django.db import models

class Author(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Book(models.Model):
	title = models.CharField(max_length=255)
	publication_year = models.IntegerField()
	author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.title} ({self.publication_year})"
