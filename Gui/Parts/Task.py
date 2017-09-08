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

class Task:
    def __init__(self, args):
        "docstring"
        print(args)
        self.title = args["title"] if "title" in args else "title"

        self.builder  = Gtk.Builder()
        self.builder.add_from_file("./Gui/Parts/Task.glade")
        
        self.main = self.builder.get_object("main")
        self.main.set_label(self.title)
