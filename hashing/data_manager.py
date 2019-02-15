from database_common import connection_handler
from psycopg2 import sql
import bcrypt



def hash_password(plain_text_password):
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')



def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)





@connection_handler
def set_data(cursor, **kwargs):
    for key in kwargs:
        query = sql.SQL(    """ UPDATE hash
                                SET {}=%(value)s""").format(sql.Identifier(key));
        params = {'value':kwargs[key]}
        cursor.execute(query,params)







@connection_handler
def get_data(cursor):
    query = """ SELECT * FROM hash;"""
    cursor.execute(query)
    return cursor.fetchone()


