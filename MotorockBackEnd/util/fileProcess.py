# -*- coding: utf-8 -*-
import pandas as pd
import psycopg2.errors
import psycopg2.extras as extras

DB = 'motorock'
USER = 'usr_motorock'
PWD = '@W9q4x6r1'
HOST = '127.0.0.1'
PORT = '5432'

conn = psycopg2.connect( 
    database=DB, user=USER, password=PWD, host=HOST, port=PORT
) 


def read_transform_csv(file):
    csv = pd.read_csv(file, encoding='utf8', sep=';') #pd.read_csv("MotorockBackend/util/eye-vendas-11-10-2024.csv", encoding="utf8", delimiter=";")
    df = csv[["#", "Horário", "forma de pagamento", "Total", "Usuário"]]
    df = df.rename(columns={"#":"ID_TRANSACAO","Horário":"DATAHORATRANSACAO","forma de pagamento":"TIPOPAGAMENTO", "Total":"VL_VENDA", "Usuário":"USR_VENDA"})
    

    df['VL_VENDA'] = df['VL_VENDA'].str.replace(',','.').astype('float')
    df['DT_VENDA'] = pd.to_datetime(df["DATAHORATRANSACAO"]).dt.date
    df["HR_VENDA"] = pd.to_datetime(df["DATAHORATRANSACAO"]).dt.time
    
    return df


def load_sales_table(conn, df, table):

    tuples = [tuple(x) for x in df.to_numpy()] 
    cols = ','.join(list(df.columns)) 
    
    # SQL query to execute 
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols) 
    cursor = conn.cursor() 
    try: 
        extras.execute_values(cursor, query, tuples) 
        conn.commit() 
    except Exception as error: 
        print("Error: %s" % error) 
        conn.rollback() 
        cursor.close() 
        raise Exception(f"Error insert data: {error}")
    finally:
        cursor.close() 

