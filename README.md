# django_blog

Django_blog is a django app to make posts on your blog.  

Django_blog was developed in Python 2.7.6 with Django 1.9.6.

### Installing

    git clone https://github.com/Emiliemorais/blog_django_plugin.git
    cd blog_django_plugin/
    python setup.py install
    
### Configuration

* Insert django_blog on your INSTALLED_APPS
        
        INSTALLED_APPS = (
          'django.contrib.auth',
          ...
          'django_blog',
          ...
        )

* Include the django_blog urls on your file

        import django_blog.urls
  
        urlpatterns = [
            ...
            url('^django_blog/', include(django_blog.urls, namespace='dp_blog')),
            ...
        ]

* Run migrations
        
        python manage.py migrate
  
### Usage
* Creating posts
    
  To create new posts with default form, include on your template:

        {% new_post %}
        
  To create new posts with form defined by you, include on your urls:
       
        import django_blog.views as django_blog_views
        url(<url_regex>, django_blog_views.PostView.as_view(), {'template_name': <your_template_name>}, name=<name>)
      
      
      * Now you can create a template using {{form}} to get the elements of the new post form.
* Getting posts
    
    To get all posts from new to old include on your template:

        {% all_posts_new_to_old %}
        
    To get all posts from old to new include on your template:

        {% all_posts_old_to_new %}
