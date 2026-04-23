#Sistem Undo/Redo
class TextEditor:
    def __init__(self):
        self.content = ''
        self.undo_stack = []
    
    def write(self, text):
        self.undo_stack.append(self.content)
        self.content += text
        print(f'Tulis: {self.content}')
    
    def undo(self):
        if self.undo_stack:
            self.content = self.undo_stack.pop()
            print(f'Undo: {self.content}')
        else:
            print('Tiada yang bisa diundo Lagih.')

editor = TextEditor()
editor.write('Halo dunia')
editor.write("DUnia Jahat")
editor.write('!')
editor.undo()
editor.undo()
