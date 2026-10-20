
from django.http import HttpResponse
from django.shortcuts import redirect,render
from blogs.models import Blog,Category
from assignment.models import About
from .forms import RegistrationForm
def home(request):
  featured_posts = Blog.objects.filter(is_featured = True, status = 'Published').order_by('-updated_at')
  posts = Blog.objects.filter(is_featured = False, status = 'Published')
  #fetch about us
  try:
    about = About.objects.get()
  except:
    about = None

  
  context = {
    'featured_posts': featured_posts,
    'posts' : posts,
    'about': about,
  }
  return render(request, 'home.html', context)

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    print("Form valid:", form.is_valid())
    print("Form errors:", form.errors)
    if form.is_valid():
      form.save()
      return redirect('register')
    else:
      print(form.errors)
  else:
    form = RegistrationForm()

  form = RegistrationForm()
  context = {
    'form':form,
  }
  return render(request, 'register.html',context)