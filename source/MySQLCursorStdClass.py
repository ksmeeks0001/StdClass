from mysql.connector import cursor

class MySQLCursorStdClass(cursor.MySQLCursorDict):
    """
    Return rows from MysqlCursor with dot access

    connection:
        mysql-connector-python connection

    class_name:
        Optional name of a subclass of StdClass
    """

    def __init__(self, connection, class_name=StdClass):
        self._cls = class_name

        super().__init__(connection)
        
    def _row_to_python(self, rowdata, desc=None):
        """
        Overide the base class function to return StdClass
        """
        return self._cls(super(MySQLCursorStdClass, self)._row_to_python(rowdata, desc))
