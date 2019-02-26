"""Test suite for gym-demo."""
import docopt
import gym
import pytest

from gym_demo.demo import (
    get_environment_names,
    get_space_description,
    group_environments,
    main,
    print_environment_description,
    render_environment,
    run_environment,
)


def test_get_environment_names():
    environments = get_environment_names()

    assert len(environments)
    assert "Acrobot-v1" in environments


def test_group_environments():
    environments = get_environment_names()
    group_names = group_environments(environments)

    assert len(group_names) <= len(environments)
    assert "Acrobot" in group_names


def test_get_space_description():
    environment = gym.make("Acrobot-v1")
    description = get_space_description(environment.observation_space)
    assert "Box(6,)" in description
    assert "Low values:\n[ -1" in description


def test_print_environment_description(capsys):
    environment = gym.make("Acrobot-v1")
    print_environment_description(environment)

    captured = capsys.readouterr()
    assert "Environment: Acrobot-v1" in captured.out
    assert "Observation Space:\nBox(6,)" in captured.out


def test_run_environment(capsys):
    environment = gym.make("Acrobot-v1")
    run_environment(environment, steps_count=1, render=False)
    captured = capsys.readouterr()
    assert "Reward: -1.0" in captured.out

    environment = gym.make("CartPole-v1")
    run_environment(environment, render=False, print_observation=True)
    captured = capsys.readouterr()
    assert "Observation: [" in captured.out
    assert "Done after" in captured.out


@pytest.mark.filterwarnings("ignore: numpy.ufunc size changed")
def test_render_environment(monkeypatch):
    environment = gym.make("Acrobot-v1")
    monkeypatch.setattr(environment, "render", lambda: True)
    success = render_environment(environment)
    assert success is True

    environment = gym.make("Roulette-v0")
    success = render_environment(environment)
    assert success is False


def test_main_no_options():
    with pytest.raises(docopt.DocoptExit):
        main()
