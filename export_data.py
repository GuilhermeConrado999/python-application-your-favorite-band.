import sqlite3
import pandas as pd

def export_to_csv():
    try:
        # se conecte ao banco de dados
        conn = sqlite3.connect("users_songs.db")
        
        # leia a tabela atravez de um dataframe do pandas
        print("Reading data from 'users' table...")
        df = pd.read_sql_query("SELECT * FROM users", conn)
        
        # define o nome de saida
        output_file = "users_songs_export.csv"
        
        # exporte para csv
        # usaremos o index=False Portanto, não adicionamos uma coluna para o índice do DataFrame.
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
        
        conn.close()
        print(f"Success! Data exported to: {output_file}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    export_to_csv()
