#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - mar. sept. 11:59 2017
#   - Initial Version 1.0
#  =================================================

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

from Gui.mainWindow import mainWindow
from Xml.myData import myData

db = myData({"path":"./test.xml"})

win = mainWindow()

for p in db.Projects():
    np = win.newProject(p.attrib)
    for m in p.iter("Milestone"):
        np.addMilestone(m.attrib)
    for t in p.findall("Task"):
        np.addTask(t.attrib)
        
    
Gtk.main()
