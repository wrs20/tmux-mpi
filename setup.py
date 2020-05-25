from setuptools import setup, find_packages

long_description = """"""

install_requires = []
with open('requirements.txt') as fh:
    for l in fh:
        if len(l) > 0:
            install_requires.append(l)

setup(
   name='tmux-mpi',
   version='1.0',
   description='',
   license="GPL3",
   long_description=long_description,
   author='William R Saunders',
   author_email='W.R.Saunders@bath.ac.uk',
   url="https://github.com/wrs20/tmux-mpi",
   packages=find_packages(),
   install_requires=install_requires,
   scripts=['tmux-mpi'],
   include_package_data=True
)
