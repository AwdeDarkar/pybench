PyBench Version Planning
========================

These are my _expected_ plans for each tagged release and a changelog once the
tags are created.

Versions
--------

### 0.0 - done 2020-04-30 10:51

  + Initial version; basically just planning, minimal content, and structure

#### 0.0.1 - done 2020-04-30 10:51

  + Literally just draw a window

#### 0.0.2

  + Window with the key UI components in place

#### 0.0.3

  + Refactor UI a bit and make it customizable with a config file
  + Also make it look nice

### 0.1

  + Custom sprite classes drawn to canvas

#### 0.1.1

  + Sprite layering
  + UI Sprite primitives
    + With customization support

#### 0.1.2

  + Nominal 'edit' and 'simulation' modes
  + Selectable dropable sprites that do things in simulation

#### 0.1.3

  + Arbitrary mode support with each mode getting a UI layer
  + Customizable keyboard controls for arbitrary modes

### 0.2

  + Seed in util config
  + Simulation history saving
  + Simulation frame saving
  + Simulation state loading and saving

### 1.0

  + Package installable with CLI tools
    + Including `init` command to create a new bench project
