from setuptools import setup, find_packages
import os

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

extra_files = package_files('src/repo2txt')

setup(
    name="repo2txt",
    version="0.1.0",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={'repo2txt': extra_files},
    include_package_data=True,
    install_requires=[
        "python-docx",
    ],
    entry_points={
        "console_scripts": [
            "repo2txt=repo2txt.repo2txt:main",
        ],
    },
    author="gatzer",
    author_email="gstuardov@gmail.com",
    description="Una herramienta para convertir repositorios a texto",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://codeberg.org/gatzer/repo2txt",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)