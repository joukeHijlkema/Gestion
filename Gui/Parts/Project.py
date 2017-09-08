#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - mar. sept. 14:04 2017
#   - Initial Version 1.0
#  =================================================
import gi
from gi.repository import Gtk, GObject, Gdk

import arrow
from .Milestone import Milestone
from .Task import Task


class Project(Gtk.Box):
    ID = 0
    title=""
    def __init__(self, args):
        "the Project widget"
        super(Project, self).__init__(args)
        self.ID =Project.ID 
        Project.ID+=1
        print("new project ID=%s"%self.ID)

        self.builder  = Gtk.Builder()
        self.builder.add_from_file("./Gui/Parts/Project.glade")

        self.main          = self.builder.get_object("main")
        self.project       = self.builder.get_object("project")
        self.msFrame       = self.builder.get_object("msFrame")
        self.tskFrame      = self.builder.get_object("tskFrame")
        self.milestones    = self.builder.get_object("milestones")
        self.tasks         = self.builder.get_object("tasks")
        self.toggleButton  = self.builder.get_object("togglebutton")
        self.secondBox     = self.builder.get_object("secondBox")
        self.description   = self.builder.get_object("description")
        self.start         = self.builder.get_object("start")
        self.end           = self.builder.get_object("end")
        self.progress      = self.builder.get_object("progress")

        self.pack_start(self.builder.get_object("main"), True, True, 0)

        handlers      = {
            "onToggle": self.update,
            "onLabelChange": self.update,
            "cancelButtonClicked": self.Cancel,
            "okButtonClicked": self.OK,
            "newMilestoneClicked": self.newMilestone
        }

        self.builder.connect_signals(handlers)
        self.progress.connect("draw", self.on_draw)

        if "description" in args:
            self.description.set_text(args["description"])

        if "start" in args:
            self.startDate = arrow.get(args["start"],"DD/MM/YYYY")
        else:
            self.startDate = arrow.now()
        self.start.set_text(self.startDate.format("DD/MM/YYYY"))
            
        if "end" in args:
            self.endDate = arrow.get(args["end"],"DD/MM/YYYY")
        else:
            self.startDate = arrow.now().shift(days=+1)
        self.end.set_text(self.endDate.format("DD/MM/YYYY"))

        self.today = self.relDate(arrow.now())
        self.milestoneList=[]
        self.taskList=[]
        self.update(None)

        # debug
        self.prog=0.6
    ## --------------------------------------------------------------
    ## Description : relative date
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 06-11-2017 15:11:40
    ## --------------------------------------------------------------
    def relDate (self,date):
        return (date-self.startDate)/(self.endDate-self.startDate)
    ## --------------------------------------------------------------
    ## Description : add a milestone
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 06-02-2017 15:02:31
    ## --------------------------------------------------------------
    def addMilestone (self,m):
        nm = Milestone(m)
        self.milestones.pack_start(nm.main, True, True, 0)
        self.milestoneList.append(nm)
        nm.main.show_all()
    ## --------------------------------------------------------------
    ## Description : new milestone
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 07-02-2017 15:02:10
    ## --------------------------------------------------------------
    def newMilestone (self,*args):
        res=self.builder.get_object("getTitle").run()
        if self.title!="":
            self.addMilestone({"title":self.title})
    ## --------------------------------------------------------------
    ## Description : add a task
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 07-51-2017 17:51:27
    ## --------------------------------------------------------------
    def addTask (self,t):
        nt = Task(t)
        self.tasks.pack_start(nt.main, True, True, 0)
        self.taskList.append(nt)
        nt.main.show_all()
    ## --------------------------------------------------------------
    ## Description : make a new Task
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 07-51-2017 17:51:52
    ## --------------------------------------------------------------
    def newTask (self,*args):
        res=self.builder.get_object("getTitle").run()
        if self.title!="":
            self.addTask({"title":self.title})
        
    ## --------------------------------------------------------------
    ## Description : update the Project
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 05-52-2017 14:52:39
    ## --------------------------------------------------------------
    def update (self,*args):
        # print("update with %s"%args)
        self.secondBox.set_visible(self.toggleButton.get_active())
        self.msFrame.set_visible(self.toggleButton.get_active())
        self.tskFrame.set_visible(self.toggleButton.get_active())
        self.project.set_label(self.description.get_text())
    ## --------------------------------------------------------------
    ## Description : on draw
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 05-12-2017 15:12:18
    ## --------------------------------------------------------------
    def on_draw (self,wid,cr):
        # print("Drawing")

        r = self.progress.get_allocation()
        cr.scale(r.width,r.height)

        cr.set_source_rgb(1, 1, 1)
        cr.rectangle(0,0,1,1)
        cr.fill()

        cr.set_source_rgb(0, 1, 0)
        cr.rectangle(0,0,self.prog,1)
        cr.fill()

        for i in self.milestoneList:
            self.drawLine(cr,self.relDate(i.date),[1,0,0],0.02)

        self.drawLine(cr,self.today,[0,0,1],0.01)
    ## --------------------------------------------------------------
    ## Description : draw a line
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 05-24-2017 16:24:24
    ## --------------------------------------------------------------
    def drawLine (self,cr,x,col,lw):
        # print("draw line at %s"%x)
        cr.move_to(x,0)
        cr.line_to(x,1)
        cr.set_source_rgb(*col)
        cr.set_line_width(lw)
        cr.stroke()
    ## --------------------------------------------------------------
    ## Description : OK button clicked
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 06-18-2017 17:18:27
    ## --------------------------------------------------------------
    def OK (self,args):
        print(args)
        print("OK")
        self.title=self.builder.get_object("titleEntry").get_text()
        self.builder.get_object("getTitle").response(1)
        args.get_window().hide()
    ## --------------------------------------------------------------
    ## Description : cancle button clicked
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 06-18-2017 17:18:55
    ## --------------------------------------------------------------
    def Cancel (self,args):
        print("Cancel")
        self.title=""
        self.builder.get_object("getTitle").response(0)
        args.get_window().hide()
    
