import mysql.connector
from settings import *

class MySQL():
    conn = None

    def __init__(self):
        self.connect()

    @classmethod
    def connect(self):
        if self.conn is None:
            self.conn = mysql.connector.connect(
                host=HOST_MSQL,
                database=DATABASE_MYSQL,
                user=USER_MYSQL,
                password=PASSWORD_MYSQL
            )
        return self.conn
    
    def close_connection(self):
        self.conn.close()
        print("MySQL connection is closed")

    def show_databases(self):
        cursor = self.conn.cursor()
        databases = ("show databases")
        cursor.execute(databases)
        for (databases) in cursor:
            print(databases[0])

    def show_tables(self):
        cursor = self.conn.cursor()
        tables = ("show tables")
        cursor.execute(tables)
        for (tables) in cursor:
            print(tables[0])

    def insert_warm(self, new_record):
        cursor = self.conn.cursor()
        
        try:
            query = """
                    INSERT INTO warm (id_unique, channels, fipe_percent, hot_deal, price, search_price, seller_ad_type, seller_budget_invest, seller_car_delivery, seller_city, seller_dealer_score, seller_exceeded_plan, seller_type, seller_state, seller_troca_com_troco, spec_armored, spec_body_type, spec_color_primary, spec_make, spec_model, spec_ports, spec_odometer, spec_title, spec_transmission, spec_attrs, spec_version, spec_year_fabrication, spec_year_model) 
                    VALUES (
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                    ) 
            """
            print(query)

            cursor.execute(query, new_record)
            self.conn.commit()
            print("Record inserted successfully into ~warm~ table")
            cursor.close()

        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))

        

