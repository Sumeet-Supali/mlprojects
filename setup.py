from setuptools import find_packages,setup
from typing import List

hype_e_dot = '-e .' #creating a contstant with vale -e .

def get_req(file_path:str)->List[str]:
    '''
    this will open the file,read line by line  and store in a list
    this list of names will be installed one by one in a single go.
    no need to write pip install......

    -e . this is in requirements.txt file ,it will trigger setup.py and both the file will run same time
    '''

    #empty list
    requirements = []
    with open(file_path) as file_obj:
        #reading lines one by one and storing in list
        requirements = file_obj.readline()

        #removing \n from the list 
        requirements = [x.replace("\n","") for x in requirements]

        if hype_e_dot in requirements:
            requirements.remove(hype_e_dot)

    return requirements



setup(
    name='mlproject',#optional
    author='sumeet',#optional
    author_email='suryasumeet360@gmal.com',#optional
    packages=find_packages(),#converting all codes to one single package.
    install_requires =get_req('requirements.txt'), #calling function with input as filepath name
    version='0.0.1'   #optional
)