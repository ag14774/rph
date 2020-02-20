import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rph",
    version="1.0.0",
    author="Andreas Georgiou",
    author_email="geandrea@ethz.ch",
    description="PyTorch module for random projection hashing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ag14774/rph.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.6',
)
