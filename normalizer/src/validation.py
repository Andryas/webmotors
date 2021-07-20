def completeness(item):
    fields = ["UniqueId", "Channels", "FipePercent", "HotDeal"]
    fields_list = {"Prices": ["Price", "SearchPrice"], "Seller": ["AdType", "BudgetInvestimento", "CarDelivery", "City", "DealerScore", "ExceededPlan", "SellerType", "State", "TrocaComTroco"], "Specification": ["Armored", "BodyType", "Color", "Make", "Model", "NumberPorts", "Odometer", "Title", "CVT", "VehicleAttributes", "Version", "YearFabrication", "YearModel"]}
    
    fields_missing = list(set(fields) - set(item.keys()))
    for attr in fields_missing:
        item[attr] = None

    fields_list_missing = list(set(fields_list.keys()) - set(item.keys()))
    for attr in fields_list_missing:
        for sub_attr in item[attr]:
            item[attr][sub_attr] = None
    
    for attr in list(fields_list.keys()):
        sub_fields_missing = list(set(fields_list[attr]) - set(item[attr].keys()))
        for sub_attr in sub_fields_missing:
            item[attr][sub_attr] = None
