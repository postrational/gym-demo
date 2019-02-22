[![Build Status](https://travis-ci.org/postrational/gym-demo.svg?branch=master)](https://travis-ci.org/postrational/gym-demo)
[![Coverage Status](https://coveralls.io/repos/github/postrational/gym-demo/badge.svg?branch=master)](https://coveralls.io/github/postrational/gym-demo?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e9866afb65984daf8286501198e3125e)](https://www.codacy.com/app/postrational/gym-demo?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=postrational/gym-demo&amp;utm_campaign=Badge_Grade)
[![PyPI version](https://badge.fury.io/py/gym-demo.svg)](https://badge.fury.io/py/gym-demo)

# gym-demo

##### Explore OpenAI Gym environments

This package provides the `gym-demo` command, which allows you to
explore the various [Open AI gym][gym] environments installed on your
system.

This allows you to get a quick overview of an environment before you
start working on it. You will get information about the environments
*observation space*, *action space* as well as the *rewards* you can
expect to get and other available information.

[![gym-demo on YouTube](https://raw.githubusercontent.com/postrational/gym-demo/master/gym-demo-screenshot.png)](https://www.youtube.com/watch?v=fHuqpwXBBtg)

### Installation

You can install OpenAI Gym and `gym-demo` using `pip`:


    $ pip install gym[atari]
    $ pip install gym-demo


### Usage

Use `gym-demo --help` to display usage information and a list of
environments installed in your Gym.

    $ gym-demo --help

Start a demo of an environment to get information about its observation
and action space and observe the rewards an agent gets during a random
run.

    $ gym-demo SpaceInvaders-ram-v4
    Environment: SpaceInvaders-ram-v4

    Observation Space: Box(128,)
    Low values:
    [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
    High values:
    [255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255
     255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255
     255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255
     255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255
     255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255
     255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255
     255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255
     255 255]

    Action Space: Discrete(6)
    Action meanings: ['NOOP', 'FIRE', 'RIGHT', 'LEFT', 'RIGHTFIRE', 'LEFTFIRE']


    Running environment demonstration...
    Unique environment information is output to standard out:
    Reward: 0.0, Done: False, Info: {'ale.lives': 3}
    Reward: 5.0, Done: False, Info: {'ale.lives': 3}
    Reward: 0.0, Done: False, Info: {'ale.lives': 3}
    Reward: 10.0, Done: False, Info: {'ale.lives': 3}
    Reward: 0.0, Done: False, Info: {'ale.lives': 3}
    Reward: 15.0, Done: False, Info: {'ale.lives': 3}
    Reward: 0.0, Done: False, Info: {'ale.lives': 3}
    Reward: 20.0, Done: False, Info: {'ale.lives': 3}
    Reward: 0.0, Done: False, Info: {'ale.lives': 3}
    Reward: 25.0, Done: False, Info: {'ale.lives': 3}
    Reward: 0.0, Done: False, Info: {'ale.lives': 3}
    Reward: 0.0, Done: False, Info: {'ale.lives': 2}
    Reward: 30.0, Done: False, Info: {'ale.lives': 2}
    Reward: 0.0, Done: False, Info: {'ale.lives': 2}
    Reward: 0.0, Done: False, Info: {'ale.lives': 1}
    Reward: 5.0, Done: False, Info: {'ale.lives': 1}
    Reward: 0.0, Done: False, Info: {'ale.lives': 1}
    Reward: 10.0, Done: False, Info: {'ale.lives': 1}
    Reward: 0.0, Done: False, Info: {'ale.lives': 1}
    Reward: 15.0, Done: False, Info: {'ale.lives': 1}
    Reward: 0.0, Done: False, Info: {'ale.lives': 1}
    Reward: 20.0, Done: False, Info: {'ale.lives': 1}
    Reward: 0.0, Done: False, Info: {'ale.lives': 1}
    Reward: 0.0, Done: True, Info: {'ale.lives': 0}



[gym_docs]: https://gym.openai.com/docs/ "OpenAI Gym Documentation"
[gym_site]: https://gym.openai.com/ "OpenAI Gym"
[gym]: https://github.com/openai/gym "OpenAI Gym GitHub"
