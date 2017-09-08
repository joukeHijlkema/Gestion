#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - mer. sept. 15:07 2017
#   - Initial Version 1.0
#  =================================================

import gi
from gi.repository import Gtk, GObject, Gdk

import arrow

class Milestone:
    def __init__(self, args):
        "docstring"
        self.date   = arrow.get(args["date"],"DD/MM/YYYY") if "date" in args else arrow.now()
        self.title  = args["title"] if "title" in args else "title"
        self.done   = args["done"]=="True" if "done" in args else False
        self.type   = args["type"] if "type" in args else "?"
        
        # print("Milestone %s"%self.title.encode('utf-8'))

        self.builder  = Gtk.Builder()
        self.builder.add_from_file("./Gui/Parts/Milestone.glade")

        self.main        = self.builder.get_object("main")
        self.dateEntry   = self.builder.get_object("date")
        self.cal         = self.builder.get_object("cal")
        self.calendar    = self.builder.get_object("calendar")
        self.doneButton  = self.builder.get_object("done")

        handlers      = {
            "onDateClick": self.dateClick,
            "cancelButtonClicked": self.Cancel,
            "okButtonClicked": self.OK,
            "daySelected": self.OK
        }

        self.builder.connect_signals(handlers)

        self.main.set_label(self.title)
        self.dateEntry.set_text(self.date.format("DD/MM/YYYY"))
        self.calendar.select_month(self.date.timetuple().tm_mon-1,self.date.timetuple().tm_year)
        self.calendar.select_day(self.date.timetuple().tm_mday)
        self.doneButton.set_active(self.done)
    ## --------------------------------------------------------------
    ## Description : when date gets clicked
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 06-39-2017 15:39:22
    ## --------------------------------------------------------------
    def dateClick (self,*args):
        if args[1].state & Gdk.ModifierType.SHIFT_MASK and args[1].button==1:
            # print("select date")
            d = self.cal.run()
    ## --------------------------------------------------------------
    ## Description : OK button clicked
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 06-18-2017 17:18:27
    ## --------------------------------------------------------------
    def OK (self,args):
        print("OK")
        d = self.calendar.get_date()
        self.date = arrow.get("%02d/%02d/%04d"%(d.day,d.month+1,d.year),"DD/MM/YYYY")
        self.dateEntry.set_text(self.date.format("DD/MM/YYYY"))
        self.cal.response(1)
        self.cal.hide()
    ## --------------------------------------------------------------
    ## Description : cancle button clicked
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 06-18-2017 17:18:55
    ## --------------------------------------------------------------
    def Cancel (self,args):
        print("Cancel")
        self.cal.set_visible("False")
        self.cal.hide()
