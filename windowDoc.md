# pygl2d.window #

PyGL2D's window module is for setting up the window for drawing.

### window.init(size, caption="PyGL2D Window", flags=DOUBLEBUF) ###

Initialise the SDL/PyGame window. `caption` is the window caption. `flags` can be extra pygame flags, such as `HWSURFACE`, `FULLSCREEN`, etc. Note that these are pygame variables, and to use them you need to import pygame.

### window.begin\_draw() ###

Call this right before you begin drawing your objects. If you don't, then you won't see anything!

### window.end\_draw() ###

And always call this after you're done drawing, or else you'll get some crazy GL errors.