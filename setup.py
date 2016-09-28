#!/usr/bin/python2

from setuptools import setup, find_packages


setup(
    name = "haverifier",
    version = "1.1.0",
    packages = find_packages(),
    package_dir = {},
    zip_safe = False,
    # zip_safe = True,
    package_data = {
        "services":[
            "*.yaml",
        ],
        "haverifier": [
            "./benchmark/scenarios/availability/*.yaml",
            "./benchmark/scenarios/availability/attacker/*.yaml",
            "./benchmark/scenarios/availability/ha_tools/*.bash",
            "./benchmark/scenarios/availability/ha_tools/*/*.bash",
            "./benchmark/scenarios/availability/attacker/scripts/*/*.bash",
        ]
    },
    include_package_data = True,
    install_requires = [
        "PyYAML",
        "oslo.config",
        "paramiko",
        "cryptography",
        "scp",
        ],
    entry_points={
        "console_scripts": [
            "haverifier=haverifier.main:main"
        ],
    },
)
