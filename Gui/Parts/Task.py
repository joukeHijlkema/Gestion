#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - jeu. sept. 17:53 2017
#   - Initial Version 1.0
#  =================================================

import gi
from gi.repository import Gtk, GObject, Gdk

import arrow

class Task(GObject.GObject):
    __gsignals__ = {'taskSelected': (GObject.SIGNAL_RUN_FIRST, None, (GObject.GObject,)) }
    def __init__(self,t):
        "docstring"
        super(Task, self).__init__()

        args = t.attrib
        print(args)
        
        self.title = args["title"] if "title" in args else "title"
        self.project = args["project"] if "project" in args else "project"

        self.builder  = Gtk.Builder()
        self.builder.add_from_file("./Gui/Parts/Task.glade")
        
        self.main = self.builder.get_object("main")
        self.main.set_label(self.title)

        self.subTasks = self.builder.get_object("subMain")

        self.part = self.builder.get_object("partValue")
        self.part.set_value(int(args["part"]))
        self.done = self.builder.get_object("doneValue")
        self.done.set_value(int(args["done"]))

        for s in t.findall("Task"):
            self.addSubTask(s)
            
        handlers      = {
            "taskTodayButton":self.selectTask
        }
        self.builder.connect_signals(handlers)

    ## --------------------------------------------------------------
    ## Description : add a subTask
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 13-31-2017 18:31:39
    ## --------------------------------------------------------------
    def addSubTask(self,s):
        print(s.attrib)
        s.attrib["project"]=self.project
        nt = Task(s)
        nt.connect("taskSelected",self.selectTask)
        self.subTasks.pack_end(nt.main, True, True, 0)
    ## --------------------------------------------------------------
    ## Description : task selected
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 13-59-2017 18:59:58
    ## --------------------------------------------------------------
    def selectTask (self,sender,*origin):
        if origin:
            self.emit('taskSelected',origin[0])
        else:
            self.emit('taskSelected',self)
  
            
