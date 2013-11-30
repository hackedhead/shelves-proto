from django.contrib import admin

from partz.models import Project, Note, Media

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug':('name',)}
  pass
admin.site.register(Project,ProjectAdmin)

class NoteAdmin(admin.ModelAdmin):
  pass
admin.site.register(Note,NoteAdmin)

class MediaAdmin(admin.ModelAdmin):
  pass
admin.site.register(Media,MediaAdmin)

