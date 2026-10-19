from django.contrib import admin
from .models import About, SocialLink

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    count = About.objects.all().count()
    if count == 0:
      return True
    return False
# admin.site.register(About) ##-- this is not helping in enforcing only one about

admin.site.register(SocialLink)