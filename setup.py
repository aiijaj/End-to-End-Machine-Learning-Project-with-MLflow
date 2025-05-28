import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

setuptools.setup(
    name="mlProject",
    version=__version__,
    author="aiijaj",
    author_email="aijajmulla2004@gmail.com",
    description="A small Python package for ML app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aiijaj/End-to-End-Machine-Learning-Project-with-MLflow",
    project_urls={
        "Bug Tracker": "https://github.com/aiijaj/End-to-End-Machine-Learning-Project-with-MLflow/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[],  # you can list requirements here or leave empty
)
