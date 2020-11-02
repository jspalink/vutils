from setuptools import setup, find_packages

# Lib requirements
requires = [
    'textblob',
    'nltk'
]

setup(
    name='vutils',
    version='1.0.0',
    
    package_dir={'': 'src'},
    namespace_packages=['vutils'],
    packages=find_packages('src'),
    zip_safe=False,
    install_requires=requires,
    url='',
    license='',
    author='Jonathan Spalink',
    author_email='jspalink@econtext.ai',
    description='Some simple utility functions for working with the Veritone Engine (v3)'
)

