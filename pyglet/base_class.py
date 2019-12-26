import pyglet
from pyglet.window import key
from pyglet.gl import *


class Window(pyglet.window.Window):
	def __init__(self, *args, **kwargs):
		super(Window, self).__init__()

	def on_draw(self):
		glClear(GL_COLOR_BUFFER_BIT)
		glLoadIdentity()
		glBegin(GL_TRIANGLES)
		glVertex2f(0, 0)
		glVertex2f(10, 0)
		glVertex2f(10, 10)
		glEnd()
	
	def on_key_press(self, symbol, modifiers):
		if symbol == key.ESCAPE:
			print('cool')
			pass
			#return pyglet.event.EVENT_HANDLED


if __name__ == "__main__":
	window = Window()
	pyglet.app.run()
