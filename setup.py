from setuptools import setup, find_packages

setup(
    name="repo2txt",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "python-docx",
        # Añade aquí otras dependencias si las hay
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