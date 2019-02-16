#!/usr/bin/env python

"""Usage: gym_demo.py [--steps=NN --no-render --observations] ENV_NAME

Show a random agent playing in a given OpenAI environment.

Arguments:
  ENV_NAME          Name of the Gym environment to run

Options:
  -h --help
  --steps=<STEPS>   How many iteration to run for.  [default: 5000]
  --no-render       Don't render the environment graphically.
  --observations    Print environment observations.

"""
import re
from time import sleep
from itertools import zip_longest

import gym
from docopt import docopt


def get_environment_names():
    return [spec.id for spec in gym.envs.registry.all()]


def get_space_description(space):
    description = repr(space)
    if isinstance(space, gym.spaces.Box):
        description += "\nLow values: {}".format(space.low)
        description += "\nHigh values: {}".format(space.high)
    return description


def print_environment_description(env):
    print("Environment: {}\n".format(env.spec.id))
    print("Observation Space: {}\n".format(get_space_description(env.observation_space)))
    print("Action Space: ()".format(get_space_description(env.action_space)))
    if hasattr(env.unwrapped, "get_action_meanings"):
        print("Action meanings:", env.unwrapped.get_action_meanings())
    print("\n")


def list_to_columns(strings):
    strings_in_columns = ""
    strings = sorted(strings)
    for col1, col2, col3 in zip_longest(
        strings[::3], strings[1::3], strings[2::3], fillvalue=""
    ):
        strings_in_columns += "{:<50}{:<50}{:<}\n".format(col1, col2, col3)
    return strings_in_columns


def run_environment(env, steps_count, render=True, print_observation=False):
    env.reset()
    prev_env_output = None
    for step in range(steps_count):
        observation, reward, done, info = env.step(env.action_space.sample())

        if render:
            env.render()
            sleep(0.01)

        if (reward, done, info) != prev_env_output:
            print("Reward: {}, Done: {}, Info: {}".format(reward, done, info))
            prev_env_output = (reward, done, info)

        if print_observation:
            print("Observation: {}".format(observation))

        if done:
            break

    env.close()


def main():
    environment_names = get_environment_names()

    help_string = "{}\n\nAvailable environments:\n\n{}".format(
        __doc__, list_to_columns(environment_names)
    )
    arguments = docopt(help_string)

    steps = int(arguments.get("--steps"))
    render_env = not arguments.get("--no-render")
    print_observations = arguments.get("--observations")
    env_name = arguments.get("ENV_NAME")

    if env_name in environment_names:
        environment = gym.make(env_name)
        print_environment_description(environment)
        run_environment(environment, steps, render_env, print_observations)

    else:
        print("ERROR: Environment with requested ID not found.")
        regex = re.compile(".*{}.*".format(env_name), re.IGNORECASE)
        environment_names = [
            spec.id for spec in gym.envs.registry.all() if regex.match(spec.id)
        ]
        if len(environment_names):
            print("\nPerhaps you were looking for:")
            print(list_to_columns(environment_names))


if __name__ == "__main__":
    main()
