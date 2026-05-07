from setuptools import setup, find_packages

setup(
    name="contador", packages=find_packages(), install_requires=[
        "numpy",
        "opencv-python",
        "matplotlib"
    ],
)