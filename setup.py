from setuptools import find_packages, setup

PKG_NAME = "dz_phone_numbers"

with open("README.md", "r") as fh:
    long_description = fh.read()

dev_dependencies = ["pytest"]

setup(
    name=PKG_NAME,
    version="1.0.0",
    license="MIT",
    author="Walid Ziouche",
    author_email="hi@walid.dev",
    description="Algerian phone numbers as value object, python implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="dz phone number tel telephone mobile regex",
    extras_require={"dev": dev_dependencies},
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Telecommunications Industry",
        "Topic :: Utilities",
        "Typing :: Typed",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires=">=3.6, <4",
    project_urls={
        "Bug Reports": "https://github.com/01walid/py-dz-phone-number/issues",
        "Source": "https://github.com/01walid/py-dz-phone-number",
    },
)
