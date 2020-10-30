# PyBites Python Code Challenge 26: Create a Simple Python GUI

_See: https://codechalleng.es/challenges/26/_

I have elected to try to produce some kind of GUI interface using the 
[pygame](https://www.pygame.org/) library.  I am aware that there are a number 
of GUIwidget packages already available, but my desire to "reinvent the wheel" 
is as an educational exercise.

## Aim

My first aim is to draught out a minimal set of useful widgets, building a 
hierarchy of common Python classes to represent the different items.

## Process

All visible elements of a GUI are built upon the foundation of a base 
component that provides a skeleton of parameters to define the area limits of 
screen real-estate that are available to a component.

The definition of a `BaseComponent` impacts the whole of the allowable 
interaction of a GUI and so this would seem to be the most obvious first step.

The most basic GUI element is the screen rectangle, or `panel`. This has a few 
properties beyond those of the base class, including the visible aspects of 
how the panel should be represented and the first suggestions of interactions
by the mouse within the environment.
 
A specialisation of the `panel` component is the `button`. The button has a
number of predefined property values as well as the clear intention of 
invoking interaction with a mouse. The properties are already defined within
the `panel` component and so have little difference on the surface, however, 
a `button` has built in responses to demonstrate, for example, a mouse click
being acknowledged.

# Component properties
## BaseComponent
### Inheritance

`Object` -> `BaseComponent`

### Positional properties

- `left` : int
- `top` : int
- `width` : int
- `height` : int
  - together these properties comprise the `area`

### Visual properties

- `visible` : bool
- `disabled` : bool

### Non-visual properties

- `name` : str

## Panel
### Inheritance

`BaseComponent` -> `Panel`

### Visual properties

- `colour` : tuple(byte, byte, byte)
- `border` : bool
- `border_colour` : tuple(byte, byte, byte)
- `text` : str
- `alignment` : tuple(Enum(left, centre, right), Enum(top, middle, bottom))

### Non-visual properties

- `onClick` : Callable[]
- `onMouseDown` : Callable[]
- `onMouseOver` : Callable[]
- `onMouseUp` : Callable[]

## Button
### Inheritance

`BaseComponent` -> `Panel` -> `Button`

