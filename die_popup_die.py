import os
import signal
import sublime
import sublime_plugin
from time import sleep
import subprocess, shlex

class StopAnnoyingMe(sublime_plugin.EventListener):
    def run(self, edit):
        pass

    def on_post_save_async(self, view):
        command = "wmctrl -lx"
        command = shlex.split(command)
        p = subprocess.Popen(command, stdout=subprocess.PIPE)
        out, err = p.communicate()
        out = out.splitlines()
        for w in out:
            w = str(w)
            # Search only for windows with the sublime WM class!
            w = w.split()
            if len(w) == 5 and w[2] == "sublime_text.Sublime_text" and w[4] == "'":
                # DIE POPUP!
                command = "wmctrl -ic " + w[0][2:]
                command = shlex.split(command)
                subprocess.Popen(command)
                print(command)
                break;
