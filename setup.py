from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirments(file_path:str) -> List[str]:
    '''
    this function will return a list of requirements
    '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
nam = 'dev_ml_ops',
version = '0.0.1',
author = 'Aadhil',
author_email = 'aadhil.imam@gmail.com',
packages = find_packages(),
install_requires = get_requirments('requirments.txt')
) 