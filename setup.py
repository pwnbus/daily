try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Daily Taskboard',
    'author': 'Brandon Myers',
    'url': 'https://github.com/pwnbus/daily',
    'download_url': 'https://github.com/pwnbus/daily/archive/master.zip',
    'author_email': 'pwnbus@mozilla.com',
    'version': '0.0.1',
    'install_requires': [
        'Flask==1.0.2',
        'Flask-SQLAlchemy==2.2',
        'mysqlclient==1.3.12',
        'PyYAML'
    ],
    'packages': ['daily'],
    'scripts': [],
    'name': 'daily'
}

setup(**config)
