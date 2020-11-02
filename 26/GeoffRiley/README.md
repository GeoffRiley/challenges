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

A GUI comprises of many elementary components, both visible and invisible. The
visible components go towards creating a visual presentation, whilst the 
invisible components provide the necessary support and interconnections.

All components, whether visible or invisible, are built upon a single 
foundation component which provides a common base interface for all other
components.  This common base has the minimum amount of features that are 
found in both kinds of component.

Looking at the visible components, again there are two major types: purely
graphical and controlled graphical. Purely graphical elements have no user
interaction and are drawn (possibly influenced by various flags) as decoration.
Controlled graphical components, however, give rise to user interaction and
are either directly or indirectly influenced by user actions.

Controlled graphical components can also be subdivided into container and 
non-container. A container is able to hold other components—including other 
containers, whereas a non-container is a direct display element. A 
non-container is not necessarily a static element though as these are the 
workhorses through with user interaction is achieved. 

## Implementation

The common base element that everything else is built upon is `BaseComponent`.
The definition of the `BaseComponent` impacts every single other component
within the GUI definition, for this reason it has a bare minimum of 
functionality that will be shared.






The most basic GUI element is the screen rectangle, or `panel`. This has a few 
properties beyond those of the base class, including the visible aspects of 
how the panel should be represented, the area that it should occupy, its colour
and gives the first suggestions of interactions by accepting the mouse events 
within the limits of it's surface. The `panel` may contain other components, 
and and restricts those components to the limits of the defined area.

What would appear to be a specialisation of the `panel` component is the 
`button`. At first glance they resemble each other: both appear as a 
rectangular area and bother react to mouse clicks. However, unlike the `panel`, 
the `button` is not a container and is therefore not a descendent class. The 
`button` does have a number of predefined default property values, such as the 
size of the area covered by a `button` and the style of drawing with rounded
corners. It also has the clear intention of invoking interaction with a mouse. 

# Component properties
## `BaseComponent`

| Component | `BaseComponent` | |
| ---: | ---: | :--- |
| _Properties_
| | `name` | `str`
| | `tag` | `ANY`

### Inheritance

`Object` -> `BaseComponent`

### Properties

- `name` : str

All components should be assigned unique names.  This will allow a component
to be easily recognised, for example, during a debugging process.  Each 
component is created with a randomly unique name, but this should be set to
a logical name after creation. 

- `tag` : ANY

Every component has a `tag` associated with it. The tag has no system meaning
but is provided for end user defined purposed. The tag is never modified by 
the system during operation other than being set to the default of `None` upon
creation.

## `GraphicalComponent`

| Component | `GraphicalComponent` | |
| ---: | ---: | :--- |
| _Properties_
| | `area.left` | `int`
| | `area.top` | `int`
| | `area.width` | `int`
| | `area.height` | `int`
| | `visible` | `bool`
| _Methods_
| | `hide()`
| | `show()`

### Inheritance

`BaseComponent` -> `GraphicalComponent`

### Properties

- `area` : Rect

The `area` specified the position of this component within it's current
container. The minimum parameters required to describe an area are:

- `Rect`
    - `left` : int
    - `top` : int
    - `width` : int
    - `height` : int

> Note: `Rect` is defined in [pygame.Rect](https://www.pygame.org/docs/ref/rect.html).

- `visible` : bool

The `visible` property indicates whether the component should be drawn or not. 
It is modified by using the `hide()` and `show()` methods.

### Methods

- `hide()`
- `show()`

These two methods work in tandem to (a) modify the `visible` property and (b)
cause the component to either be hidden or shown as a consequence. No 
parameters are expected for either method.

## `ControlComponent`

| Component | `ControlComponent` | |
| ---: | ---: | :--- |
| _Properties_ |
| | `area` | `Rect`
| | `visible` | `bool`
| | `disabled` | `bool`
| _Methods_
| | `hide()`
| | `show()`
| | `disable()`
| | `enable()`

### Inheritance

`BaseComponent` -> `GraphicalComponent` -> `ControlComponent`

### properties

- `area` : Rect
- `visible` : bool

These properties are inherited directly from `GraphicalComponent`.

- `disabled` : bool

The `disabled` property indicated if this component is currently available for
interaction. When it is `False` then the component will ignore any attempted 
user interaction, when it is `True` then the component will respond.

It is normal for a disabled control to be displayed differently to an active
control.

## Methods

- `hide()`
- `show()`

These methods are inherited directly from `GraphicalComponent`.

- `disable()`
- `enable()`

The purpose of these two methods is to (a) modify the value of the `disabled`
property and (b) to trigger the change in operation of the component between
its inactive and active states.

## `ContainerComponent`

| Component | `ContainerComponent` | |
| ---: | ---: | :--- |
| _Properties_
| | `area` | `Rect`
| | `visible` | `bool`
| | `disabled` | `bool`
| |
| _Methods_
| | `hide()`
| | `show()`
| | `disable()`
| | `enable()`
| |

### Inheritance

`BaseComponent` -> `GraphicalComponent` -> `ControlComponent` -> `ContainerComponent`



## Panel
### Inheritance

`BaseComponent` -> `GraphicalComponent` -> `ControlComponent` -> `ContainerComponent` -> `Panel`

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

`BaseComponent` -> `GraphicalComponent` -> `ControlComponent` -> `Button`

### Visual properties

- `click_colour` : ColourValue
- `hover_colour` : ColourValue
- `button_colour` : ColourValue

## Label
### Inheritance

`BaseComponent` -> `GraphicalComponent` -> `Label`

