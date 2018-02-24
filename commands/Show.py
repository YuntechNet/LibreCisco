from commands.Command import Command
from enums.SwitchMode import SwitchMode

class Show(Command):
    
    reg = '^(show)'
    mode = SwitchMode.ENABLE

    def __init__(self, args=None):
        super().__init__()
        self.name = 'show'
        self.args = args
