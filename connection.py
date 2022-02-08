import mysql.connector

def create_connection(host, user, password, database):
    return mysql.connector.connect(host=host, user=user, password=password, database=database)


def close_connection(con):
    return con.close()