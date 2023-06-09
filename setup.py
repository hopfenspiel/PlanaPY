from setuptools import setup, find_packages

VERSION = '0.2.1'
DESCRIPTION = 'Anaplan RESTful API Convenience Library'

setup(
    name='PlanaPY',
    version=VERSION,
    license='MIT',
    author='Erik Schau',
    author_email='hopfenspiel@gmail.com',
    packages=find_packages(),
    description=DESCRIPTION,
    url='https://github.com/hopfenspiel/PlanaPY',
    keywords='anaplan',
    install_requires=[
          'requests',
          'pandas',
      ],

)
