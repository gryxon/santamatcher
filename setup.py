import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="santamatcher-gryxon",
    version="0.0.0",
    author="gryxon",
    author_email="gryxon@gmail.com",
    description="Package is for matching people in pair in secret way.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gryxon/santamatcher",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': ['santamatcher=santamatcher.cli_sender:main'],
    },
    python_requires='>=3.6',
)