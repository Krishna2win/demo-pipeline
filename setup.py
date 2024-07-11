from setuptools import setup,find_packages

setup(name="census_income",
      version="0.0.1",
      author="Krishna",
      author_email="krishna@gamil.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )