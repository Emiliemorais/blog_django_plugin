from distutils.core import setup

setup(name='DP Blog',
    version='0.1.0',
    description='Django plugin for blogs',
    author='Emilie Morais',
    author_email='emilie.mo@hotmail.com',
    url='https://github.com/Emiliemorais/blog_django_plugins',
    license='BSD License',
    install_requires=[
        'django=1.9',
    ],
    packages=[
        'django_blog',
        'django_blog.migrations',
        'django_blog.templatetags',
    ],
    package_data={
        'django_blog': ['templates/*.html', 'locale/pt_BR/LC_MESSAGES/*']        
    },
)