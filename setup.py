import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="depict",
    version="0.1",
    author="Victor Boulanger",
    author_email="vb@live.fr",
    description="Business grade visualizations in seconds",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vboulanger/depict",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    python_requires='>=3.6',
)

# https://pypi.org/classifiers/
