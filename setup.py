from setuptools import setup

setup(
	name="notkionpoiskapi",
	version="1.0.0",
	description="Неофициальная библиотека для Kinopoisk API Unofficial",
	long_description=open("readme.md", "r", encoding="utf8").read(),
	long_description_content_type="text/markdown",
	keywords="api kinopoisk python",
	url="https://github.com/DevCraftClub/NotKinoPoiskAPI",
	author="Maxim Harder",
	author_email="dev@devcraft.club",
	install_requires=[
		"requests",
		"python-decouple",
	],
	classifiers=[
		"License :: OSI Approved :: GNUv3 License",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10",
		"Programming Language :: Python :: 3.11",
	],
	zip_safe=False,
)
