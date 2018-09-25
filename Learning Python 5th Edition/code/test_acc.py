# module: test_acc.py

import unittest
import unittest.mock

import acc


class TestAccountWindow(unittest.TestCase):
    HELP_HELP = 'Help help'
    HELP_ABOUT = 'Help about'

    def setUp(self):
        self.config = ['',  # __init__() config calls, Window title.
                       self.HELP_HELP,  # Help menu item
                       self.HELP_ABOUT,  # About menu item
                       '']  # Help menu

    def test_menu_help_item_help(self):
        self.messagebox_helper(self.HELP_HELP, icon='question')

    def test_menu_help_item_about(self):
        self.messagebox_helper(self.HELP_ABOUT)

    @unittest.mock.patch('acc.configparser.ConfigParser.get', autospec=True)
    @unittest.mock.patch('acc.messagebox.showinfo', autospec=True)
    def messagebox_helper(
            self, menu_item, mock_messagebox, mock_get_value, **kwargs):
        self.config += ['title',  # app.messagebox config calls
                        'message']
        mock_get_value.side_effect = self.config
        app = acc.AccountWindow()
        app.children['account menubar'].children['help menu'].invoke(menu_item)
        mock_messagebox.assert_called_with(self.config[-2],
                                           self.config[-1],
                                           parent=app, **kwargs)
