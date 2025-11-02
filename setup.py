from setuptools import setup, find_packages

setup(
    name="netbox-hello-world",
    version="0.1.0",
    description="Hello‑World plugin for NetBox 4.4.4",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)

