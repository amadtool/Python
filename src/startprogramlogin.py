import win32api
import subprocess
import win32com.client
from pywinauto import mouse, keyboard
#from pywinauto.keyboard import send_keys
from pywinauto.application import Application
import sys
import os

program = r'C:\Program Files\Autodesk\Revit 2017\Revit.exe'

subprocess.Popen(
    [program], start_new_session=True
)
shell = win32com.client.Dispatch("WScript.Shell")
try:
	win32api.Sleep(6000)
	shell.SendKeys("ncongur@limak.com.tr")
	shell.SendKeys("{ENTER}")
	win32api.Sleep(3500)
	shell.SendKeys("Limak@123")
	shell.SendKeys("{ENTER}")
	app = Application().connect(title="Autodesk Revit 2017.2 - [Recent Files]", timeout=20)
	dlg=app['AdApplicationButton']
	dlg.click()
	dlg.wait('visible')
	app2 = Application().connect(title="Autodesk Revit 2017.2 - [Recent Files]", timeout=15)
	dlgx = app2['ApplicationMenuWindow']
	mouse.click(button='left', coords=(311, 598))
	app3 = Application().connect(title="Autodesk Revit 2017.2 - [Recent Files]", timeout=5)
	dlg3 = app3['Options']
	dlg3.SysLink.click()
	app4=Application().connect(path=r"C:\Program Files\Autodesk\Revit 2017\Revit.exe")
	dlg4 = app4['Sign in']
	dlg3.Edit.type_keys('^a{BACKSPACE}')
	keyboard.send_keys(os.getlogin())
	dlg3.Edit.type_keys('{ENTER}')
	dlg3.Edit.type_keys('{ESC}')
except:
	print(sys.exc_info()[0])
