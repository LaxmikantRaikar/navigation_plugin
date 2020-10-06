from qgis.PyQt.QtCore import Qt, QTimer, QUrl
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QMenu, QApplication
from qgis.core import *
import os
from qgis.utils import iface



class ForRev:


    def __init__(self, iface):
        self.iface = iface
        self.canvas = iface.mapCanvas()
        self.toolbar = self.iface.addToolBar('Forward reverse Toolbar')
        self.toolbar.setObjectName('ForrevToolsToolbar')

    def initGui(self):
        #create toolbar buttons
        icon = QIcon(os.path.dirname(__file__) + "/images/for.png")
        self.farAction = QAction(icon, "Forward one feature", self.iface.mainWindow())
        #add shortcut to button
        self.iface.registerMainWindowAction(self.farAction, "right")
        self.farAction.setObjectName('forwardtool')
        # set action for button click does not needed
        self.farAction.triggered.connect(self.forward)
        #self.farAction.setCheckable(True)
        self.toolbar.addAction(self.farAction)
        self.iface.addPluginToMenu("Forward reverse Toolbar", self.farAction)



        icon = QIcon(os.path.dirname(__file__) + "/images/rev.png")
        self.revAction = QAction(icon, "Reverse one feature", self.iface.mainWindow())
        #add shortcut to button
        self.iface.registerMainWindowAction(self.revAction, "left")
        self.revAction.setObjectName('reversetool')
        self.revAction.triggered.connect(self.reverse)
        #self.revAction.setCheckable(True)  does not needed
        # set action for button click
        self.toolbar.addAction(self.revAction)
        self.iface.addPluginToMenu("Forward reverse Toolbar", self.revAction)


        icon = QIcon(os.path.dirname(__file__) + "/images/sett.png")
        self.settAction = QAction(icon, "Settings", self.iface.mainWindow())
        self.settAction.setObjectName('settings')
        self.settAction.triggered.connect(self.sett)
        # set action for button click
        self.toolbar.addAction(self.settAction)
        self.iface.addPluginToMenu("Forward reverse Toolbar", self.settAction)




    def unload(self):
        '''Unload plugin from the QGIS interface'''

        self.iface.removePluginMenu('Forward reverse Toolbar', self.farAction)
        self.iface.removePluginMenu('Forward reverse Toolbar', self.revAction)
        self.iface.removePluginMenu('Forward reverse Toolbar', self.settAction)

        # Remove Toolbar Icons
        self.iface.removeToolBarIcon(self.farAction)
        self.iface.removeToolBarIcon(self.revAction)
        self.iface.removeToolBarIcon(self.settAction)


        self.iface.unregisterMainWindowAction(self.farAction)
        self.iface.unregisterMainWindowAction(self.revAction)

        del self.toolbar

    def sett(self):
        self.iface.messageBar().pushMessage("Settings add")


    def forward(self):
        layer = iface.activeLayer()
        count = layer.selectedFeatureCount()
        selection = layer.selectedFeatures()

    try:
        if count == 1:
            for feature in selection:
                cur_id = feature.id()
                print(cur_id)
                cur_id = cur_id+1
                layer.removeSelection()
                layer.select(cur_id)
                iface.actionZoomToSelected().trigger()


        else:
                self.iface.messageBar().pushMessage("Select one vector feature")
    except:
            self.iface.messageBar().pushMessage("Reached First object")



    def reverse(self):
        layer = iface.activeLayer()
        count = layer.selectedFeatureCount()
        selection = layer.selectedFeatures()
        try:
            if count == 1:
                for feature in selection:

                    cur_id = feature.id()
                    print(cur_id)
                    cur_id = cur_id-1
                    layer.removeSelection()

                    layer.select(cur_id)
                    iface.actionZoomToSelected().trigger()


            else:
                self.iface.messageBar().pushMessage("Select one vector feature")
        except:
            self.iface.messageBar().pushMessage("Reached Last object")


