from setuptools import setup

setup(
    name='pacman',
    version='1.0',
    description='Pacman',
    license='GPL',
    author='Peter Leddiman',
    author_email='peter.leddiman@gmail.com',
    packages=['pacman_game'],
    include_package_data=True,
    install_requires=['pygobject'],
    scripts=['pacman']
)
