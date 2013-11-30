from django.db import models

# Create your models here.

class DatedModel(models.Model):
  birth_date = models.DateTimeField(auto_now_add=True)
  mod_date = models.DateTimeField(auto_now=True)

class Project(DatedModel):
  name = models.CharField(max_length=5000)
  slug = models.SlugField()
  description = models.TextField(blank=True,null=True)
  category = models.CharField(blank=True, null=True, max_length=250)

  def __unicode__(self):
    return self.name
  
class Note(DatedModel):
  project = models.ForeignKey(Project)
  content = models.TextField()

class Media(DatedModel):
  project = models.ForeignKey(Project)
  image = models.ImageField(upload_to="images")
  description = models.TextField(blank=True,null=True)

