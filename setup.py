from setuptools import find_packages, setup
from typing import List  # Correctly imported for use with Python 3.8

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:  # Use List from the typing module
    """
    This function will return the list of requirements.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='syd.asadnaqvi@gmail.com',
    author_email='syd.asadnaqvi@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
