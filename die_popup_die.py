import sublime
import sublime_plugin
from time import sleep
import os, signal

class StopAnnoyingMe(sublime_plugin.EventListener):
    def run(self, edit):
        w = sublime.windows()
        for i in w:
            print(len(i.views()))
        #print(w)

    def on_post_save_async(self, view):
        #sleep(5)
        w = sublime.windows()
        print("Activated!!")
        for i in w:
            print(i.id())
