from setuptools import setup, find_packages

with open("README.md", "r") as doc_file:
    long_doc = doc_file.read()

descricao = "Uma inteligência artificial simplificada para fins didáticos ou aplicações minimas"

setup(
    name="simple-neural-network",
    version="0.0.1",
    author="oopaze",
    description=descricao,
    long_description=long_doc,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: General Public License :: GNU",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.8",
    install_requires=[],
    py_modules=[],
)
