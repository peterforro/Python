import os
import psycopg2, psycopg2.extras
import urllib



class Database:


    def __init__(self):
        self.__user_name = 'peterforro'#os.environ.get('PSQL_USER')
        self.__password = 'ifur6iwillb9!'#os.environ.get('PSQL_PASSWORD')
        self.__database_name = 'telephonebook'#os.environ.get('PSQL_DB')
        self.__connection_str = f'postgresql://{self.__user_name}:{self.__password}@localhost/{self.__database_name}'



    def connect(self):
        try:
            connection = psycopg2.connect(self.__connection_str)
            connection.autocommit = True
        except psycopg2.DatabaseError as exception:
            print('Database connection problem')
            raise exception
        return connection



    def connection_handler(self,function):
        def wrapper(*args, **kwargs):
            connection = self.connect()
            dict_cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            ret_value = function(dict_cur, *args, **kwargs)
            dict_cur.close()
            connection.close()
            return ret_value
        return wrapper



    def insert(self, user_input):
        connection = self.connect()
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = ''' INSERT INTO records (name, phone, birth, email)
                    VALUES (%(name)s, %(phone)s, %(birth)s, %(email)s)  '''
        cursor.execute(query, user_input)
        cursor.close()
        connection.close()



    def get_records(self):
        connection = self.connect()
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = ''' SELECT name,birth,phone,email FROM records;  '''
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result



    def delete_records(self):
        connection = self.connect()
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = ''' DELETE FROM records;    '''
        cursor.execute(query)
        cursor.close()
        connection.close()
