from setuptools import setup, find_packages

setup(
    name="ekacare-sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "pyjwt>=2.0.0",
    ],
    author="Eka Care SDK Developer",
    author_email="developer@eka.care",
    description="Python SDK for Eka Care APIs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords="healthcare, eka care, api, sdk, health records, abdm",
    url="https://developer.eka.care",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.6",
)
