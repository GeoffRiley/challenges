## PyBites Python Code Challenge 26: Create a Simple Python GUI

See: https://codechalleng.es/challenges/26/

I have elected to try to produce some kind of GUI 
interface using the [pygame](https://www.pygame.org/) 
library.  I am aware that there are a number of GUI
widget packages already available, but my desire to 
'reinvent the wheel' is as an educational exercise.

### Aim

My first aim is to draught out a minimal set of useful
widgets, building a hierarchy of common Python classes
to represent the different items.

### Process

The most basic GUI element is the screen rectangle, or 
`panel`. All visible elements of a GUI are build upon the 
foundation of a panel and so this would seem to be the
most obvious first step.

## Component properties
### Panel
Positional properties

- `Left` : int
- `Top` : int
- `Width` : int
- `Height` : int

Visual properties

- `Visible` : bool
- `Border` : bool
- `Background-Colour` : tuple(byte, byte, byte)
- `Border-Colour` : tuple(byte, byte, byte)
