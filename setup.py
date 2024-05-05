import setuptools

with open("README.md","r",encoding="utf-8", errors="ignore") as fh:
	long_description = fh.read()

setuptools.setup(
	name="promptparse.py",
	version="0.0.1",
	author="M-307",
	author_email="me@m307.dev",
	description="Promptparse (maybe)",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/mrwan200/pytwitterscraper",
	keywords = ['promptparse', 'promptpat', 'tlv','emvcoqr'],
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires=">=3.9",
	include_package_data=True
)