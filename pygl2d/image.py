#PyGL2D - A 2D library for PyGame and PyOpenGL
#Copyright (C) 2008 - PyMike

from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

import rect, window

#Thanks Ian Mallett!
def Texture(surface,filters):
    texture = glGenTextures(1)
    Data = pygame.image.tostring(surface,"RGBA",1)
    
    glBindTexture(GL_TEXTURE_2D,texture)
    glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,surface.get_width(),surface.get_height(),0,GL_RGBA,GL_UNSIGNED_BYTE,Data)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    
    if filters == None:
        return texture
    
    for f in filters:
        if f == "filter":
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        elif f == "wrap":
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        elif f == "mipmap":
            glTexEnvf( GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE )
            gluBuild2DMipmaps(GL_TEXTURE_2D,3,surface.get_width(),surface.get_height(),GL_RGB,GL_UNSIGNED_BYTE,Data)
            if "filter" in filters:
                glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
                glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            else:
                glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
                glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    return texture

#Again, thanks Ian :)
class Image:
    
    def __init__(self, filename, filters=["filter"]):
        """Load an image for drawing. <- return None
        """
        
        #load pygame image
        if type("") is type(filename):
            image = pygame.image.load(filename)
        else:
            image = filename
        self.image = image
        
        #convert to GL texture
        self.texture = Texture(image, filters)
        
        #image dimensions
        self.width = self.w = image.get_width()
        self.height = self.h = image.get_height()
        self.size = image.get_size()
        self.win_size = window.get_size()
        
        #image mods
        self.rotation = 0
        self.scalar = 1.0
        self.color = [1.0, 1.0, 1.0, 1.0]
        self.ox, self.oy = self.image.get_width()/2, self.image.get_height()/2
        
        #crazy gl stuff :)
        self.dl = glGenLists(1)
        glNewList(self.dl, GL_COMPILE)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glBegin(GL_QUADS)
        glTexCoord2i(0, 0); glVertex3f(-self.width/2.0,-self.height/2.0,0)
        glTexCoord2i(1, 0); glVertex3f( self.width/2.0,-self.height/2.0,0)
        glTexCoord2i(1, 1); glVertex3f( self.width/2.0, self.height/2.0,0)
        glTexCoord2i(0, 1); glVertex3f(-self.width/2.0, self.height/2.0,0)
        glEnd()
        glEndList()
    
    def delete(self):
        glRemoveTextures([self.texture])
        del self
   
    def scale(self, scale):
        """Scale the image on a ratio of 0.0 to 1.0 <- return None
        """
        
        self.scalar = scale
    
    def rotate(self, rotation):
        """Rotate the image on a ratio of 0.0 to 360 <- return None
        """
        
        self.rotation = rotation
    
    def colorize(self, r, g, b, a):
        """Color an image on a RGBA (0-255) scale. <- return None
        """
        
        self.color = (r/255.0, g/255.0, b/255.0, a/255.0)
    
    def get_width(self):
        """Returns the width of the image. <- return int
        """
        
        return self.image.get_width()*self.scalar
    
    def get_height(self):
        """Returns the height of the image. <- return int
        """
        
        return self.image.get_height()*self.scalar
    
    def get_rect(self):
        """Get the rect of the image. <- return rect.Rect
        """
        
        return rect.Rect(0, 0, self.get_width(), self.get_height())
        
    def draw(self, pos):
        """Draw the image to a certain position <- return None
        """
        
        glPushMatrix()
        #print pos[0]+self.ox, self.win_size[1] - pos[1] - self.oy
        glTranslatef(pos[0]+self.ox, self.win_size[1] - pos[1] - self.oy, 0)
        glColor4f(*self.color)
        glRotatef(self.rotation, 0, 0, 1)
        glScalef(self.scalar, self.scalar, self.scalar)
        glCallList(self.dl)
        glPopMatrix()
