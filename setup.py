#!/usr/bin/env python
"""
Setup script for gym-demo.

https://github.com/postrational/gym-demo"
"""
import os

from setuptools import setup

setup(
    name="gym-demo",
    version="0.2.2",
    description="Explore OpenAI Gym environments.",
    long_description=open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
    ).read(),
    long_description_content_type="text/markdown",
    author="Michal Karzynski",
    author_email="github@karzyn.com",
    url="https://github.com/postrational/gym-demo",
    packages=["gym_demo"],
    install_requires=["setuptools", "gym", "docopt", "colorful"],
    setup_requires=["pytest-runner"],
    entry_points={"console_scripts": ["gym-demo = gym_demo.demo:main"]},
)
