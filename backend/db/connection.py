import psycopg2
import dotenv

psw = dotenv.dotenv_values(".env")["DB_PASSWORD"]
def conection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password=psw
        )
        return conn
    except Exception as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None
    
    