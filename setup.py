from setuptools import setup

with open("README.md", 'r', encoding='utf-8') as fh:
    long_description = fh.read()

AUTHOR_NAME = 'Gargeya'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='gargiinnamuri@gmail.com',
    description="Movie Recommender System along with a web app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[SRC_REPO], 
    python_requires='>=3.7',  
    install_requires=LIST_OF_REQUIREMENTS,
)
