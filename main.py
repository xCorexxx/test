import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlTableModel

from ui_main import Ui_MainWindow
from new_plot import Ui_Dialog
from connection import Data

class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        self.view_data()
        self.reload_data()

        self.ui.btn_add.clicked.connect(self.open_new_transaction_window)
        self.ui.btn_edit.clicked.connect(self.open_new_transaction_window)
        self.ui.btn_delete.clicked.connect(self.delete_current_transaction)


    def reload_data(self):
        self.ui.le_fact_mulcher.setText(self.conn.total_mulch())
        self.ui.le_fact_ech.setText(self.conn.total_ech())
        self.ui.le_fact_davs.setText(self.conn.total_davs())
        self.ui.le_fact_pod.setText(self.conn.total_pod())


    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('expenses')
        self.model.select()
        self.ui.tableView.setModel(self.model)
    def open_new_transaction_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        sender = self.sender()
        if sender.text() == "Добавить участок":
            self.ui_window.btn_save.clicked.connect(self.add_new_transaction)
        else:
            self.ui_window.btn_save.clicked.connect(self.edit_current_transaction)

    def add_new_transaction(self):
        date = self.ui_window.data.text()
        prod = self.ui_window.cb_prod.currentText()
        PLOT = self.ui_window.le_plot.text()
        km1 =self.ui_window.le_plot_2.text()
        pk1 = self.ui_window.le_plot_3.text()
        km2 = self.ui_window.le_plot_4.text()
        pk2 = self.ui_window.le_plot_5.text()
        km = self.ui_window.le_tree_2.text()
        tree = self.ui_window.le_tree.text()

        self.conn.add_new_transaction_query(date, prod, PLOT, km1, pk1, km2, pk2, km, tree)
        self.view_data()
        self.reload_data()
        self.new_window.close()

    def edit_current_transaction(self):
        index  = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))

        date = self.ui_window.data.text()
        prod = self.ui_window.cb_prod.currentText()
        PLOT = self.ui_window.le_plot.text()
        km1 = self.ui_window.le_plot_2.text()
        pk1 = self.ui_window.le_plot_3.text()
        km2 = self.ui_window.le_plot_4.text()
        pk2 = self.ui_window.le_plot_5.text()
        km = self.ui_window.le_tree_2.text()
        tree = self.ui_window.le_tree.text()

        self.conn.update_transaction_query(date, prod, PLOT, km1, pk1, km2, pk2, km, tree, id)
        self.view_data()
        self.reload_data()
        self.new_window.close()

    def delete_current_transaction(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))

        self.conn.delete_transaction_query(id)
        self.view_data()
        self.reload_data()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())