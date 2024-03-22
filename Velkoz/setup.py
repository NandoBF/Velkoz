from setuptools import setup, find_packages

 #python setup.py sdist bdist_wheel
VERSION = '0.0.3' 
DESCRIPTION = 'Velkoz Riot Api package'
LONG_DESCRIPTION = 'Package that uses RiotApi to get information.\n Made to gain experience so it is not something as advanced as the other packages that do the same. Would not recommend.'

# Setting up
setup(
        name="Velkoz", 
        version=VERSION,
        author="Nabattis",
        author_email="<ferreirafernando6205@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['requests'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'riotapi', 'api'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
