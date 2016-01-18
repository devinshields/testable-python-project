try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'TODO: My Project',
    'author': 'Devin Shields',
    'url': 'TODO: URL to get it at.',
    'download_url': 'TODO: Where to download it.',
    'author_email': 'TODO:',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['amazmodule'],
    'scripts': [],
    'name': 'amazmodule'
}

setup(**config)
