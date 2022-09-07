from setuptools import setup, find_packages
import versioneer

setup(
    name='board-games',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url='https://github.com/dp90/board-games.git',
    author='David P. Kroon',
    author_email='davidkroon90@gmail.com',
    description='Board Games Engines',
    long_description='A Python packages to play board games!'
)