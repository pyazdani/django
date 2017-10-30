  from __future__ import unicode_literals
  from django.db import models
  # Create your models here.
  class Blog(models.Model):
      name = models.CharField(max_length=255)
      desc = models.TextField()
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
  class Comment(models.Model):
      comment = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      # Notice the association made with ForeignKey for a one-to-many relationship
      # There can be many comments to one blog
      blog = models.ForeignKey(Blog, related_name = "comments")
  class Admin(models.Model):
      first_name = models.CharField(max_length=255)
      last_name = models.CharField(max_length=255)
      email = models.CharField(max_length=255)
      blogs = models.ManyToManyField(Blog, related_name = "admins")
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)


  class Author(models.Model):
  name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  class Book(models.Model):
  title = models.CharField(max_length=255)
  author = models.ForeignKey(Author, related_name="books")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  ### QUERIES ###
  this_author = Author.objects.get(id=2)
  my_book = Book.objects.create(title="Little Women", author=this_author)
  # or on one line...
  my_book = Book.objects.create(title="Little Women", author=Author.objects.get(id=2))

  this_author = Author.objects.get(id=2)
  books = Book.objects.filter(author=this_author)
  # one-line version:
  books = Book.objects.filter(author=Author.objects.get(id=2))

  books = Book.objects.filter(author__name="Louise May Alcott")
  books = Book.objects.filter(author__name__startswith="Lou")

  ## VIEWS.PY FILE ##
  def index(request):
  context = {"authors": Author.objects.all()}
  return render(request, "books/index.html", context)

  ## TEMPLATES/HTML FILE ##
  <h1>Author List</h1>
  <ul>
    {% for author in authors %}
      <li>{{author.name}}
        <ul>
          {% for book in author.books.all %}
            <li><em>{{book.title}}</em></li>
          {% endfor %}
        </ul>
      </li>
    {% endfor %}
  </ul>

  ## MANY TO MANY RELATIONSHIPS ##
  class Book(models.Model):
  title = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  class Publisher(models.Model):
  name = models.CharField(max_length=255)
  books = models.ManyToManyField(Book, related_name="publishers")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  this_book = Book.objects.get(id=4)
  this_publisher = Publisher.objects.get(id=2)
  this_book.publishers.add(this_publisher) !!!OR!!! this_publisher.books.add(this_book) OR this_book.publishers.all() 

  def __repr__(self):
    return "<Blog object: {} {}>".format(self.name, self.desc)

##ADDING VALIDATIONS##
  # Inside your app's models.py file
from __future__ import unicode_literals
from django.db import models
#Our new manager!
#No methods in our new manager should ever catch the whole request object with a parameter!!! (just parts, like request.POST)
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Blog name should be more than 5 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Blog desc should be more than 10 characters"
        return errors;
class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = BlogManager()
    # *************************

# Inside your app's views.py file
from django.shortcuts import render, HttpResponse, redirect
from .models import Blog
def update(request):
    errors = Blog.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/blog/edit/'+id)
        else:
            blog = Blog.objects.get(id = id)
            blog.name = request.POST['name']
            blog.desc = request.POST['desc']
            blog.save()
            return redirect('/blogs')

## KEYWORD NAMING ROUTES AND FORMS ##

# Inside your app's urls.py file
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.toindex, name='my_index'),
    url(r'^this_app/new$', views.new, name='my_new'),
    url(r'^this_app/(?P<id>\d+)/edit$', views.edit, name='my_edit'),
    url(r'^this_app/(?P<id>\d+)/delete$', views.delete, name='my_delete'),
    url(r'^this_app/(?P<id>\d+)$', views.show, name='my_show'),
]

<!-- Inside your app's index.html file -->
<a href="/target/this_app/new"></a>
<!-- is the equivalent of:  -->
<a href="{% url 'my_new' %}"></a>
<!-- This form's action attribute -->
<form class="" action="/target/this_app/5/delete" method="post">
  <input type="submit" value="Submit">
</form>
<!-- is the equivalent of: -->
<form class="" action="{%url 'my_delete' id=5 %}" method="post">
  <input type="submit" value="Submit">
</form>

## REDIRECT FROM VIEWS.PY ##
# Inside your app's views.py file
from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
# Create your views here.
# Example of an old index method:
def index(request):
    print("hello, I am your first request")
    return redirect('/target/this_app/new')
# Can be transformed to the following:
def index(request):
   print("hello, I am your first request")
   return redirect(reverse('my_new'))

## FOR MULTIPLE APPS IN A PROJECT ##
urlpatterns = [
    url(r'^accounts/', include('apps.login_reg_app.urls', namespace='users')),
    url(r'^courses/', include('apps.courses_app.urls', namespace='courses')),
]

<!-- Inside a Django template (.html) -->
<a href="{% url 'courses:index' %}">This link will hit the index route in your courses_app</a>
<a href="{% url 'users:index' %}">And this link will hit the index route in your login_reg_app</a>

#In a views.py method
return redirect(reverse('users:new'))
#-If you need to pass in a Keyword Argument(kwarg) to show ID of multiple routes(blog id, etc.)
return redirect(reverse('users:show', kwargs={'id': your_id_variable }))
