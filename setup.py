from setuptools import setup, find_packages
from typing import List

hypen_e_dot = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function returns the list of requirements.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Use strip() to remove leading/trailing whitespace
    

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='sanjana',
    author_email='sanjanathiruvathira@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
