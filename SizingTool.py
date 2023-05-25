from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap
import os
import sys

home_directory = os.path.expanduser( '~' )
sys.path.append(str(home_directory) + '/Circuit Sizing Tool/files')

import main
import pandas as pd

class UI_resultsWindow(QtWidgets.QDialog):                           
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Simulation Results")
        self.resize(600, 400)

        data = pd.read_csv(str(home_directory) + '/Circuit Sizing Tool/files/outputs/out_sizing.csv')
        
        self.table = QTableWidget()
        self.table.setRowCount(data.shape[0])
        self.table.setColumnCount(data.shape[1])
        
        self.table.setHorizontalHeaderLabels(data.columns)
        
        # Insere os dados do arquivo CSV na tabela
        for row in range(data.shape[0]):
            for col in range(data.shape[1]):
                item = QTableWidgetItem(str(data.iloc[row, col]))
                self.table.setItem(row, col, item)
        
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(633, 425)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gb_simParameters = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_simParameters.setGeometry(QtCore.QRect(10, 210, 181, 191))
        self.gb_simParameters.setObjectName("gb_simParameters")
        self.gridLayoutWidget = QtWidgets.QWidget(self.gb_simParameters)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 161, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid_parameters = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid_parameters.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.grid_parameters.setContentsMargins(0, 0, 0, 0)
        self.grid_parameters.setVerticalSpacing(1)
        self.grid_parameters.setObjectName("grid_parameters")
        self.txt_VDS = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.txt_VDS.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.txt_VDS.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txt_VDS.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.txt_VDS.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_VDS.setObjectName("txt_VDS")
        self.grid_parameters.addWidget(self.txt_VDS, 1, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_parameters.addItem(spacerItem, 3, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_parameters.addItem(spacerItem1, 6, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_parameters.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_parameters.addItem(spacerItem3, 5, 0, 1, 1)
        self.lb_L = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb_L.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_L.setAutoFillBackground(False)
        self.lb_L.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_L.setObjectName("lb_L")
        self.grid_parameters.addWidget(self.lb_L, 5, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_parameters.addItem(spacerItem4, 7, 3, 1, 1)
        self.txt_L = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.txt_L.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.txt_L.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txt_L.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.txt_L.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_L.setObjectName("txt_L")
        self.grid_parameters.addWidget(self.txt_L, 5, 5, 1, 1)
        self.lb_M = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb_M.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_M.setObjectName("lb_M")
        self.grid_parameters.addWidget(self.lb_M, 6, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_parameters.addItem(spacerItem5, 6, 3, 1, 1)
        self.lb_VGS = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb_VGS.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_VGS.setObjectName("lb_VGS")
        self.grid_parameters.addWidget(self.lb_VGS, 0, 1, 1, 1)
        self.txt_W = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.txt_W.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.txt_W.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txt_W.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.txt_W.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_W.setObjectName("txt_W")
        self.grid_parameters.addWidget(self.txt_W, 4, 5, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_parameters.addItem(spacerItem6, 4, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_parameters.addItem(spacerItem7, 5, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_parameters.addItem(spacerItem8, 1, 3, 1, 1)
        self.txt_NF = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.txt_NF.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.txt_NF.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txt_NF.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.txt_NF.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_NF.setObjectName("txt_NF")
        self.grid_parameters.addWidget(self.txt_NF, 7, 5, 1, 1)
        self.lb_W = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb_W.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_W.setObjectName("lb_W")
        self.grid_parameters.addWidget(self.lb_W, 4, 1, 1, 1)
        self.txt_VBS = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.txt_VBS.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.txt_VBS.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txt_VBS.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.txt_VBS.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_VBS.setObjectName("txt_VBS")
        self.grid_parameters.addWidget(self.txt_VBS, 3, 5, 1, 1)
        self.lb_VBS = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb_VBS.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_VBS.setObjectName("lb_VBS")
        self.grid_parameters.addWidget(self.lb_VBS, 3, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_parameters.addItem(spacerItem9, 1, 0, 1, 1)
        self.txt_M = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.txt_M.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.txt_M.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txt_M.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.txt_M.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_M.setObjectName("txt_M")
        self.grid_parameters.addWidget(self.txt_M, 6, 5, 1, 1)
        self.lb_NF = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb_NF.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_NF.setObjectName("lb_NF")
        self.grid_parameters.addWidget(self.lb_NF, 7, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_parameters.addItem(spacerItem10, 7, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_parameters.addItem(spacerItem11, 4, 0, 1, 1)
        self.lb_VDS = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb_VDS.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_VDS.setObjectName("lb_VDS")
        self.grid_parameters.addWidget(self.lb_VDS, 1, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_parameters.addItem(spacerItem12, 0, 3, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_parameters.addItem(spacerItem13, 0, 0, 1, 1)
        self.txt_VGS = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.txt_VGS.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.txt_VGS.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txt_VGS.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.txt_VGS.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_VGS.setObjectName("txt_VGS")
        self.grid_parameters.addWidget(self.txt_VGS, 0, 5, 1, 1)
        self.gb_searchParameters = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_searchParameters.setGeometry(QtCore.QRect(200, 210, 281, 191))
        self.gb_searchParameters.setObjectName("gb_searchParameters")
        self.cb_variable = QtWidgets.QComboBox(self.gb_searchParameters)
        self.cb_variable.setGeometry(QtCore.QRect(90, 90, 61, 23))
        self.cb_variable.setObjectName("cb_variable")
        self.cb_variable.addItem("")
        self.cb_variable.addItem("")
        self.cb_objective = QtWidgets.QComboBox(self.gb_searchParameters)
        self.cb_objective.setGeometry(QtCore.QRect(90, 60, 61, 23))
        self.cb_objective.setObjectName("cb_objective")
        self.cb_objective.addItem("")
        self.cb_objective.addItem("")
        self.cb_objective.addItem("")
        self.cb_objective.addItem("")
        self.chkb_onlySimulate = QtWidgets.QCheckBox(self.gb_searchParameters)
        self.chkb_onlySimulate.setGeometry(QtCore.QRect(20, 30, 111, 21))
        self.chkb_onlySimulate.setObjectName("chkb_onlySimulate")
        self.txt_objective = QtWidgets.QTextEdit(self.gb_searchParameters)
        self.txt_objective.setGeometry(QtCore.QRect(160, 60, 104, 21))
        self.txt_objective.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.txt_objective.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txt_objective.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.txt_objective.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.txt_objective.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_objective.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.txt_objective.setObjectName("txt_objective")
        self.lb_maxError = QtWidgets.QLabel(self.gb_searchParameters)
        self.lb_maxError.setGeometry(QtCore.QRect(16, 120, 71, 21))
        self.lb_maxError.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_maxError.setObjectName("lb_maxError")
        self.txt_maxError = QtWidgets.QTextEdit(self.gb_searchParameters)
        self.txt_maxError.setGeometry(QtCore.QRect(93, 120, 171, 21))
        self.txt_maxError.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.txt_maxError.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txt_maxError.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.txt_maxError.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_maxError.setObjectName("txt_maxError")
        self.lb_objective = QtWidgets.QLabel(self.gb_searchParameters)
        self.lb_objective.setGeometry(QtCore.QRect(10, 60, 81, 21))
        self.lb_objective.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_objective.setObjectName("lb_objective")
        self.lb_variable = QtWidgets.QLabel(self.gb_searchParameters)
        self.lb_variable.setGeometry(QtCore.QRect(9, 90, 81, 21))
        self.lb_variable.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_variable.setObjectName("lb_variable")
        self.chkb_output = QtWidgets.QCheckBox(self.gb_searchParameters)
        self.chkb_output.setGeometry(QtCore.QRect(20, 150, 71, 21))
        self.chkb_output.setObjectName("chkb_output")
        self.txt_output = QtWidgets.QTextEdit(self.gb_searchParameters)
        self.txt_output.setEnabled(False)
        self.txt_output.setGeometry(QtCore.QRect(92, 150, 171, 21))
        self.txt_output.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.txt_output.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txt_output.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.txt_output.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_output.setObjectName("txt_output")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(490, 210, 131, 151))
        self.groupBox.setObjectName("groupBox")
        self.rd_65nm = QtWidgets.QRadioButton(self.groupBox)
        self.rd_65nm.setEnabled(False)
        self.rd_65nm.setGeometry(QtCore.QRect(30, 68, 81, 21))
        self.rd_65nm.setObjectName("rd_65nm")
        self.rd_180nm = QtWidgets.QRadioButton(self.groupBox)
        self.rd_180nm.setEnabled(False)
        self.rd_180nm.setGeometry(QtCore.QRect(30, 48, 81, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rd_180nm.setFont(font)
        self.rd_180nm.setObjectName("rd_180nm")
        self.lb_technology = QtWidgets.QLabel(self.groupBox)
        self.lb_technology.setGeometry(QtCore.QRect(20, 28, 81, 16))
        self.lb_technology.setObjectName("lb_technology")
        self.lb_tranModel = QtWidgets.QLabel(self.groupBox)
        self.lb_tranModel.setGeometry(QtCore.QRect(16, 98, 111, 16))
        self.lb_tranModel.setObjectName("lb_tranModel")
        self.cb_tranModel = QtWidgets.QComboBox(self.groupBox)
        self.cb_tranModel.setGeometry(QtCore.QRect(38, 118, 61, 23))
        self.cb_tranModel.setObjectName("cb_tranModel")
        self.cb_tranModel.addItem("")
        self.cb_tranModel.addItem("")
        self.gv_projectPreview = QtWidgets.QGraphicsView(self.centralwidget)
        self.gv_projectPreview.setGeometry(QtCore.QRect(10, 21, 471, 181))
        self.gv_projectPreview.setObjectName("gv_projectPreview")
        self.gv_transistorView = QtWidgets.QGraphicsView(self.centralwidget)
        self.gv_transistorView.setGeometry(QtCore.QRect(490, 20, 131, 181))
        self.gv_transistorView.setObjectName("gv_transistorView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(12, 2, 91, 16))
        self.label.setObjectName("label")
        self.btn_Ok = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Ok.setGeometry(QtCore.QRect(523, 370, 71, 31))
        self.btn_Ok.setObjectName("btn_Ok")
        self.btn_addRect = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addRect.setGeometry(QtCore.QRect(444, 174, 31, 23))
        self.btn_addRect.setObjectName("btn_addRect")
        self.btn_deleteRect = QtWidgets.QPushButton(self.centralwidget)
        self.btn_deleteRect.setGeometry(QtCore.QRect(444, 148, 31, 23))
        self.btn_deleteRect.setObjectName("btn_deleteRect")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 633, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #################################################

        self.tech = sys.argv[1]
        if self.tech == '65':
            self.rd_65nm.toggle()

        if self.tech == '180':
            self.rd_180nm.toggle()
            self.cb_tranModel.addItem("")
            self.cb_tranModel.setItemText(2, QtCore.QCoreApplication.translate("MainWindow", "nch3"))
            self.cb_tranModel.addItem("")
            self.cb_tranModel.setItemText(3, QtCore.QCoreApplication.translate("MainWindow", "pch3"))
            self.cb_tranModel.addItem("")
            self.cb_tranModel.setItemText(4, QtCore.QCoreApplication.translate("MainWindow", "mench"))
            self.cb_tranModel.addItem("")
            self.cb_tranModel.setItemText(5, QtCore.QCoreApplication.translate("MainWindow", "mepch"))
            self.cb_tranModel.addItem("")
            self.cb_tranModel.setItemText(6, QtCore.QCoreApplication.translate("MainWindow", "mench3"))
            self.cb_tranModel.addItem("")
            self.cb_tranModel.setItemText(7, QtCore.QCoreApplication.translate("MainWindow", "nanch"))
            self.cb_tranModel.addItem("")
            self.cb_tranModel.setItemText(8, QtCore.QCoreApplication.translate("MainWindow", "nanch3"))

        #As entradas iniciam desativadas até que se adicione um retângulo
        self.txt_VGS.setEnabled(False)
        self.txt_VDS.setEnabled(False)
        self.txt_VBS.setEnabled(False)
        self.txt_W.setEnabled(False)
        self.txt_L.setEnabled(False)
        self.txt_M.setEnabled(False)
        self.txt_NF.setEnabled(False)
        self.txt_objective.setEnabled(False)
        self.txt_maxError.setEnabled(False)
        self.cb_objective.setEnabled(False)
        self.cb_tranModel.setEnabled(False)
        self.cb_variable.setEnabled(False)
        self.chkb_onlySimulate.setEnabled(False)
        self.chkb_output.setEnabled(False)
        self.btn_deleteRect.setEnabled(False)
        self.btn_Ok.setEnabled(False)

        #Exibe a figura do transistor nMOS inicialmente
        transistorScene = QtWidgets.QGraphicsScene()
        transistorScene.addPixmap(QPixmap(str(home_directory) + '/Circuit Sizing Tool/files/images/nMOS.png'))
        self.gv_transistorView.setScene(transistorScene)
        self.cb_tranModel.currentTextChanged.connect(self.changeImage)

        #Criar cena para exibir retângulos
        self.projectScene = QtWidgets.QGraphicsScene()
        self.gv_projectPreview.setScene(self.projectScene)

        #Figuras para desenhar 
        self.rects = []
        self.arrows = []
        self.figureText = []

        #Listas dos parâmetros de simulação
        self.transistorModels = []
        self.variables = []
        self.objectives = []
        self.objective_values = []
        self.maxErrors = []
        self.Lvalues = []
        self.Wvalues = []
        self.Mvalues = []
        self.NFvalues = []
        self.VGSvalues = []
        self.VDSvalues = []
        self.VBSvalues = []
        self.outputs_bool = []
        self.noOperation_bool = []
        self.output_list = []

        #Funções da janela
        self.chkb_onlySimulate.clicked.connect(self.only_simulate)
        self.chkb_output.clicked.connect(self.output_enable)
        self.btn_Ok.clicked.connect(self.ok)
        self.btn_addRect.clicked.connect(self.draw_rect)
        self.btn_deleteRect.clicked.connect(self.erase_rect)

    def draw_rect(self):
        if len(self.rects) == 0:
            self.rects.append(QtWidgets.QGraphicsRectItem(QtCore.QRectF(0, 0, 100, 100)))
            self.projectScene.addItem(self.rects[0])
            
            #Ativar as entradas quando houver um retângulo
            self.txt_VGS.setEnabled(True)
            self.txt_VDS.setEnabled(True)
            self.txt_VBS.setEnabled(True)
            self.txt_W.setEnabled(True)
            self.txt_L.setEnabled(True)
            self.txt_M.setEnabled(True)
            self.txt_NF.setEnabled(True)
            self.txt_objective.setEnabled(True)
            self.txt_maxError.setEnabled(True)
            self.cb_objective.setEnabled(True)
            self.cb_tranModel.setEnabled(True)
            self.cb_variable.setEnabled(True)
            self.chkb_onlySimulate.setEnabled(True)
            self.chkb_output.setEnabled(True)
            self.btn_deleteRect.setEnabled(True)
            self.btn_Ok.setEnabled(True)
        else:
            #Salva os parâmetros do retângulo anterior nas respectivas listas
            self.transistorModels.append(self.cb_tranModel.currentText())
            self.variables.append(self.cb_variable.currentText())
            self.objectives.append(self.cb_objective.currentText().lower())
            self.objective_values.append(self.txt_objective.toPlainText())
            self.maxErrors.append(self.txt_maxError.toPlainText())
            self.Lvalues.append(self.txt_L.toPlainText())
            self.Wvalues.append(self.txt_W.toPlainText())
            self.Mvalues.append(self.txt_M.toPlainText())
            self.NFvalues.append(self.txt_NF.toPlainText())
            self.VGSvalues.append(self.txt_VGS.toPlainText())
            self.VDSvalues.append(self.txt_VDS.toPlainText())
            self.VBSvalues.append(self.txt_VBS.toPlainText())
            self.outputs_bool.append(self.chkb_output.isChecked())
            self.noOperation_bool.append(self.chkb_onlySimulate.isChecked())
            self.output_list.append(self.txt_output.toPlainText())

            #Move os retângulos
            for item in self.rects:
                item.moveBy(-200, 0)
            self.rects.append(QtWidgets.QGraphicsRectItem(QtCore.QRectF(0, 0, 100, 100)))
            for line in self.arrows:
                line.moveBy(-200, 0)
            self.arrows.append(QtWidgets.QGraphicsLineItem(QtCore.QLineF(-100, 50, 0, 50)))
            #Cria o texto dentro dos retângulos
            transistorModel = self.cb_tranModel.currentText()
            variable = self.cb_variable.currentText()
            objective = self.cb_objective.currentText().lower()
            if self.txt_output.toPlainText() == '' or self.chkb_output.isChecked() == False:
                output = 'N/A'
            else:
                output = self.txt_output.toPlainText()

            self.infoText = "\n Model: "+transistorModel+"\n Variable: "+variable+"\n Objective: "+objective+"\n Output: "+output
            self.figureText.append(QtWidgets.QGraphicsSimpleTextItem(self.infoText,self.rects[-2]))
            self.projectScene.addItem(self.figureText[-1])

            self.projectScene.addItem(self.rects[-1])
            self.projectScene.addItem(self.arrows[-1])
    
    def erase_rect(self):
        if len(self.rects) > 0:
            #Deleta os últimos parâmetros salvos nas respectivas listas
            if len(self.transistorModels) == len(self.rects)+1:
                del self.transistorModels[-1]
                del self.variables[-1]
                del self.objectives[-1]
                del self.objective_values[-1]
                del self.maxErrors[-1]
                del self.Lvalues[-1]
                del self.Wvalues[-1]
                del self.Mvalues[-1]
                del self.NFvalues[-1]
                del self.VGSvalues[-1]
                del self.VDSvalues[-1]
                del self.VBSvalues[-1]
                del self.outputs_bool[-1]
                del self.noOperation_bool[-1]
                del self.output_list[-1]

            #Remove último retângulo e move os restantes em +200 píxels
            self.projectScene.removeItem(self.rects[-1])
            del self.rects[-1]
            for item in self.rects:
                item.moveBy(200, 0)

            #Remove linhas e textos, e move os restantes em +200 píxels
            if len(self.arrows) > 0:
                self.projectScene.removeItem(self.arrows[-1])
                del self.arrows[-1]
                for line in self.arrows:
                    line.moveBy(200, 0)
                if len(self.figureText) == len(self.rects):
                    self.projectScene.removeItem(self.figureText[-1])
                    del self.figureText[-1]

            #Desativar as entradas novamente
            if len(self.rects) == 0:
                self.txt_VGS.setEnabled(False)
                self.txt_VDS.setEnabled(False)
                self.txt_VBS.setEnabled(False)
                self.txt_W.setEnabled(False)
                self.txt_L.setEnabled(False)
                self.txt_M.setEnabled(False)
                self.txt_NF.setEnabled(False)
                self.txt_objective.setEnabled(False)
                self.txt_maxError.setEnabled(False)
                self.cb_objective.setEnabled(False)
                self.cb_tranModel.setEnabled(False)
                self.cb_variable.setEnabled(False)
                self.chkb_onlySimulate.setEnabled(False)
                self.chkb_output.setEnabled(False)
                self.btn_deleteRect.setEnabled(False)
                self.btn_Ok.setEnabled(False)
        else:
            pass

    def changeImage(self):
        if self.cb_tranModel.currentText() in ['nch', 'nch3', 'mench', 'mench3', 'nanch', 'nanch3']:
            scene = QtWidgets.QGraphicsScene()
            scene.addPixmap(QPixmap(str(home_directory) + '/Circuit Sizing Tool/files/images/nMOS.png'))
            self.gv_transistorView.setScene(scene)
            QApplication.processEvents()
        elif self.cb_tranModel.currentText() in ['pch', 'pch3', 'mepch']:
            scene = QtWidgets.QGraphicsScene()
            scene.addPixmap(QPixmap(str(home_directory) + '/Circuit Sizing Tool/files/images/pMOS.png'))
            self.gv_transistorView.setScene(scene)
            QApplication.processEvents()
 
    def output_enable(self):
        if self.chkb_output.isChecked() == True:
            self.txt_output.setEnabled(True)
            QApplication.processEvents()
        else:
            self.txt_output.setEnabled(False)
            QApplication.processEvents()
    
    def only_simulate(self):
        if self.chkb_onlySimulate.isChecked() == True:
            self.cb_variable.setEnabled(False)
            self.txt_objective.setEnabled(False)
            self.txt_maxError.setEnabled(False)
            QApplication.processEvents()
        else:
            self.cb_variable.setEnabled(True)
            self.txt_objective.setEnabled(True)
            self.txt_maxError.setEnabled(True)
            QApplication.processEvents()

    def ok(self):
        if self.rd_180nm.isChecked():
            self.tech = "180nm"
        elif self.rd_180nm.isChecked():
            self.tech = "65nm"

        technology = self.tech
        transistorModel = self.cb_tranModel.currentText()
        variable = self.cb_variable.currentText()
        objective = self.cb_objective.currentText().lower()

        self.transistorModels.append(self.cb_tranModel.currentText())
        self.variables.append(self.cb_variable.currentText())
        self.objectives.append(self.cb_objective.currentText().lower())
        self.objective_values.append(self.txt_objective.toPlainText())
        self.maxErrors.append(self.txt_maxError.toPlainText())
        self.Lvalues.append(self.txt_L.toPlainText())
        self.Wvalues.append(self.txt_W.toPlainText())
        self.Mvalues.append(self.txt_M.toPlainText())
        self.NFvalues.append(self.txt_NF.toPlainText())
        self.VGSvalues.append(self.txt_VGS.toPlainText())
        self.VDSvalues.append(self.txt_VDS.toPlainText())
        self.VBSvalues.append(self.txt_VBS.toPlainText())
        self.outputs_bool.append(self.chkb_output.isChecked())
        self.noOperation_bool.append(self.chkb_onlySimulate.isChecked())
        self.output_list.append(self.txt_output.toPlainText())

        if len(self.rects) < len(self.transistorModels):
            del self.transistorModels[0]
            del self.variables[0]
            del self.objectives[0]
            del self.objective_values[0]
            del self.maxErrors[0]
            del self.Lvalues[0]
            del self.Wvalues[0]
            del self.Mvalues[0]
            del self.NFvalues[0]
            del self.VGSvalues[0]
            del self.VDSvalues[0]
            del self.VBSvalues[0]
            del self.outputs_bool[0]
            del self.noOperation_bool[0]
            del self.output_list[0]

        if self.txt_output.toPlainText() == '' or self.chkb_output.isChecked() == False:
            output = 'N/A'
        else:
            output = self.txt_output.toPlainText()

        self.infoText = "\n Model: "+transistorModel+"\n Variable: "+variable+"\n Objective: "+objective+"\n Output: "+output
        self.figureText.append(QtWidgets.QGraphicsSimpleTextItem(self.infoText,self.rects[-1]))
        self.projectScene.addItem(self.figureText[-1])

        QApplication.processEvents()
        try:
            i = 0
            iOut = 0
            dataFrame = False
            while i < len(self.rects):
                if self.outputs_bool[i] == False:
                    if self.objective_values[i] != 'out':
                        main.main(str(technology+"nm"), str(self.transistorModels[i]), no_op=self.noOperation_bool[i], target_name=str(self.objectives[i]), target_value=float(self.objective_values[i]), max_error=float(self.maxErrors[i]), L=float(self.Lvalues[i]), NF=float(self.NFvalues[i]), M=float(self.Mvalues[i]), VGS=float(self.VGSvalues[i]), VDS=float(self.VDSvalues[i]), VBS=float(self.VBSvalues[i]), parameter_calc_name=str(self.variables[i]))
                    else:
                        main.main(str(technology+"nm"), str(self.transistorModels[i]), no_op=self.noOperation_bool[i], target_name=str(self.objectives[i]), target_value=float(out), max_error=float(self.maxErrors[i]), L=float(self.Lvalues[i]), W=float(self.Wvalues[i]), NF=float(self.NFvalues[i]), M=float(self.Mvalues[i]), VGS=float(self.VGSvalues[i]), VDS=float(self.VDSvalues[i]), VBS=float(self.VBSvalues[i]), parameter_calc_name=str(self.variables[i]))
                if self.outputs_bool[i] == True:
                    if self.objective_values[i] != 'out':
                        out = main.main(str(technology+"nm"), str(self.transistorModels[i]), no_op=self.noOperation_bool[i], target_name=str(self.objectives[i]), target_value=float(self.objective_values[i]), max_error=float(self.maxErrors[i]), L=float(self.Lvalues[i]), W=float(self.Wvalues[i]), NF=float(self.NFvalues[i]), M=float(self.Mvalues[i]), VGS=float(self.VGSvalues[i]), VDS=float(self.VDSvalues[i]), VBS=float(self.VBSvalues[i]), parameter_calc_name=str(self.variables[i]), out_param=str(self.output_list[iOut]))
                        iOut += 1
                    else:
                        out = main.main(str(technology+"nm"), str(self.transistorModels[i]), no_op=self.noOperation_bool[i], target_name=str(self.objectives[i]), target_value=float(out), max_error=float(self.maxErrors[i]), L=float(self.Lvalues[i]), W=float(self.Wvalues[i]), NF=float(self.NFvalues[i]), M=float(self.Mvalues[i]), VGS=float(self.VGSvalues[i]), VDS=float(self.VDSvalues[i]), VBS=float(self.VBSvalues[i]), parameter_calc_name=str(self.variables[i]), out_param=str(self.output_list[iOut]))
                        iOut += 1
                
                columns = []
                rows = []
                if self.transistorModels[i] in ['nch', 'nch3', 'mench', 'mench3', 'nanch', 'nanch3']:
                    outFile = open(str(home_directory) + '/Circuit Sizing Tool/files/outputs/output_nmos'+ str(self.tech) + '.txt', 'r')
                elif self.transistorModels[i] in ['pch', 'pch3', 'mepch']:
                    outFile = open(str(home_directory) + '/Circuit Sizing Tool/files/outputs/output_pmos'+ str(self.tech) + '.txt', 'r')
                outFileTxt = outFile.readlines()
                outFile.close()
                for line in outFileTxt:
                    if '#' not in line:
                        if line.split("=")[0] != '\n':
                            columns.append(line.split("=")[0])
                            rows.append(line.split("=")[1][:-1])
                if dataFrame == False:
                    columns[0] = 'Objective'
                    columns[1] = 'Variable'
                    self.resultData = pd.DataFrame(columns=columns)
                    dataFrame = True
                self.resultData.loc[len(self.resultData)] = rows
    
                rows = []

                i += 1
            
            self.resultData.to_csv(str(home_directory) + '/Circuit Sizing Tool/files/outputs/out_sizing.csv')

            #Exibe mensagem após concluir as simulações
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Sizing Process Done!")
            msgBox.setWindowTitle("Sucess")
            msgBox.setStandardButtons(QMessageBox.Ok)
 
            returnValue = msgBox.exec()

            #Exibe janela com os resultados
            self.resultsWindow()

        except:
            self.projectScene.removeItem(self.figureText[-1])
            del self.figureText[-1]

            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("Error! Verify the parameter inputs!")
            error_window = error_dialog.exec_()

    def resultsWindow(self):                                          
        self.w = UI_resultsWindow(self)
        self.w.show()
        self.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sizing Tool"))
        self.gb_simParameters.setTitle(_translate("MainWindow", "Simulation Parameters"))
        self.lb_L.setText(_translate("MainWindow", "L"))
        self.lb_M.setText(_translate("MainWindow", "M"))
        self.lb_VGS.setText(_translate("MainWindow", "VGS"))
        self.lb_W.setText(_translate("MainWindow", "W"))
        self.lb_VBS.setText(_translate("MainWindow", "VBS"))
        self.lb_NF.setText(_translate("MainWindow", "NF"))
        self.lb_VDS.setText(_translate("MainWindow", "VDS"))
        self.gb_searchParameters.setTitle(_translate("MainWindow", "Search Options"))
        self.cb_variable.setItemText(0, _translate("MainWindow", "W"))
        self.cb_variable.setItemText(1, _translate("MainWindow", "L"))
        self.cb_objective.setItemText(0, _translate("MainWindow", "Ids"))
        self.cb_objective.setItemText(1, _translate("MainWindow", "gm"))
        self.cb_objective.setItemText(2, _translate("MainWindow", "gds"))
        self.cb_objective.setItemText(3, _translate("MainWindow", "gmb"))
        self.chkb_onlySimulate.setText(_translate("MainWindow", "Only Simulate"))
        self.lb_maxError.setText(_translate("MainWindow", "Max Error:"))
        self.lb_objective.setText(_translate("MainWindow", "Objective:"))
        self.lb_variable.setText(_translate("MainWindow", "Variable:"))
        self.chkb_output.setText(_translate("MainWindow", "Output: "))
        self.groupBox.setTitle(_translate("MainWindow", "Transistor Config"))
        self.rd_65nm.setText(_translate("MainWindow", "65 nm"))
        self.rd_180nm.setText(_translate("MainWindow", "180 nm"))
        self.lb_technology.setText(_translate("MainWindow", "Technology"))
        self.lb_tranModel.setText(_translate("MainWindow", "Transistor Model"))
        self.cb_tranModel.setItemText(0, _translate("MainWindow", "nch"))
        self.cb_tranModel.setItemText(1, _translate("MainWindow", "pch"))
        self.label.setText(_translate("MainWindow", "Project View"))
        self.btn_Ok.setText(_translate("MainWindow", "Ok"))
        self.btn_addRect.setText(_translate("MainWindow", "+"))
        self.btn_deleteRect.setText(_translate("MainWindow", "-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
