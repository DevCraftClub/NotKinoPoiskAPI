from setuptools import setup

setup(
    name="notkionpoiskapi",
    version="1.0.0",
    description="Неофициальная библиотека для Kinopoisk API Unofficial",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    keywords="api kinopoisk python",
    url="https://github.com/DevCraftClub/NotKinoPoiskAPI",
    author="Maxim Harder",
    author_email="dev@devcraft.club",
    packages=["notkionpoiskapi"],
    install_requires=[
        "requests",
        "python-decouple"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    zip_safe=False,
)