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

from Project import Project
from dayTask import dayTask

class mainWindow(Gtk.Window):
    __gsignals__ = {'taskSelected': (GObject.SIGNAL_RUN_FIRST, None, (GObject.GObject,)) }
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
        p = Project(args)
        p.connect("taskSelected",self.taskSelected)
        self.builder.get_object("container").pack_end(p, True, True, 0)
        p.show()
        return p
    ## --------------------------------------------------------------
    ## Description : task selected
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 13-04-2017 19:04:40
    ## --------------------------------------------------------------
    def taskSelected (self,t,t2):
        print("Main : task selected : %s"%(t2.title))
        dt = dayTask(t2)
        self.builder.get_object("dayBox").pack_end(dt.main, True, True, 0)
        
        dt.main.show()
        
