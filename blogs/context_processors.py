
from .models import Category
from assignment.models import SocialLink
def get_categories(request):
  categories = Category.objects.all()
  return dict(categories = categories)

def get_social_link(requst):
  social_links = SocialLink.objects.all()
  return dict(social_links = social_links)