"""
deprecated.driver to run the application.
"""
import gui.build.connection as connection
import gui.build.login as login
import gui.build.mainmenu as mainmenu

def authenticate(un,pas):
    try:
        login.authentication(un, pas)
        user = login.fetchdetails(un)
        print(user.name + " " + user.branch)
        id = mainmenu.display(user)
        return 0
    except ValueError as excep:
        print(excep)
        return -1
