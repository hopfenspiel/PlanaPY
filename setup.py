from setuptools import setup, find_packages


setup(
    name='planapy',
    version='0.1.0',
    license='MIT',
    author='Erik Schau',
    author_email='hopfenspiel@gmail.com',
    packages=find_packages(include=['src']),
    description='Anaplan RESTful API Convenience Library',
    url='https://github.com/hopfenspiel/PlanaPY',
    keywords='anaplan',
    install_requires=[
          'requests',
          'pandas',
      ],

)
