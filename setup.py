from setuptools import setup, find_packages

setup(
    name = 'pacman',
    version = '1.0',
    description = 'Pacman',
    license = 'GPL',
    author = 'Peter Leddiman',
    author_email = 'peter.leddiman@gmail.com',
    packages = [
        'pacman_game',
        'pacman_game.controller',
        'pacman_game.model',
        'pacman_game.view',
    ],
    install_requires = ['pygobject'],
    scripts = ['pacman']
)
