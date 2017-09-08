#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - mar. sept. 12:02 2017
#   - Initial Version 1.0
#  =================================================
import gi
from gi.repository import Gtk, GObject, Gdk

from .Parts.Project import Project

class mainWindow(Gtk.Window):
    def __init__(self, *args):
        "main window of the Gestion GUI"
        super(mainWindow, self).__init__()

        self.builder  = Gtk.Builder()
        self.builder.add_from_file("./Gui/Parts/mainWindow.glade")
        self.window   = self.builder.get_object("mainWindow")
        handlers      = {
            "onDeleteWindow": self.Quit,
            "onNewProject": self.newProject
        }

        self.builder.connect_signals(handlers)
 
        self.window.show_all()

    ## --------------------------------------------------------------
    ## Description : Quit
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 05-07-2017 12:07:54
    ## --------------------------------------------------------------
    def Quit (self,*args):
        print(args)
        Gtk.main_quit()
    ## --------------------------------------------------------------
    ## Description : add a new project
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 05-09-2017 14:09:08
    ## --------------------------------------------------------------
    def newProject (self,args):
        cont = self.builder.get_object("container")
        p = Project(args)
        cont.attach(p,0,p.ID,1,1)
        p.show()
        return p
