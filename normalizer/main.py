from src.periferics.mongo import mongo

prop = mongo().find(collection='raw', limit=1)
prop = prop[0]
