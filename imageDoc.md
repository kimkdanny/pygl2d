# pygl2d.image #

The Image object for PyGL2D allows you to load images and draw them. It also lets you perform transformations, such as scaling, rotating, and coloring. Remember when drawing the image that (0, 0) is the topleft corner of the screen.

## Image(object): ##


### init(filename) <- return None ###

Initialise the Image. filename should be a path to the image file. Note that it CAN also be a pygame Surface.

### delete() <- return None ###

Delete the image from memory, including it's OpenGL texture.

### draw(pos) <- return None ###

Draws the image to the main screen at pos. Currently does not support drawing to other images.

### scale(scale) <- return None ###

Scale the image where 1.0 is the image's default size.

### rotate(rotation) <- return None ###

Rotate the image to the angle (rotation) given in degrees.
e.g. `image.scale(45)`

### colorize(r, g, b, a) <- return None ###

Color the image on an RGBA scale of 0-255. If you want to make your image transparent, use the "a" value.

### get\_width(self) <- return int ###

Returns the width of the original image. Does not provide alterations when the image is rotated, but it does support alterations in scaling.

### get\_height(self) <- return int ###

Functions the same as get\_width(), only it returns the image's height instead of width

### get\_rect(self) <- return rect.Rect ###

Returns a rect the size of the image.