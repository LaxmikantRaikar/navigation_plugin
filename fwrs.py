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
        self.toolbar = self.iface.addToolBar('Navigate Features Toolbar')
        self.toolbar.setObjectName('NavigateFeaturesToolbar')

    def initGui(self):
        #create toolbar buttons
        icon = QIcon(os.path.dirname(__file__) + "/images/for.png")
        self.farAction = QAction(icon, "Jump to next feature", self.iface.mainWindow())
        #add shortcut to button
        self.iface.registerMainWindowAction(self.farAction, "right")
        self.farAction.setObjectName('forwardtool')
        # set action for button click does not needed
        self.farAction.triggered.connect(self.forward)
        #self.farAction.setCheckable(True)
        self.toolbar.addAction(self.farAction)
        self.iface.addPluginToMenu("Navigate Features Toolbar", self.farAction)



        icon = QIcon(os.path.dirname(__file__) + "/images/rev.png")
        self.revAction = QAction(icon, "Jump to previous feature", self.iface.mainWindow())
        #add shortcut to button
        self.iface.registerMainWindowAction(self.revAction, "left")
        self.revAction.setObjectName('reversetool')
        self.revAction.triggered.connect(self.reverse)
        #self.revAction.setCheckable(True)  does not needed
        # set action for button click
        self.toolbar.addAction(self.revAction)
        self.iface.addPluginToMenu("Navigate Features Toolbar", self.revAction)







    def unload(self):
        '''Unload plugin from the QGIS interface'''

        self.iface.removePluginMenu('Navigate Features Toolbar', self.farAction)
        self.iface.removePluginMenu('Navigate Features Toolbar', self.revAction)

        # Remove Toolbar Icons
        self.iface.removeToolBarIcon(self.farAction)
        self.iface.removeToolBarIcon(self.revAction)

        #
        self.iface.unregisterMainWindowAction(self.farAction)
        self.iface.unregisterMainWindowAction(self.revAction)

        del self.toolbar



    def forward(self):
 
        layer = iface.activeLayer()

        total_count = layer.featureCount()
        #print(total_count)
        count = layer.selectedFeatureCount()
        selection = layer.selectedFeatures()


        if count == 1:
            for feature in selection:
                cur_id = feature.id()
                print(cur_id)
                cur_id = cur_id+1
                if cur_id < total_count:
                    layer.removeSelection()
                    layer.select(cur_id)
                    iface.actionZoomToSelected().trigger()
                else:
                    self.iface.messageBar().pushMessage("Last feature reached")
  
        else:
            self.iface.messageBar().pushMessage("Select one vector feature")




    def reverse(self):

        layer = iface.activeLayer()
        count = layer.selectedFeatureCount()
        selection = layer.selectedFeatures()

        if count == 1:
            for feature in selection:

                cur_id = feature.id()
                print(cur_id)
                cur_id = cur_id-1
                if cur_id > -1:
                    
                    layer.removeSelection()

                    layer.select(cur_id)
                    iface.actionZoomToSelected().trigger()
                else: 

                    self.iface.messageBar().pushMessage("First feature reached")

        else:
            self.iface.messageBar().pushMessage("Select one vector feature")
    
