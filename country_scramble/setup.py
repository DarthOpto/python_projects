"""Country Scrambler"""
import os

from setuptools import find_packages, setup

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(BASE_PATH, "README.md"), encoding="utf-8") as readme_file:
    LONG_DESCRIPTION = readme_file.read()

with open(
    os.path.join(BASE_PATH, "requirements.txt"), encoding="utf-8"
) as requirements_file:
    REQUIREMENTS = requirements_file.read()

PACKAGES = find_packages(BASE_PATH)

ENTRY_POINTS = {
    "console_scripts": [
        # 'flask: flask.test_runner.main'
    ]
}

setup(
    author="Curtis Salisbury",
    author_email="curtis.salisbury@gmail.com",
    description=__doc__,
    entry_points=ENTRY_POINTS,
    long_description=LONG_DESCRIPTION,
    install_requires=REQUIREMENTS,
    name="Country Scrambler",
    packages=PACKAGES,
    python_requires=">=3.7.*",
    version="0.0.1",
)
