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
        # set action for button click
        self.farAction.triggered.connect(self.forward)
        self.farAction.setCheckable(True)
        self.toolbar.addAction(self.farAction)
        self.iface.addPluginToMenu("Forward reverse Toolbar", self.farAction)

        

        icon = QIcon(os.path.dirname(__file__) + "/images/rev.png")
        self.revAction = QAction(icon, "reverse one feature", self.iface.mainWindow())
        #add shortcut to button
        self.iface.registerMainWindowAction(self.revAction, "left")
        self.revAction.setObjectName('reversetool')
        self.revAction.triggered.connect(self.reverse)
        self.revAction.setCheckable(True)
        # set action for button click
        self.toolbar.addAction(self.revAction)
        self.iface.addPluginToMenu("Forward reverse Toolbar", self.revAction)


     


    def unload(self):
        '''Unload plugin from the QGIS interface'''

        self.iface.removePluginMenu('Forward reverse Toolbar', self.farAction)
        self.iface.removePluginMenu('Forward reverse Toolbar', self.revAction)

        # Remove Toolbar Icons
        self.iface.removeToolBarIcon(self.farAction)
        self.iface.removeToolBarIcon(self.revAction)
        
        
        self.iface.unregisterMainWindowAction(self.farAction)
        self.iface.unregisterMainWindowAction(self.revAction)
        
        del self.toolbar


    
        
    def forward(self):
         try:
            layer = iface.activeLayer()
            feature_count = layer.featureCount
            count = layer.selectedFeatureCount()
            selection = layer.selectedFeatures()

        except:
            print("Open")

        
        
        if count == 1:
            for feature in selection:    
                try: 
                    layer.removeSelection()
                    layer.select(feature['id']+1)
                    iface.actionZoomToSelected().trigger();
                    print(feature['id']+1)
                    
                except:
                    print("Last Feature reached")

                
        else:
            print("select one feature")


    def reverse(self):
        
        layer = iface.activeLayer()
        count = layer.selectedFeatureCount()
        selection = layer.selectedFeatures()
        feature_count = layer.featureCount
        if count == 1:
            for feature in selection:    
                try:
                    layer.removeSelection()
                    layer.select(feature['id']-1)
                    iface.actionZoomToSelected().trigger();
                    print(feature['id']-1)
                except:
                    print("Last Feature reached")
        else:
            print("select one feature")


