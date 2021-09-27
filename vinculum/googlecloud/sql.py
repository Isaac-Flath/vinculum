import mysql.connector
from mysql.connector.constants import ClientFlag
import pandas as pd
import os

def get_config(
    user_var='GC_SQL_USER',
    pass_var='GC_SQL_PASS',
    host_var='GC_SQL_HOST',
    ssl_ca_path='~/ssl/server-ca.pem',
    ssl_cert_path='~/ssl/server-ca.pem',
    ssl_key_path='~/ssl/server-ca.pem',
    database='political_influence'
    ):
    config = {
        'user': os.getenv(user_var),
        'password': os.getenv(pass_var),
        'host': os.getenv(host_var),
        'client_flags': [ClientFlag.SSL],
        'ssl_ca': ssl_ca_path,
        'ssl_cert': ssl_cert_path,
        'ssl_key': ssl_key_path,
        'database':database
    }
    return config

def sql_connect(config=get_config()):
    '''Connect to google cloud mysql'''
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor()  # initialize connection cursor
    return cnxn, cursor

def run_sql_qry(qry, config,return_df=False):
    '''Run a sql query from a string'''
    cnxn,cursor = sql_connect(config)
    try:
        cursor.execute(qry)
        if return_df: 
            out = cursor.fetchall()
            df = pd.DataFrame(out,columns=[i[0] for i in cursor.description]))
    finally:
        cnxn.close()
    if return_df: return df

def split_sql_file(path):
    '''Loads sql file and splits on ; in case there are multiple queries'''
    with open(path, 'r') as f:
        qry = f.readlines()
    qrys = qry.split(';')
    return qrys

def run_sql_file(path,config,return_last_df=False):
    '''runs all queries in a sql query file'''
    qrys = split_sql_file(path)
    qry_cnt = len(qrys)
    for i,qry in enumerate(qrys):
        if (i == (qry_cnt -1)) and (return_last_df==True):
            run_sql_qry(qry=qry,config=config,return_last_df=return_last_df)
        else:
            run_sql_qry(qry=qry,config=config,return_last_df=False)

    