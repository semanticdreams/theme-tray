
#!/usr/bin/env python3
import sys
import os
import subprocess
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Qt


class ThemeTray(QSystemTrayIcon):
    def __init__(self, icon_path):
        super().__init__(QIcon(icon_path))

        # Track theme state
        self.dark_mode = False

        # Tooltip
        self.setToolTip("Click to toggle light/dark mode")

        # --- Context menu ---
        self.menu = QMenu()
        quit_action = QAction("Quit", self.menu)
        quit_action.triggered.connect(QApplication.quit)
        self.menu.addAction(quit_action)
        self.setContextMenu(self.menu)

        # --- Connect signals ---
        self.activated.connect(self.on_activated)

        self.show()

    def on_activated(self, reason):
        # Trigger (left click): toggle theme
        # Context (right click): handled by system tray automatically
        if reason == QSystemTrayIcon.Trigger:
            self.toggle_theme()
        elif reason == QSystemTrayIcon.Context:
            # Explicitly show the menu (needed for XFCE)
            self.menu.popup(self.geometry().center())

    def toggle_theme(self):
        if self.dark_mode:
            subprocess.run([
                "bash", "-c",
                "gsettings set org.gnome.desktop.interface color-scheme 'prefer-light' && "
                "xfconf-query -c xsettings -p /Net/ThemeName -s 'Greybird'"
            ])
            self.setToolTip("Light mode active (click to switch to dark)")
            self.dark_mode = False
        else:
            subprocess.run([
                "bash", "-c",
                "gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark' && "
                "xfconf-query -c xsettings -p /Net/ThemeName -s 'Greybird-dark'"
            ])
            self.setToolTip("Dark mode active (click to switch to light)")
            self.dark_mode = True


def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    icon_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'icon.png')

    tray = ThemeTray(icon_path)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
