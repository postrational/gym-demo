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
import math
import re
import shutil
from itertools import zip_longest
from time import sleep
from typing import List, Text

import gym
from docopt import docopt


def get_environment_names() -> List[Text]:
    """Return a list of names of registered Open AI Gym environments."""
    return sorted(spec.id for spec in gym.envs.registry.all())


def group_environments(env_names: List[Text]) -> List[Text]:
    """Group a sorted list of environment names into families."""
    names_without_version = [name.split("-")[0] for name in env_names]
    family_names = [names_without_version.pop(0)]
    for name in names_without_version:
        if not family_names[-1] in name:
            family_names.append(name)
    return family_names


def get_space_description(space: gym.Space) -> Text:
    """Return a textual description of gym.Space object."""
    description = repr(space)
    if isinstance(space, gym.spaces.Box):
        description += "\nLow values:\n{0}".format(space.low)
        description += "\nHigh values:\n{0}".format(space.high)
    return description


def print_environment_description(env: gym.Env) -> None:
    """Output the Gym environment description to standard out."""
    print("Environment: {0}\n".format(env.spec.id))
    print(
        "Observation Space: {0}\n".format(get_space_description(env.observation_space))
    )
    print("Action Space: {0}".format(get_space_description(env.action_space)))
    if hasattr(env.unwrapped, "get_action_meanings"):
        print("Action meanings:", env.unwrapped.get_action_meanings())
    print("\n")


def list_to_columns(strings: List[Text]) -> Text:
    """Prepare multi-column output string from a list of strings."""
    terminal_width = shutil.get_terminal_size((80, 20)).columns
    max_string_width = max(len(string) for string in strings)
    margin = 3
    col_width = max_string_width + margin
    num_cols = int(terminal_width / col_width)
    col_height = math.ceil(len(strings)/num_cols)
    cols = [strings[i:i + col_height] for i in range(0, len(strings), col_height)]

    format_string = "{:<}\n"
    for _ in range(num_cols-1):
        format_string = "{{:<{}}}{}".format(col_width, format_string)

    strings_in_columns = ""
    for col_strings in zip_longest(*cols, fillvalue=""):
        strings_in_columns += format_string.format(*col_strings)
    return strings_in_columns


def render_environment(env: gym.Env) -> bool:
    """Graphically render state of environment.

    Return true if rendering was successful, false otherwise.
    """
    try:
        env.render()
        sleep(0.02)
        return True
    except NotImplementedError:
        return False


def run_environment(
    env: gym.Env,
    steps_count: int = 1000,
    render: bool = True,
    print_observation: bool = False,
) -> None:
    """Execute main environment run loop.

    Renders environment state graphically and outputs environment information to
    standard out.

    :param env: the environment to run
    :param steps_count: how many steps to run for?
    :param render: should the environment be rendered graphically?
    :param print_observation: should the full observed state be output to std out?
    """
    env.reset()
    print("Running environment demonstration...")
    print("Unique environment information is output to standard out:")
    prev_env_output = None
    for _ in range(steps_count):
        observation, reward, done, info = env.step(env.action_space.sample())

        if render:
            render = render_environment(env)

        if (reward, done, info) != prev_env_output:
            print("Reward: {0}, Done: {1}, Info: {2}".format(reward, done, info))
            prev_env_output = (reward, done, info)

        if print_observation:
            print("Observation: {0}".format(observation))

        if done:
            break

    env.close()


def main() -> None:
    """Process script argument and run."""
    environment_names = get_environment_names()
    environment_families = group_environments(environment_names)

    help_string = "{0}\n\nAvailable environments:\n\n{1}".format(
        __doc__, list_to_columns(environment_families)
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
        regex = re.compile(".*{0}.*".format(env_name), re.IGNORECASE)
        environment_names = [
            spec.id for spec in gym.envs.registry.all() if regex.match(spec.id)
        ]
        if len(environment_names):
            print("\nPerhaps you were looking for:")
            print(list_to_columns(environment_names))


if __name__ == "__main__":
    main()
