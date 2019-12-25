import pyglet
from pyglet.window import key

config = pyglet.gl.Config(samples=4)
window = pyglet.window.Window(config=config)

label = pyglet.text.Label('Hello, world', font_name='Times New Roman', font_size=36,
							x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')

@window.event
def on_draw():
	label.draw()
	
@window.event
def on_key_press(symbol, modifiers):
	if symbol == key.ESCAPE:
		#Escape no longer closes the window
		return pyglet.event.EVENT_HANDLED

pyglet.app.run()
