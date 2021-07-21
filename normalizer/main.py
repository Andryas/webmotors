# from pymongo.helpers import _fields_list_to_dict
from src.mongo import mongo
from src.mysql import MySQL
from src.validation import completeness
from src.record import record

queue = mongo().find(collection="raw", query={"$or": [{"status": 0}, {"status": None}]}, fields={"status": 1}, limit = 2)

# if len(queue) > 0:
# for q in queue:
q = queue[0]
item = mongo().find(collection="raw", query={"_id": q["_id"]})
item = item[0]
completeness(item)
item_processed = record(item)


new_record = item_processed
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="rootteste",
    database="crawler"
    # auth_plugin='mysql_native_password'
)
cursor = conn.cursor(())

query = """INSERT INTO warm (id_unique, channels, fipe_percent, hot_deal, price,search_price, seller_ad_type, seller_budget_invest, seller_car_delivery,seller_city, seller_dealer_score, seller_exceeded_plan, seller_type,seller_state, seller_troca_com_troco, spec_armored, spec_body_type,spec_color_primary, spec_make, spec_model, spec_ports, spec_odometer,spec_title, spec_transmission, spec_attrs, spec_version,spec_year_fabrication, spec_year_model) VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s) 
"""%new_record

    
print(query)
cursor.execute(query, new_record)
conn.commit()

