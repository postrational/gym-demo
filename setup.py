#!/usr/bin/env python

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
    entry_points={"console_scripts": ["gym-demo = gym_demo.demo:main"]},
)
