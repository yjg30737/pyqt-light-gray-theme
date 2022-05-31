from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMenuBar, QToolButton

from qt_sass_theme_getter.qtSassThemeGetter import QtSassThemeGetter

t = QtSassThemeGetter()
t.setTheme('light')

def getThemeStyle() -> str:
    return t.getThemeStyle()

def getIconButtonStyle() -> str:
    return t.getIconButtonStyle()

def getIconTextButtonStyle() -> str:
    return t.getIconTextButtonStyle()

def getMenuBarStyle(menu_bar: QMenuBar) -> str:
    tool_button = menu_bar.findChild(QToolButton)
    tool_button.setArrowType(Qt.RightArrow)
    return t.getMenuBarStyle()

def getMainWidgetStyle() -> str:
    return t.getMainWidgetStyle()
