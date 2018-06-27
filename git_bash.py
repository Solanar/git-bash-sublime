import os
from os import path

import sublime
import sublime_plugin


# https://stackoverflow.com/questions/17085438/open-folder-in-git-bash-with-sublime-text-2-on-windows
class GitBashCommand(sublime_plugin.WindowCommand):
    def run(self, **args):
        # https://github.com/wbond/sublime_terminal
        if 'paths' in args:
            dir_ = args['paths'][0]
        else:
            if (
                self.window.active_view() and
                self.window.active_view().file_name()
            ):
                dir_ = self.window.active_view().file_name()
            elif self.window.folders():
                dir_ = self.window.folders()[0]
            else:
                sublime.error_message('No place to open Git Bash to')

                return

        if path.isfile(dir_):
            dir_ = path.dirname(dir_)

        os.chdir(path.abspath(dir_))

        # TODO make this a parameter
        git = 'C:\\Program Files\\Git\\git-bash.exe'
        if not path.isfile(git):
            sublime.error_message('Could not locate: {}'.format(git))

            return

        # TODO support other platforms
        # use start to prevent sublime from waiting
        # use "" to prevent extra empty cmd window
        # https://stackoverflow.com/questions/5909012/windows-batch-script-launch-program-and-exit-console
        os.system('start "" "{}"'.format(git))

        # this works but doesn't give focus to git-bash / UAC alert
        # self.window.run_command(
        #     'exec',
        #     {
        #         'cmd': ['C:\\Program Files\\Git\\git-bash.exe'],
        #         'shell': True,
        #         'working_dir': dir_,
        #     }
        # )

        # hide sublime output, seems to not be needed
        # self.window.run_command('hide_panel', {'panel': 'output.exec'})
