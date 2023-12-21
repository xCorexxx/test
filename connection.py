from PySide6 import QtWidgets, QtSql


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('expense_db.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS expenses (ID integer primary key AUTOINCREMENT, Date VARCHAR(20), "
                   " prod VARCHAR(20) , PLOT VARCHAR(20), km1 VARCHAR(20), pk1 VARCHAR (20), km2 VARCHAR(20), pk2 VARCHAR (20),  km VARCHAR (20), tree VARCHAR(20))")
        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()

        return query

    def add_new_transaction_query(self, date, prod, PLOT, km1, pk1, km2, pk2, km, tree):
        sql_query = "INSERT INTO expenses (date, prod,  PLOT, km1, pk1, km2, pk2, km, tree) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [date, prod, PLOT, km1, pk1, km2, pk2, km, tree])

    def update_transaction_query(self, date, prod, PLOT, km1, pk1, km2, pk2, km, tree, id):
        sql_query = "UPDATE expenses SET date=?, prod=?, PLOT=?, km1=?, pk1=?, km2=?, pk2=?, km=?, tree=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [date, prod, PLOT, km1, pk1, km2, pk2, km, tree, id])

    def delete_transaction_query(self, id):
        sql_query = "DELETE FROM expenses WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

    def get_total(self, column, filter=None, value=None):
        sql_query = f"SELECT SUM({column}) FROM expenses"

        if filter is not None and value is not None:
            sql_query += f" WHERE {filter} = ?"

        query_values = []

        if value is not None:
            query_values.append(value)

        query = self.execute_query_with_params(sql_query, query_values)

        if query.next():
            return str(query.value(0))

    def total(self):
        return self.get_total(column="km")

    def total_mulch(self):
        return self.get_total(column="km", filter="prod", value="Мульчер")

    def total_davs(self):
        return self.get_total(column="km", filter="prod", value="ДАВС")

    def total_pod(self):
        return self.get_total(column="km", filter="prod", value="Под. организация")

    def total_ech(self):
        return self.get_total(column="km", filter="prod", value="Эксп. персонал")
