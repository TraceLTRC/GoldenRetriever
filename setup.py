from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="GoldenRetriever",
    version="0.0.1",
    author="TraceL",
    author_email="kivlanbahmidt@gmail.com",
    description="A python wrapper for the website E-learning Management Systems of UI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TraceLosu/GoldenRetriever",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
   'beautifulsoup4',
   'requests'
    ]
)