import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="depict", # Replace with your own username
    version="0.0.2",
    author="Victor Boulanger",
    author_email="vb@live.fr",
    description="Insightful plots in seconds",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vboulanger/depict",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    python_requires='>=3.6',
)

