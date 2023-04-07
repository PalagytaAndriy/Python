from abc import ABC, abstractmethod


class Text:
    def __init__(self):
        self.text = ''

    def __str__(self):
        return self.text


class Logic:
    @staticmethod
    def save(string):
        new_st = input('Write what you want to save: ')
        string.text += new_st
        return new_st

    @staticmethod
    def delete(string):
        string.text = ''


class ICommand(ABC):
    @staticmethod
    @abstractmethod
    def execute() -> None:
        """execut command"""


class SaveCommand(ICommand):
    def __init__(self, logic, text: Text) -> None:
        self._logic = logic
        self._text: Text = text

    def execute(self) -> None:
        print(f'SaveCommand -> save {self._logic.save(self._text)}')


class DeleteCommand(ICommand):
    def __init__(self, logic, text: Text) -> None:
        self._logic = logic
        self._text: Text = text

    def execute(self) -> None:
        print(f'DeleteCommand -> delete {self._text.text}')
        self._logic.delete(self._text)


class Invoker:

    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
        else:
            print(f'Unknow command - {command_name}')


t = Text()
save = SaveCommand(Logic, t)
delete = DeleteCommand(Logic, t)
# client
save.execute()
print(f'Class Text -> {t}')
delete.execute()
print(f'Class Text -> {t}')


# invoker
invok = Invoker()
invok.register('save', save)
invok.register('delete', delete)

invok.execute('save')
print(f'Class Text -> {t}')
invok.execute('delete')
print(f'Class Text -> {t}')