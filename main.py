
import mysql.connector


def main():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='gpp',
            passwd='1234Hola',
        )
        # database='PruebasGPP'
        print("Conexion exitosa")

        mycursor = conexion.cursor()
        mycursor.execute("SHOW DATABASES")
        result = mycursor.fetchall()
        exist = False

        for i in result:
            if str(i) == '(\'PruebasGPP\',)':
                exist = True

        if exist:
            pass
        else:
            mycursor.execute("CREATE DATABASE PruebasGPP")

        mycursor = conexion.cursor()
        mycursor.execute("SHOW DATABASES")
        result = mycursor.fetchall()
        for i in result:
            print(i)

    except Exception as e:
        print("Tenemos el siguiente error:\n")
        print(e)


if __name__ == '__main__':
    main()


