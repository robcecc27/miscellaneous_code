# module: acc.py

import codecs
import configparser
import os
from tkinter import *
from tkinter import messagebox


class AccountWindow(Tk):
    def __init__(self):
        super().__init__()
        self.config = configparser.ConfigParser()
        head, _ = os.path.split(__file__)
        path_ = os.path.normpath(os.path.join(head, 'config.ini'))
        with codecs.open(path_, 'r', 'utf8') as f:
            self.config.read_file(f)

        self.title(self.config.get('GUI Account', 'title'))
        self.option_add('*tearOff', False)
        self.name = 'account window'

        menubar = Menu(self, name='account menubar')
        self['menu'] = menubar
        menu_help = Menu(menubar, name='help menu')
        menu_help.add_command(
            label=self.config.get('GUI Account', 'help help'),
            command=self.help_)
        menu_help.add_command(
            label=self.config.get('GUI Account', 'help about'),
            command=self.about)
        menubar.add_cascade(
            menu=menu_help,
            label=self.config.get('GUI Account', 'menu help'))

    def help_(self):
        title = self.config.get('GUI Help', 'title')
        message = self.config.get('GUI Help', 'message')
        messagebox.showinfo(title, message, icon='question', parent=self)

    def about(self):
        title = self.config.get('GUI About', 'title')
        message = self.config.get('GUI About', 'message')
        messagebox.showinfo(title, message, parent=self)


def main():
    app = AccountWindow()
    app.mainloop()

if __name__ == '__main__':
    sys.exit(main())


######################################################################


######################################################################
