from pywinauto.application import Application

# podemos usar apenas o metodo connect para nos conectarmos a algum programa que já esteja aberto, sem que tenha sido o python que o iniciou
# o timeout faz com que o comando aguarde aquele tempo para se conectar ao aplicativo ou quebra o programa
# podemos tambem startar o programa em um comando e depois nos conectarmos a ele com outro programa sem problema
notepad=Application(backend='uia').start(r"C:\WINDOWS\system32\notepad.exe").connect(title='Untitled - Notepad',timeout=20)

# o atributo utilizado 'UntitledNotepad' sera o titulo utilizado no comando para conectar ao app, retirando os espaços, retirando os caracteres especiais e colocando a primeira letra de cada palavra em maiuscula(?)
notepad.UntitledNotepad.print_control_identifiers()

formatMenu=notepad.UntitledNotepad.child_window(title="Format", control_type="MenuItem")

formatMenu.click_input()

print('-----------------------------')

notepad.UntitledNotepad.print_control_identifiers()

# ctrl+a + backspace (para apagar o que está escrito no campo)
# nameBox.type_keys('^a{BACKSPACE}')




# Simple Example
# It is simple and the resulting scripts are very readable. How simple?

# from pywinauto.application import Application
# app = Application().start("notepad.exe")

# app.UntitledNotepad.menu_select("Help->About Notepad")
# app.AboutNotepad.OK.click()
# app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)




# MS UI Automation Example
# More detailed example for explorer.exe:

# from pywinauto import Desktop, Application

# Application().start('explorer.exe "C:\\Program Files"')

# # connect to another process spawned by explorer.exe
# # Note: make sure the script is running as Administrator!
# app = Application(backend="uia").connect(path="explorer.exe", title="Program Files")

# app.ProgramFiles.set_focus()
# common_files = app.ProgramFiles.ItemsView.get_item('Common Files')
# common_files.right_click_input()
# app.ContextMenu.Properties.invoke()

# # this dialog is open in another process (Desktop object doesn't rely on any process id)
# Properties = Desktop(backend='uia').Common_Files_Properties
# Properties.print_control_identifiers()
# Properties.Cancel.click()
# Properties.wait_not('visible') # make sure the dialog is closed