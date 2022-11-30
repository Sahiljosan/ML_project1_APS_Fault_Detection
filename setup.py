from setuptools import find_packages,setup

def get_requirements():
    """
    This function will provide the list of libraries name that are required for this project
    """
    pass

setup(
    name = 'sensor',
    version= "0.0.1",
    author= "ineuron",
    author_email = "sahiljosan50@gmail.com",
    packages= find_packages(),
    install_requires=get_requirements()
)

