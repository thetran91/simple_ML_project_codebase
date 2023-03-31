from setuptools import find_packages,setup
from typing import List # allow assign returned datatypes 

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
name='ML Project Codebase',
version='0.0.1',
author='Eric Tran',
author_email='ericdataguy77@gmail.com',
packages=find_packages(), # find all subpackages (with __init__.py included) - E.g. src
install_requires=get_requirements('requirements.txt')

)