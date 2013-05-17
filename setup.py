from setuptools import setup, find_packages
import sys, os

version = '0.1'

def read(fname):
    # file read function copied from sorl.django-documents project
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-files-widget',
    version=version,
    description="Django AJAX upload widget and model field for multiple files or images, featuring drag & drop uploading, upload progress bar, sortable image gallery",
    long_description=read('README.md'),
    classifiers=[
        # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='django ajax html5 upload widget files images gallery sorting progress thumbnails multiple m2m imagesfield imagefield filesfield filefield admin forms field',
    author='Top Notch Development',
    author_email='info@topnotchdevelopment.nl',
    url='http://topnotchdevelopment.nl',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'sorl-thumbnail',
        'mezzanine',
    ],
    entry_points="""
        # -*- Entry points: -*-
    """,
)