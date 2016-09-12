
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
    'version': '0.3',
    'packages': ['quicklogging'],
    'setup_requires': [],
    'tests_require': ['pytest-runner', 'pytest', 'pytest-cov', 'six', 'stringimporter>=0.1.3'],
    'name': 'quicklogging',
    'zip_safe': False,
}

setup(**config)
