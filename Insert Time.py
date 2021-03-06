# -*- coding: utf-8 -*-

'''
:Title
Insert Time

:Planguage
Python

:Requires
VoodooPad 3.5+

:Description
Inserts Time

EOD
'''
VPScriptSuperMenuTitle = "GTD"
VPScriptMenuTitle = "Insert Time"
VPShortcutMask = "control"
VPShortcutKey = "M"

import AppKit
import time

def main(windowController, *args, **kwargs):
    textView = windowController.textView()
    document = windowController.document()

    if textView != None:
        dateFormat = time.strftime("%I:%M %p")
        textView.insertText_(dateFormat)

