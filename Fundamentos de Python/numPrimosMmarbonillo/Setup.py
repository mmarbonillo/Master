import setuptools 
  
with open("README.md", "r") as fh: 
    long_description = fh.read() 
  
setuptools.setup( 
    
    name="numPrimosMmarbonillo", 
    version="0.1.0",
    author="María Del Mar Fernández Bonillo", 
    author_email="mbonillo95@gmail.com",
    keywords="mmarbonillo primosMmarbonillo primos",
    packages=setuptools.find_packages(),
    license="MIT",
    
    classifiers=[ 
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3", 
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent", 
    ]
)