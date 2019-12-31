import pyglet
from pyglet.window import key
from pyglet.gl import *


class Window(pyglet.window.Window):
	def __init__(self, *args, **kwargs):
		super(Window, self).__init__()
		self.batch = pyglet.graphics.Batch()
		self.vertex_list = self.batch.add(4, pyglet.gl.GL_QUADS, None,
						  ('v2i', [200, 200, 300, 200, 300, 100, 200, 100]),
						  ('c4B', [200, 200, 220, 255] * 4))

	def on_draw(self):
		pyglet.gl.glClearColor(1,1,1,1)
		self.clear()
		self.batch.draw()
	
	def on_key_press(self, symbol, modifiers):
		if symbol == key.ESCAPE:
			pass
			# This line will prevent the ESCAPE key from closing window						  
			# return pyglet.event.EVENT_HANDLED


if __name__ == "__main__":
	window = Window()
	pyglet.app.run()
