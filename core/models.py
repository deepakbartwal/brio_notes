from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_noop

# Create your models here.

class Category(models.Model):
    CAT_CHOICES = (
        ('undergraduate', ugettext_noop('Undergraduate')),
        ('graduate', ugettext_noop('Graduate')),
        ('post_graduate', ugettext_noop('Postgraduate'))
    )
    category = models.CharField(
        blank=True, null=True, max_length=32, db_index=True, choices=CAT_CHOICES
    )
    cat_type = models.CharField(max_length=255, db_index=True)
    stream = models.CharField(blank=True, null=True, max_length=8, db_index=True)
    degree_name = models.CharField(max_length=255, db_index=True)

class Notes(models.Model):
    category = models.ForeignKey(Category, db_index=True)
    title = models.CharField(max_length=255, db_index=True)
    file = models.FileField(upload_to='notes')

class QuestionPaper(models.Model):
    category = models.ForeignKey(Category, db_index=True)
    title = models.CharField(max_length=255, db_index=True)
    file = models.FileField(upload_to='question_papers')
    is_solved = models.BooleanField(default=False)