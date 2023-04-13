from pywinauto.application import Application

notepad=Application(backend='uia').start(r"C:\WINDOWS\system32\notepad.exe").connect(title='Untitled - Notepad',timeout=20)

notepad.UntitledNotepad.print_control_identifiers()

formatMenu=notepad.UntitledNotepad.child_window(title="Format", control_type="MenuItem")

formatMenu.click_input()

print('-----------------------------')

notepad.UntitledNotepad.print_control_identifiers()

# ctrl+a + backspace (para apagar o que está escrito no campo)
# nameBox.type_keys('^a{BACKSPACE}')