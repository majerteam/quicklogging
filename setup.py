
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Logging wrapper',
    'author': 'Feth Arezki',
    'url': 'https://github.com/majerteam/quicklogging',
    'download_url': 'https://github.com/majerteam/quicklogging',
    'author_email': 'tech@majerti.fr',
    'version': '0.1',
    'packages': ['quicklogging'],
    'setup_requires': ['pytest-runner'],
    'tests_require': ['pytest', 'pytest-coverage', 'six'],
    'name': 'quicklogging'
}

setup(**config)
