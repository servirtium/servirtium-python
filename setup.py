from setuptools import setup, find_packages

setup(
    name='servirtium',
    version='0.1.0',
    description='Servirtium service virtualization',
    author='Paul Hammant',
    author_email='paul@hammant.org',
    url='https://github.com/servirtium/servirtium-python',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=find_packages(exclude="test"),
    requires=['requests', 'pytest']
)
