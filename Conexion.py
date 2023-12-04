import psycopg2
class Conexion:
    __cur = None
    __con = None
    def conectar(self):
        conn = psycopg2.connect(
        database="proyectocurso", user='postgres', password='vordank', host='127.0.0.1', port= '5432'
        )
        self.__cur = conn.cursor()
        self.__con = conn
    def desconectar(self):
        self.__con.close()
    def c(self):
        return self.__cur
    def grabar(self):
        self.__con.commit()