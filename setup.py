from setuptools import setup, find_packages

setup(
    name="contador",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "numpy",
        "matplotlib",
        "scipy"
    ],
    descripcion="contar celulas",
)