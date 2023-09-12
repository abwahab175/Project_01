from setuptools import setup, find_packages

def get_requirements(file_path):
    requirements=[]
    with open(file_path,'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n",'')for req in requirements]
    return requirements


setup(

    name = "Project_01",
    version = "0.0.1",
    description="this is a test project for ML pipeline",
    author = 'Abdul Wahab Memon',
    author_email = 'abwahab175@gmail.com',
    packages= find_packages(),
    install_requirements = get_requirements('requirements.txt')
)
