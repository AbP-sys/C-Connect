"""
Driver code. Execution starts from here
"""
from gui import StudentLogin
from tkinter import *

window = Tk()
window.title('C-Connect')
window.geometry("411x891")
window.configure(bg = "#FFFFFF")
auth = StudentLogin.portal(window)
