import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="santamatcher-gryxon",
    version="0.1.0",
    author="gryxon",
    author_email="gryxon@gmail.com",
    description="Minimalistic library and script for matching people in pair in secret way and sending notifications "
                "to them.",
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
        'console_scripts': ['santamatcher=santamatcher.scripts.cli_sender:main'],
    },
    python_requires='>=3.6',
)