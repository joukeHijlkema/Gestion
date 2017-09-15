#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - ven. sept. 14:18 2017
#   - Initial Version 1.0
#  =================================================

import gi
from gi.repository import Gtk, GObject, Gdk


class dayTask(GObject.GObject):
    __gsignals__ = {'taskDone': (GObject.SIGNAL_RUN_FIRST, None, (GObject.GObject,)) }
    def __init__(self,t):
        "docstring"
        self.task=t
        self.builder  = Gtk.Builder()
        self.builder.add_from_file("./Gui/Parts/dayTask.glade")
        
        self.main = self.builder.get_object("main")
        self.builder.get_object("Title").set_text("%s : %s"%(t.project,t.title))
        self.builder.get_object("done").set_value(t.done.get_value())
        
