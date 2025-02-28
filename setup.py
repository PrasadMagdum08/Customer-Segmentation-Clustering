from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open(file_path, "r") as file_obj:
        requirements = file_obj.readlines()

        requirements = [req.replace('\n', '') for req in requirements]


setup(
    name="Air_Quality_App",
    version="0.0.1",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)