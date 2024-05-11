from setuptools import setup, find_packages

setup(name='gai',
      packages=find_packages(), 
      install_requires=[
            'guidance',
            'openai',
            'vertexai'
      ])