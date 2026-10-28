# pip install mysqlclient
import MySQLdb

# create database clinica_db;
def test():
    try:
        conexion = MySQLdb.connect(host="localhost", user="root", passwd="", db="echotech_db")
        print("Conexion exitosa!")
        cursor = conexion.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()[0]
        print(f"Version del servidor: {version}")
        conexion.close()
    except MySQLdb.Error as e:
        print(f"Error: {e}")

test()