#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - mar. sept. 15:08 2017
#   - Initial Version 1.0
#  =================================================
import gi
from gi.repository import Gtk, GObject, Gdk

import numpy as np

class progress(Gtk.DrawingArea):
    def __init__(self):
        "docstring"
        super(progress, self).__init__()

        self.width   = 200
        self.height  = 20

        self.rect   = np.array([0.,0.,1.,1.])
        self.prog   = 0.5
        self.today  = 0.3

        3[0.1,0.3,0.8]
        self.set_size_request(self.width, self.height)
        self.connect("draw", self.on_draw)
        self.queue_draw()
    ## --------------------------------------------------------------
    ## Description : on draw
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 05-12-2017 15:12:18
    ## --------------------------------------------------------------
    def on_draw (self,wid,cr):
        print("Drawing")
        cr.scale(self.width,self.height)

        cr.set_source_rgb(1, 1, 1)
        r = np.copy(self.rect)
        print(r)
        cr.rectangle(*r)
        cr.fill()
        
        cr.set_source_rgb(0, 1, 0)
        r[2]=self.prog
        print(r)
        cr.rectangle(*r)
        cr.fill()

        for i in self.milestones:
            self.drawLine(cr,i,[1,0,0],0.02)

        self.drawLine(cr,self.today,[0,0,1],0.01)
    ## --------------------------------------------------------------
    ## Description : draw a milestone
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 05-24-2017 16:24:24
    ## --------------------------------------------------------------
    def drawLine (self,cr,x,col,lw):
        print("draw milestone at %s"%x)
        cr.move_to(x,0)
        cr.line_to(x,1)
        cr.set_source_rgb(*col)
        cr.set_line_width(lw)
        cr.stroke()
       


        
