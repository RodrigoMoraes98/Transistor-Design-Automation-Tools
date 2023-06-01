from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os, sys
home_directory = os.path.expanduser( '~' )
sys.path.append(str(home_directory) + '/Circuit Sizing Tool/files')

import sweep
import pandas as pd
import matplotlib.pyplot as plt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(714, 472)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tb_parameters = QtWidgets.QTableWidget(self.centralwidget)
        self.tb_parameters.setMaximumSize(QtCore.QSize(215, 231))
        self.tb_parameters.setAlternatingRowColors(True)
        self.tb_parameters.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_parameters.setGridStyle(QtCore.Qt.SolidLine)
        self.tb_parameters.setObjectName("tb_parameters")
        self.tb_parameters.setColumnCount(2)
        self.tb_parameters.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setKerning(True)
        item.setFont(font)
        self.tb_parameters.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_parameters.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_parameters.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tb_parameters.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_parameters.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_parameters.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_parameters.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_parameters.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_parameters.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tb_parameters.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tb_parameters.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tb_parameters.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tb_parameters.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tb_parameters.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tb_parameters.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tb_parameters.setItem(6, 0, item)
        self.tb_parameters.horizontalHeader().setDefaultSectionSize(100)
        self.gridLayout.addWidget(self.tb_parameters, 1, 0, 1, 1)
        self.tb_simResults = QtWidgets.QTableWidget(self.centralwidget)
        self.tb_simResults.setEnabled(False)
        self.tb_simResults.setMinimumSize(QtCore.QSize(350, 231))
        self.tb_simResults.setMaximumSize(QtCore.QSize(16777215, 231))
        self.tb_simResults.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_simResults.setAlternatingRowColors(True)
        self.tb_simResults.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)
        self.tb_simResults.setObjectName("tb_simResults")
        self.tb_simResults.setColumnCount(14)
        self.tb_simResults.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tb_simResults.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_simResults.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_simResults.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_simResults.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_simResults.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_simResults.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_simResults.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_simResults.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_simResults.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_simResults.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_simResults.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_simResults.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_simResults.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_simResults.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_simResults.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_simResults.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_simResults.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_simResults.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_simResults.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_simResults.setHorizontalHeaderItem(13, item)
        self.tb_simResults.horizontalHeader().setDefaultSectionSize(80)
        self.tb_simResults.horizontalHeader().setMinimumSectionSize(25)
        self.gridLayout.addWidget(self.tb_simResults, 1, 1, 1, 3)
        self.gb_tranConfig = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_tranConfig.setObjectName("gb_tranConfig")
        self.rb_180nm = QtWidgets.QRadioButton(self.gb_tranConfig)
        self.rb_180nm.setEnabled(False)
        self.rb_180nm.setGeometry(QtCore.QRect(30, 50, 100, 21))
        self.rb_180nm.setObjectName("rb_180nm")
        self.rb_65nm = QtWidgets.QRadioButton(self.gb_tranConfig)
        self.rb_65nm.setEnabled(False)
        self.rb_65nm.setGeometry(QtCore.QRect(30, 70, 100, 21))
        self.rb_65nm.setObjectName("rb_65nm")
        self.cb_tranModel = QtWidgets.QComboBox(self.gb_tranConfig)
        self.cb_tranModel.setGeometry(QtCore.QRect(40, 120, 61, 23))
        self.cb_tranModel.setObjectName("cb_tranModel")
        self.cb_tranModel.addItem("")
        self.cb_tranModel.addItem("")
        self.lb_technology = QtWidgets.QLabel(self.gb_tranConfig)
        self.lb_technology.setGeometry(QtCore.QRect(20, 30, 81, 16))
        self.lb_technology.setObjectName("lb_technology")
        self.lb_tranModel = QtWidgets.QLabel(self.gb_tranConfig)
        self.lb_tranModel.setGeometry(QtCore.QRect(20, 100, 111, 16))
        self.lb_tranModel.setObjectName("lb_tranModel")
        self.gridLayout.addWidget(self.gb_tranConfig, 0, 3, 1, 1)
        self.btn_sweep = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sweep.setObjectName("btn_sweep")
        self.gridLayout.addWidget(self.btn_sweep, 3, 3, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 3)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(50, 110, 61, 31))
        self.pushButton.setObjectName("pushButton")
        self.cb_plotSelectAxis = QtWidgets.QCheckBox(self.groupBox)
        self.cb_plotSelectAxis.setEnabled(False)
        self.cb_plotSelectAxis.setGeometry(QtCore.QRect(10, 30, 141, 21))
        self.cb_plotSelectAxis.setObjectName("cb_plotSelectAxis")
        self.lb_Xaxis = QtWidgets.QLabel(self.groupBox)
        self.lb_Xaxis.setEnabled(False)
        self.lb_Xaxis.setGeometry(QtCore.QRect(10, 60, 51, 16))
        self.lb_Xaxis.setObjectName("lb_Xaxis")
        self.lb_Yaxis = QtWidgets.QLabel(self.groupBox)
        self.lb_Yaxis.setEnabled(False)
        self.lb_Yaxis.setGeometry(QtCore.QRect(10, 83, 51, 16))
        self.lb_Yaxis.setObjectName("lb_Yaxis")
        self.lb_XaxisName = QtWidgets.QLabel(self.groupBox)
        self.lb_XaxisName.setEnabled(False)
        self.lb_XaxisName.setGeometry(QtCore.QRect(60, 62, 81, 16))
        self.lb_XaxisName.setObjectName("lb_XaxisName")
        self.lb_YaxisName = QtWidgets.QLabel(self.groupBox)
        self.lb_YaxisName.setEnabled(False)
        self.lb_YaxisName.setGeometry(QtCore.QRect(60, 83, 81, 16))
        self.lb_YaxisName.setObjectName("lb_YaxisName")
        self.gridLayout.addWidget(self.groupBox, 0, 2, 1, 1)
        self.gb_simPreferences = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_simPreferences.setObjectName("gb_simPreferences")
        self.lb_sweepParameter = QtWidgets.QLabel(self.gb_simPreferences)
        self.lb_sweepParameter.setGeometry(QtCore.QRect(10, 32, 121, 16))
        self.lb_sweepParameter.setObjectName("lb_sweepParameter")
        self.cb_sweepParameter = QtWidgets.QComboBox(self.gb_simPreferences)
        self.cb_sweepParameter.setGeometry(QtCore.QRect(126, 29, 61, 23))
        self.cb_sweepParameter.setObjectName("cb_sweepParameter")
        self.cb_sweepParameter.addItem("")
        self.cb_sweepParameter.addItem("")
        self.cb_sweepParameter.addItem("")
        self.cb_sweepParameter.addItem("")
        self.cb_sweepParameter.addItem("")
        self.cb_objectiveParameter = QtWidgets.QComboBox(self.gb_simPreferences)
        self.cb_objectiveParameter.setGeometry(QtCore.QRect(90, 58, 61, 23))
        self.cb_objectiveParameter.setObjectName("cb_objectiveParameter")
        self.cb_objectiveParameter.addItem("")
        self.cb_objectiveParameter.addItem("")
        self.cb_objectiveParameter.addItem("")
        self.cb_objectiveParameter.addItem("")
        self.lb_objectiveParameter = QtWidgets.QLabel(self.gb_simPreferences)
        self.lb_objectiveParameter.setGeometry(QtCore.QRect(14, 62, 71, 16))
        self.lb_objectiveParameter.setObjectName("lb_objectiveParameter")
        self.lb_variableParameter = QtWidgets.QLabel(self.gb_simPreferences)
        self.lb_variableParameter.setGeometry(QtCore.QRect(14, 93, 81, 16))
        self.lb_variableParameter.setObjectName("lb_variableParameter")
        self.cb_variableParameter = QtWidgets.QComboBox(self.gb_simPreferences)
        self.cb_variableParameter.setGeometry(QtCore.QRect(126, 88, 61, 23))
        self.cb_variableParameter.setObjectName("cb_variableParameter")
        self.cb_variableParameter.addItem("")
        self.cb_variableParameter.addItem("")
        self.lb_maxError = QtWidgets.QLabel(self.gb_simPreferences)
        self.lb_maxError.setGeometry(QtCore.QRect(14, 122, 121, 16))
        self.lb_maxError.setObjectName("lb_maxError")
        self.txt_maxError = QtWidgets.QTextEdit(self.gb_simPreferences)
        self.txt_maxError.setGeometry(QtCore.QRect(126, 120, 61, 21))
        self.txt_maxError.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_maxError.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_maxError.setObjectName("txt_maxError")
        self.cb_sweepStep = QtWidgets.QComboBox(self.gb_simPreferences)
        self.cb_sweepStep.setGeometry(QtCore.QRect(290, 29, 81, 23))
        self.cb_sweepStep.setObjectName("cb_sweepStep")
        self.cb_sweepStep.addItem("")
        self.cb_sweepStep.addItem("")
        self.lb_sweepStep = QtWidgets.QLabel(self.gb_simPreferences)
        self.lb_sweepStep.setGeometry(QtCore.QRect(210, 30, 81, 16))
        self.lb_sweepStep.setObjectName("lb_sweepStep")
        self.lb_from = QtWidgets.QLabel(self.gb_simPreferences)
        self.lb_from.setGeometry(QtCore.QRect(250, 60, 41, 16))
        self.lb_from.setObjectName("lb_from")
        self.txt_from = QtWidgets.QTextEdit(self.gb_simPreferences)
        self.txt_from.setGeometry(QtCore.QRect(300, 60, 71, 21))
        self.txt_from.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_from.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_from.setObjectName("txt_from")
        self.lb_to = QtWidgets.QLabel(self.gb_simPreferences)
        self.lb_to.setGeometry(QtCore.QRect(250, 90, 21, 16))
        self.lb_to.setObjectName("lb_to")
        self.txt_to = QtWidgets.QTextEdit(self.gb_simPreferences)
        self.txt_to.setGeometry(QtCore.QRect(300, 90, 71, 21))
        self.txt_to.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_to.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_to.setObjectName("txt_to")
        self.lb_nOfSteps = QtWidgets.QLabel(self.gb_simPreferences)
        self.lb_nOfSteps.setGeometry(QtCore.QRect(210, 122, 81, 16))
        self.lb_nOfSteps.setObjectName("lb_nOfSteps")
        self.sb_nOfSteps = QtWidgets.QSpinBox(self.gb_simPreferences)
        self.sb_nOfSteps.setGeometry(QtCore.QRect(290, 120, 81, 24))
        self.sb_nOfSteps.setObjectName("sb_nOfSteps")
        self.txt_objectiveValue = QtWidgets.QTextEdit(self.gb_simPreferences)
        self.txt_objectiveValue.setGeometry(QtCore.QRect(160, 60, 61, 21))
        self.txt_objectiveValue.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_objectiveValue.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_objectiveValue.setObjectName("txt_objectiveValue")
        self.gridLayout.addWidget(self.gb_simPreferences, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 714, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_project = QtWidgets.QAction(MainWindow)
        self.actionNew_project.setObjectName("actionNew_project")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSimulation_options = QtWidgets.QAction(MainWindow)
        self.actionSimulation_options.setObjectName("actionSimulation_options")
        self.actionSave_csv_file = QtWidgets.QAction(MainWindow)
        self.actionSave_csv_file.setObjectName("actionSave_csv_file")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ###################################################
        self.tech = sys.argv[1]
        if self.tech == '65':
            self.rb_65nm.toggle()

        if self.tech == '180':
            self.rb_180nm.toggle()
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
        
        self.count = 0
        self.gm_id = []
        self.gm_gds = []
        self.gmb_gm = []
        self.gmb_gds = []


        self.cb_plotSelectAxis.clicked.connect(self.select_plot)
        self.btn_sweep.clicked.connect(self.sweep_pressed)
        self.tb_simResults.cellClicked.connect(self.select_column)
        self.pushButton.clicked.connect(self.plot)
        ###################################################

    def plot(self):
        particular_cases = ['gm/id', 'gm/gds', 'gmb/gm', 'gmb/gds']
        particular_cases_lists = [self.gm_id, self.gm_gds, self.gmb_gm, self.gmb_gds]

        x = self.lb_XaxisName.text()
        y = self.lb_YaxisName.text()
        plt.xlabel(x)
        plt.ylabel(y)
        data = pd.read_csv(str(home_directory) + '/Circuit Sizing Tool/files/outputs/out_sweep.csv')
        
        if x and y not in particular_cases:
            plt.plot(data[x], data[y])
        elif x in particular_cases and y not in particular_cases:
            index_x = particular_cases.index(x)
            plt.plot(particular_cases_lists[index_x], data[y])
        elif y in particular_cases and x not in particular_cases:
            index_y = particular_cases.index(y)
            plt.plot(data[x], particular_cases_lists[index_y])
        elif x and y in particular_cases:
            index_x = particular_cases.index(x)
            index_y = particular_cases.index(y)
            print(particular_cases_lists[index_x])
            plt.plot(particular_cases_lists[index_x], particular_cases_lists[index_y])

        plt.show()

    def select_column(self):
        columns = ['Sweep Parameter', 'Objective', 'Variable', 'ids ', 'gm ', 'gds ', 'cgd ', 'cgs ', 'cdb ', 'cds ', 'gm/id', 'gm/gds', 'gmb/gm', 'gmb/gds']
        if self.lb_Xaxis.isEnabled() == True:
            if self.count % 2 == 0:
                self.lb_XaxisName.setText(str(columns[self.tb_simResults.currentColumn()]))
                self.count += 1
            else:
                self.lb_YaxisName.setText(str(columns[self.tb_simResults.currentColumn()]))
                self.count += 1
        self.pushButton.setEnabled(True)

    def select_plot(self):
        dlg = QMessageBox()
        dlg.setWindowTitle("Information")
        dlg.setText("Click in the columns below to select the plot axis!")
        button = dlg.exec()
        self.lb_Xaxis.setEnabled(True)
        self.lb_XaxisName.setEnabled(True)
        #Selecionar o parâmetro do eixo Y após selecionar para o eixo X
        self.lb_Yaxis.setEnabled(True)
        self.lb_YaxisName.setEnabled(True)
        

    def sweep_pressed(self):
        try:
            VarMin = self.txt_from.toPlainText()
            VarMax = self.txt_to.toPlainText()
            steps = self.sb_nOfSteps.value()
            sweepType = self.cb_sweepStep.currentText().lower()
            sweepVar = self.cb_sweepParameter.currentText()
            technology = sys.argv[1]
            transistorModel = self.cb_tranModel.currentText()
            targetName = self.cb_objectiveParameter.currentText()
            targetValue = self.txt_objectiveValue.toPlainText()
            maxError = self.txt_maxError.toPlainText()
            vgs = str(self.tb_parameters.item(0,1).text())
            vds = str(self.tb_parameters.item(1,1).text())
            vbs = str(self.tb_parameters.item(2,1).text())
            w = str(self.tb_parameters.item(3,1).text())
            l = str(self.tb_parameters.item(4,1).text())
            m = str(self.tb_parameters.item(5,1).text())
            nf = str(self.tb_parameters.item(6,1).text())
            variable = self.cb_variableParameter.currentText()

            self.progressBar.setRange(0, steps)

            sweep.sweep(float(VarMin), float(VarMax), steps, sweepType, sweepVar, str(technology + "nm"), transistorModel, targetName, targetValue, float(maxError), float(w), float(l), int(nf), int(m), float(vgs), float(vds), float(vbs), variable)

            self.tb_simResults.setEnabled(True)
            self.cb_plotSelectAxis.setEnabled(True)

            data = pd.read_csv(str(home_directory) + '/Circuit Sizing Tool/files/outputs/out_sweep.csv')
            self.tb_simResults.setRowCount(data.shape[0])
            for column in data.columns:
                if column.strip(' ').lower() == 'sweep parameter':
                    for i in range(data.shape[0]):
                        item = QtWidgets.QTableWidgetItem(str(data['Sweep Parameter'][i]))
                        self.tb_simResults.setItem(i, 0, item)
                if column.strip(' ').lower() == 'objective':
                    for i in range(data.shape[0]):
                        item = QtWidgets.QTableWidgetItem(str(data['Objective'][i]))
                        self.tb_simResults.setItem(i, 1, item)
                if column.strip(' ').lower() == 'variable':
                    for i in range(data.shape[0]):
                        item = QtWidgets.QTableWidgetItem(str(data['Variable'][i]))
                        self.tb_simResults.setItem(i, 2, item)
                if column.strip(' ').lower() == 'ids':
                    for i in range(data.shape[0]):
                        item = QtWidgets.QTableWidgetItem(str(data['ids '][i]))
                        self.tb_simResults.setItem(i, 3, item)
                if column.strip(' ').lower() == 'gm':
                    for i in range(data.shape[0]):
                        item = QtWidgets.QTableWidgetItem(str(data['gm '][i]))
                        self.tb_simResults.setItem(i, 4, item)
                if column.strip(' ').lower() == 'gds':
                    for i in range(data.shape[0]):
                        item = QtWidgets.QTableWidgetItem(str(data['gds '][i]))
                        self.tb_simResults.setItem(i, 5, item)
                if column.strip(' ').lower() == 'cgd':
                    for i in range(data.shape[0]):
                        item = QtWidgets.QTableWidgetItem(str(data['cgd '][i]))
                        self.tb_simResults.setItem(i, 6, item)
                if column.strip(' ').lower() == 'cgd':
                    for i in range(data.shape[0]):
                        item = QtWidgets.QTableWidgetItem(str(data['cgs '][i]))
                        self.tb_simResults.setItem(i, 7, item)
                if column.strip(' ').lower() == 'cdb':
                    for i in range(data.shape[0]):
                        item = QtWidgets.QTableWidgetItem(str(data['cdb '][i]))
                        self.tb_simResults.setItem(i, 8, item)
                if column.strip(' ').lower() == 'cds':
                    for i in range(data.shape[0]):
                        item = QtWidgets.QTableWidgetItem(str(data['cds '][i]))
                        self.tb_simResults.setItem(i, 9, item)

            for i in range(data.shape[0]):
                self.gm_id.append(float(data['gm '][i])/float(data['ids '][i]))
                item = QtWidgets.QTableWidgetItem(str(self.gm_id[i]))
                self.tb_simResults.setItem(i, 10, item)

                self.gm_gds.append(float(data['gm '][i])/float(data['gds '][i]))
                item = QtWidgets.QTableWidgetItem(str(self.gm_gds[i]))
                self.tb_simResults.setItem(i, 11, item)

                self.gmb_gm.append(float(data['gmbs '][i])/float(data['gm '][i]))
                item = QtWidgets.QTableWidgetItem(str(self.gmb_gm[i]))
                self.tb_simResults.setItem(i, 12, item)

                self.gmb_gds.append(float(data['gmbs '][i])/float(data['gds '][i]))
                item = QtWidgets.QTableWidgetItem(str(self.gmb_gds[i]))
                self.tb_simResults.setItem(i, 13, item)

        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("Error! Verify the parameter inputs!")
            error_window = error_dialog.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sweep Tool"))
        self.tb_parameters.setSortingEnabled(False)
        item = self.tb_parameters.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tb_parameters.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tb_parameters.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tb_parameters.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tb_parameters.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tb_parameters.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tb_parameters.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tb_parameters.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Parameter"))
        item = self.tb_parameters.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        __sortingEnabled = self.tb_parameters.isSortingEnabled()
        self.tb_parameters.setSortingEnabled(False)
        item = self.tb_parameters.item(0, 0)
        item.setText(_translate("MainWindow", "VGS"))
        item = self.tb_parameters.item(1, 0)
        item.setText(_translate("MainWindow", "VDS"))
        item = self.tb_parameters.item(2, 0)
        item.setText(_translate("MainWindow", "VBS"))
        item = self.tb_parameters.item(3, 0)
        item.setText(_translate("MainWindow", "W"))
        item = self.tb_parameters.item(4, 0)
        item.setText(_translate("MainWindow", "L"))
        item = self.tb_parameters.item(5, 0)
        item.setText(_translate("MainWindow", "M"))
        item = self.tb_parameters.item(6, 0)
        item.setText(_translate("MainWindow", "NF"))
        self.tb_parameters.setSortingEnabled(__sortingEnabled)
        item = self.tb_simResults.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tb_simResults.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tb_simResults.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tb_simResults.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tb_simResults.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tb_simResults.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tb_simResults.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Sweep Parameter"))
        item = self.tb_simResults.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Objective"))
        item = self.tb_simResults.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Variable"))
        item = self.tb_simResults.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ids"))
        item = self.tb_simResults.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "gm"))
        item = self.tb_simResults.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "gds"))
        item = self.tb_simResults.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "cgd"))
        item = self.tb_simResults.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "cgs"))
        item = self.tb_simResults.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "cdb"))
        item = self.tb_simResults.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "cds"))
        item = self.tb_simResults.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "gm/Id"))
        item = self.tb_simResults.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "gm/gds"))
        item = self.tb_simResults.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "gmb/gm"))
        item = self.tb_simResults.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "gmb/gds"))
        self.gb_tranConfig.setTitle(_translate("MainWindow", "Transistor Config"))
        self.rb_180nm.setText(_translate("MainWindow", "180 nm"))
        self.rb_65nm.setText(_translate("MainWindow", "65 nm"))
        self.cb_tranModel.setItemText(0, _translate("MainWindow", "nch"))
        self.cb_tranModel.setItemText(1, _translate("MainWindow", "pch"))
        self.lb_technology.setText(_translate("MainWindow", "Technology"))
        self.lb_tranModel.setText(_translate("MainWindow", "Transistor Model"))
        self.btn_sweep.setText(_translate("MainWindow", "Sweep"))
        self.groupBox.setTitle(_translate("MainWindow", "Plot Config"))
        self.pushButton.setText(_translate("MainWindow", "Plot"))
        self.cb_plotSelectAxis.setText(_translate("MainWindow", "Select plot axis"))
        self.lb_Xaxis.setText(_translate("MainWindow", "X axis:"))
        self.lb_Yaxis.setText(_translate("MainWindow", "Y axis:"))
        self.lb_XaxisName.setText(_translate("MainWindow", "..."))
        self.lb_YaxisName.setText(_translate("MainWindow", "..."))
        self.gb_simPreferences.setTitle(_translate("MainWindow", "Simulation Preferences"))
        self.lb_sweepParameter.setText(_translate("MainWindow", "Sweep Parameter:"))
        self.cb_sweepParameter.setItemText(0, _translate("MainWindow", "W"))
        self.cb_sweepParameter.setItemText(1, _translate("MainWindow", "L"))
        self.cb_sweepParameter.setItemText(2, _translate("MainWindow", "VGS"))
        self.cb_sweepParameter.setItemText(3, _translate("MainWindow", "VDS"))
        self.cb_sweepParameter.setItemText(4, _translate("MainWindow", "VBS"))
        self.cb_objectiveParameter.setItemText(0, _translate("MainWindow", "ids"))
        self.cb_objectiveParameter.setItemText(1, _translate("MainWindow", "gm"))
        self.cb_objectiveParameter.setItemText(2, _translate("MainWindow", "gds"))
        self.cb_objectiveParameter.setItemText(3, _translate("MainWindow", "gmb"))
        self.lb_objectiveParameter.setText(_translate("MainWindow", "Objective:"))
        self.lb_variableParameter.setText(_translate("MainWindow", "Variable:"))
        self.cb_variableParameter.setItemText(0, _translate("MainWindow", "L"))
        self.cb_variableParameter.setItemText(1, _translate("MainWindow", "W"))
        self.lb_maxError.setText(_translate("MainWindow", "Maximum Error:"))
        self.cb_sweepStep.setItemText(0, _translate("MainWindow", "Linear"))
        self.cb_sweepStep.setItemText(1, _translate("MainWindow", "Logarithmic"))
        self.lb_sweepStep.setText(_translate("MainWindow", "Sweep step:"))
        self.lb_from.setText(_translate("MainWindow", "From:"))
        self.lb_to.setText(_translate("MainWindow", "To:"))
        self.lb_nOfSteps.setText(_translate("MainWindow", "nº of steps:"))
        self.actionNew_project.setText(_translate("MainWindow", "New project"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSimulation_options.setText(_translate("MainWindow", "Simulation options"))
        self.actionSave_csv_file.setText(_translate("MainWindow", "Save .csv file"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
