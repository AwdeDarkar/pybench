PyBench Core
============

This is a module designed to be a general-purpose 'experiment bench' where I can
play with a variety of simulation visualizations and game prototypes. While it is
mostly intended for my personal use, I hope to make it of publishable quality,
with good documentation and with a stable CLI interface.

Feature Goals
-------------

There are a few main features that I want for this, some more ambitious than others.

### Project-Based CLI

Like Django, Node, Sphinx, and other frameworks, I want to be able to install this
as a module and call it from the command line to create an empty project. My hope
is that this would help with standardization and interoperability (maybe).

### Modal

One of the core aspects of PyBench is that, like vim, it operates based on 'modes';
at minimum, there will be 'edit', 'examine' and 'simulate' modes, each optimized for
a specific kind of use and each with unique UI and keyboard features.

### UX Language

I also plan to build a highly-opinionated set of UX conventions and expectations.
This should make it easier to design features in the future and help ease-of-use.

### Determinism

I want simulations to be deterministic; that means seeded values with the seed
naturally regenerating each time.

### History

I want to save editor actions and simulations so that they can be regenerated
precisely, with features for naming and commenting on runs.

### Video

Also, it could be good to record each frame so I can make videos about it later.
