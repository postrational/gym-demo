import shutil
from collections import namedtuple

import pytest

from gym_demo.formatting import (
    get_columns_count_and_width,
    list_to_columns,
    print_error,
)

TerminalSize = namedtuple("terminal_size", ["columns"])

_GROUP_NAMES = [
    "Acrobot",
    "AirRaid",
    "Alien",
    "Amidar",
    "Assault",
    "Asterix",
    "Asteroids",
    "Atlantis",
    "Berzerk",
    "BipedalWalker",
    "Blackjack",
    "Bowling",
    "Boxing",
    "Breakout",
    "CarRacing",
    "Carnival",
    "CartPole",
    "Centipede",
    "ChopperCommand",
    "CrazyClimber",
    "CubeCrash",
    "DemonAttack",
    "DoubleDunk",
    "DuplicatedInput",
    "ElevatorAction",
    "FetchPickAndPlace",
    "FetchPush",
    "FetchReach",
    "FetchSlide",
    "FishingDerby",
    "Frostbite",
    "GuessingGame",
    "HandManipulateBlock",
    "HandManipulateEgg",
    "HandManipulatePen",
    "HandReach",
    "Humanoid",
    "IceHockey",
    "InvertedDoublePendulum",
    "InvertedPendulum",
    "Jamesbond",
]


@pytest.fixture
def env_group_names():
    return _GROUP_NAMES


def test_get_columns_count_and_width(monkeypatch, env_group_names):
    monkeypatch.setattr(shutil, "get_terminal_size", lambda x: TerminalSize(80))
    assert get_columns_count_and_width(env_group_names) == (3, 25)


@pytest.mark.parametrize("list_size", range(len(_GROUP_NAMES)))
@pytest.mark.parametrize("terminal_size", [5, 20, 40, 80, 160, 500])
def test_list_to_columns(monkeypatch, env_group_names, list_size, terminal_size):
    monkeypatch.setattr(
        shutil, "get_terminal_size", lambda x: TerminalSize(terminal_size)
    )
    env_group_names = env_group_names[0:list_size]
    column_output = list_to_columns(env_group_names)
    lines = column_output.splitlines()

    assert len(" ".join(lines).split()) == len(env_group_names)


def test_print_error(capsys):
    print_error("Error message!")
    print_error("Value:", 123)
    captured = capsys.readouterr()

    assert "Error message!" in captured.out
    assert "Value: 123" in captured.out
