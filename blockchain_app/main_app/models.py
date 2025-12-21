from django.db import models
from django.utils.text import slugify
from cyrtranslit import to_latin

# Create your models here.

class LessonModel(models.Model):
    title = models.CharField(blank=False, null=False, max_length=50)
    body = models.TextField()
    slug = models.SlugField(blank=True, editable=False)
    image = models.CharField(blank=True, null=True, default='placeholder.png')
    
    class Meta:
        verbose_name = 'Lesson'
        
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(to_latin(self.title, 'ru'))
        super().save(*args, **kwargs)

class StepModel(models.Model):
    title = models.CharField(blank=False, null=False, max_length=50)
    body = models.TextField()
    image = models.CharField(blank=True, null=True, max_length=255)
    script = models.CharField(blank=True, null=True, max_length=255)
    lesson = models.ForeignKey(LessonModel, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(blank=True, editable=False)
    index = models.IntegerField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Step'

    def __str__(self):
        return self.title + '(' + self.lesson.title + ')'
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(to_latin(self.title, 'ru'))
        
        if self.title == 'start':
            self.index = 1
        super().save(*args, **kwargs)
    
