"""Test suite for gym-demo."""
import gym

from gym_demo.demo import (
    get_environment_names,
    get_space_description,
    list_to_columns,
    print_environment_description,
    render_environment,
    run_environment,
)


def test_get_environment_names():
    environments = get_environment_names()

    assert len(environments)
    assert "Acrobot-v1" in environments


def test_get_space_description():
    environment = gym.make("Acrobot-v1")
    description = get_space_description(environment.observation_space)
    assert "Box(6,)" in description
    assert "Low values: [ -1" in description


def test_print_environment_description(capsys):
    environment = gym.make("Acrobot-v1")
    print_environment_description(environment)

    captured = capsys.readouterr()
    assert "Environment: Acrobot-v1" in captured.out
    assert "Observation Space: Box(6,)" in captured.out


def test_list_to_columns():
    column_output = list_to_columns(["one", "two", "three", "four", "five"])
    lines = column_output.splitlines()
    assert len(lines) == 2
    assert "three" in lines[0]
    assert "four" in lines[1]


def test_run_environment(capsys):
    environment = gym.make("Acrobot-v1")
    run_environment(environment, steps_count=1, render=False)

    captured = capsys.readouterr()
    assert "Reward: -1.0" in captured.out


def test_render_environment(monkeypatch):
    environment = gym.make("Acrobot-v1")
    monkeypatch.setattr(environment, "render", lambda: True)
    success = render_environment(environment)
    assert success is True

    environment = gym.make("Roulette-v0")
    success = render_environment(environment)
    assert success is False
