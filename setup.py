import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamlit-hierarchical-select",
    version="0.0.1",
    author="Prathamesh Joshi",
    author_email="PrathameshJoshi9199@gmail.com",
    description="A Streamlit custom component for hierarchical/tree selection with search.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Prathamesh9199/streamlit-hierarchical-select",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "streamlit >= 0.63",
    ],
)