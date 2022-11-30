from setuptools import find_packages,setup

from typing import List

requirement_file_name = "requirements.txt"
hypen_e_dot = "-e ."

## This function will provide the list of libraries name that are required for this project
def get_requirements()->List(str): ## List(str) tell the viewer that this function 
                                # is going to generate list of str, it is just a writen type

    with open(requirement_file_name) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]

    if hypen_e_dot in requirement_list:
        requirement_list.remove(hypen_e_dot)
    return requirement_list


setup(
    name = 'sensor',
    version= "0.0.1",
    author= "ineuron",
    author_email = "sahiljosan50@gmail.com",
    packages= find_packages(),
    install_requires=get_requirements(),
)

