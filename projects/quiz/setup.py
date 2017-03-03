try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description' : 'quiz',
    'author' : 'Ammar Shaqeel',
    'url' : 'NA',
    'download_url' : 'NA',
    'author_email' : 'My email.',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['quiz'],
    'scripts' : [],
    'name' : 'quiz'
}

setup(**config)
    
