#!/bin/python3
"""
    GUI component: ControlComponent
    Abstract Base Class

    ## `ControlComponent`

    | Component     | `ControlComponent`    |
    | ------------- | --------------------- |--------
    | _Properties_  |                       |
    |               | `name` *              | `str`
    |               | `tag` *               | `ANY`
    |               | `area` *              | `Rect`
    |               | `visible` *           | `bool`
    |               | `disabled` *          | `bool`
    |
    | _Methods_     |                       |
    |               | `hide()` *            |
    |               | `show()` *            |
    |               | `disable()` *         |
    |               | `enable()` *          |
    |

    * Inherited

    ### Inheritance

    `BaseComponent` -> `GraphicalComponent` -> `ControlComponent` -> `ContainerComponent`
"""

from geoff_gui.control_component import ControlComponent


class ContainerComponent(ControlComponent):
    ...
