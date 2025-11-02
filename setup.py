from setuptools import find_packages, setup

setup(
    name='netbox-hello',
    version='0.1',
    description='Simple demo plugin for NetBox',
    author='Ichha Kr Thapa',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
