#!/usr/bin/env python
"""
Setup script for gym-demo.

https://github.com/postrational/gym-demo"
"""

from setuptools import setup

setup(
    name="gym-demo",
    version="0.1.0",
    description="Explore OpenAI Gym environments.",
    author="Michal Karzynski",
    author_email="github@karzyn.com",
    url="https://github.com/postrational/gym-demo",
    packages=["gym_demo"],
    install_requires=["setuptools", "gym", "docopt"],
    setup_requires=["pytest-runner"],
    entry_points={"console_scripts": ["gym-demo = gym_demo.demo:main"]},
)
