import setuptools

with open('README.md', 'r',encoding='utf-8') as f:
    long_discreption = f.read()

__version__ = '0.0.1'

REPO_NAME = 'ML_Project_Three'
AUTHOR_USER_NAME = 'RohitDas92'
SRC_REPO = 'chicken_disease_CNN'
AUTHOR_EMAIL = 'rhtdas1992@gmail.com'

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small python package for image classification using CNN',
    long_description=long_discreption,
    long_discreption_content = 'text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls = {
        'Bug Tracker': f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues',
    },
    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src')
)