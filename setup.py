from setuptools import setup, find_packages

setup(
    name="controller",
    packages=find_packages(),
    author="Martin Styk",
    author_email="mart.styk@gmail.com",
    description="Controller",
    python_requires=">=3.9",
    setup_requires=["setuptools-git-versioning"],
    version_config={
        "dev_template": "{tag}.post{ccount}-git.{sha}",
    },
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
