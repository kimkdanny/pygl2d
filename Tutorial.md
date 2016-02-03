# Tutorial for PyGL2D #

This tutorial shows how to use the basics of PyGL2D.

## Step 1: Importing ##

Place the folder containing the pygl2d library (pygl2d/pygl2d) in your game directory. Then in the top of your game file type

```
import pygl2d
```

Run the script, and if you get no tracebacks, it worked =)

## Step 2: Setting up the Window ##

After you import pygl2d, type this line in.

```
pygl2d.window.init((640, 480), caption="My Cool Game")
```

Voila! That's all you need to do to setup the window. The first value, (640, 480), is the screen dimensions. The second value, "My Cool Game", is the caption for the window.

## Step 3: Drawing Images ##

This step is a bit longer. After you setup the window, put some random image in the same dir as your game file. Then call:

```
image = pygl2d.image.Image(yourimagefilename)
```

And you just loaded an image! Huzzah! Now let's create a loop.

```
running = 1
while running:

    for e in pygame.event.get():
        if e.type == QUIT:
            running = 0
        if e.type == KEYDOWN and e.key == K_ESCAPE:
            running = 0
```

Okay, awesome! We have a loop that will quit if you press the X or Escape button. Now we can draw the images

Under the event loop, add

```
    #Call this before you begin drawing with pygl2d
    pygl2d.window.begin_draw()

    #Draw the image!
    image.draw([0, 0])

    #Call this after you finish drawing with pygl2d
    pygl2d.window.end_draw()
```

And there you have it! When you run this script you should see an image being drawn on the screen. See the docs/ for image transformations, primitives drawing, and more!