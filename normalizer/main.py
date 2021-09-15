# from pymongo.helpers import _fields_list_to_dict
from src.mongo import mongo
from src.mysql import MySQL
from src.validation import completeness
from src.record import record

queue = mongo().find(collection="raw", query={"$or": [{"status": 0}, {"status": None}]}, fields={"status": 1})

for q in queue:
    item = mongo().find(collection="raw", query={"_id": q["_id"]})
    item = item[0]
    completeness(item)
    item_processed = record(item)
    MySQL().insert_warm(item_processed)
    mongo().update_one(collection="raw", query={"_id": q["_id"]}, update={ "$set": { "status": 1 } })
