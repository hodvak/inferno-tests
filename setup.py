from setuptools import setup, find_packages
from inferno_tests.tests import __version__

setup(
    name="hac-intro2cs-tests",
    version=__version__,
    packages=find_packages(
        include=["inferno_tests", "inferno_tests.*", "test_ex", "test_ex.*"]
    ),
    author="Hod Vaknin",
    license="MIT",
    description="python tests for Hadassah Academic Collage intro2cs courses",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    project_urls={"Source": "https://github.com/hodvak/inferno-tests"},
    install_requires=[],
    scripts=["inferno_tests/tests.py"],
    entry_points={
        "console_scripts": [
            "test_ex = inferno_tests:test_ex",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
