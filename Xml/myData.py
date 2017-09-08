#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - mer. sept. 13:06 2017
#   - Initial Version 1.0
#  =================================================
import xml.etree.ElementTree as et

class myData:
    def __init__(self, args):
        "docstring"
        self.tree = et.parse(args["path"])
        self.root = self.tree.getroot()
    ## --------------------------------------------------------------
    ## Description : get all projects
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 06-08-2017 13:08:17
    ## --------------------------------------------------------------
    def Projects (self):
       return self.root.iter("Project")
    ## --------------------------------------------------------------
    ## Description : get an attribute from an element
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 06-21-2017 13:21:57
    ## --------------------------------------------------------------
    def get (self,e,a):
        return e.get(a)
