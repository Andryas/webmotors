# from pymongo.helpers import _fields_list_to_dict
from src.mongo import mongo
from src.validation import completeness
from src.record import record

queue = mongo().find(collection="raw", query={"$or": [{"status": 0}, {"status": None}]}, fields={"status": 1}, limit = 2)

# for q in queue:
q = queue[0]
item = mongo().find(collection="raw", query={"_id": q["_id"]})
item = item[0]
completeness(item)
item_processed = record(item)
# TODO insert mysql
# TODO update mongo status -> 1

    