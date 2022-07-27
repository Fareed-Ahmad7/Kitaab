import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kitaab",                     # This is the name of the package
    version="0.0.4",                        # The initial release version
    author="Shaik Fareed Ahammad",                     # Full name of the author
    description="kitaab is a cli note-taking app",
    # Long description read from the the readme file
    long_description=long_description,
    long_description_content_type="text/markdown",
    # List of all python modules to be installed
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["kitaab"],             # Name of the python package
    # Directory of the source code of the package
    package_dir={'': 'src'},
    install_requires=[
        'rich ==12.4.4',
        'PyGithub ==1.55',
        'pytest==7.1.2'
        ]                     # Install other dependencies if any
)
