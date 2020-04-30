"""
window
====================================================================================================

Drawing the application window

----------------------------------------------------------------------------------------------------

**Created**
    2020-04-30
**Author**
    Ben Croisdale
**Copyright**
    This software is Free and Open Source for any purpose
"""

import pyglet


class Application:
    """ Core application manager (TODO, pull this out once the project grows """

    def __init__(self, config={}):
        self._config: dict = config
        self._window = ApplicationWindow(self)

    def run(self):
        """ Begin running the application """
        pyglet.app.run()


class ApplicationWindow(pyglet.window.Window):
    """ Pybench core window """

    def __init__(self, app: Application, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._app: Application = app
        self._label = pyglet.text.Label("Test window")

    def on_draw(self):
        self.clear()
        self._label.draw()


if __name__ == "__main__":
    app = Application()
    app.run()
