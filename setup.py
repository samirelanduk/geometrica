from setuptools import setup

setup(
 name="geometrica",
 version="0.1.0",
 description="A pure-Python geometry library",
 url="https://geometrica.samireland.com",
 author="Sam Ireland",
 author_email="mail@samireland.com",
 license="MIT",
 classifiers=[
  "Development Status :: 4 - Beta",
  "Intended Audience :: Science/Research",
  "License :: OSI Approved :: MIT License",
  "Topic :: Scientific/Engineering :: Mathematics",
  "Programming Language :: Python :: 3",
  "Programming Language :: Python :: 3.0",
  "Programming Language :: Python :: 3.1",
  "Programming Language :: Python :: 3.2",
  "Programming Language :: Python :: 3.3",
  "Programming Language :: Python :: 3.4",
  "Programming Language :: Python :: 3.5",
  "Programming Language :: Python :: 3.6",
 ],
 keywords="geometry trigonometry coordinates shapes",
 packages=["geometrica"],
 install_requires=["matrices"]
)
