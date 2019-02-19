import shutil
from collections import namedtuple

import pytest

from gym_demo.formatting import get_columns_count_and_width, list_to_columns

TerminalSize = namedtuple("terminal_size", ["columns"])


@pytest.fixture
def env_group_names():
    return [
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


def test_get_columns_count_and_width(monkeypatch, env_group_names):
    monkeypatch.setattr(shutil, "get_terminal_size", lambda x: TerminalSize(80))
    assert get_columns_count_and_width(env_group_names) == (3, 25)


def test_list_to_columns(monkeypatch, env_group_names):
    monkeypatch.setattr(shutil, "get_terminal_size", lambda x: TerminalSize(80))
    column_output = list_to_columns(env_group_names)
    lines = column_output.splitlines()
    assert len(lines) == 14
    assert "Acrobot" in lines[0]
    assert "AirRaid" in lines[1]
    assert len(" ".join(lines).split()) == len(env_group_names)
