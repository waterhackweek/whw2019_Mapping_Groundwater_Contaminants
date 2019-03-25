import os
import sys
from setuptools import setup, find_packages
from tethys_apps.app_installation import find_resource_files

# -- Apps Definition -- #
app_package = 'gw_contaminants'
release_package = 'tethysapp-' + app_package
app_class = 'gw_contaminants.app:GwContaminants'
app_package_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tethysapp', app_package)

# -- Please list all dependencies in the init.yml file -- #
# -- Python Dependencies -- #
dependencies = []

# -- Get Resource File -- #
resource_files = find_resource_files('tethysapp/' + app_package + '/templates')
resource_files += find_resource_files('tethysapp/' + app_package + '/public')


setup(
    name=release_package,
    version='0.0.1',
    tags='',
    description='',
    long_description='',
    keywords='',
    author='Rohit Khattar',
    author_email='rohit@byu.net',
    url='',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    package_data={'': resource_files},
    namespace_packages=['tethysapp', 'tethysapp.' + app_package],
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies
)
