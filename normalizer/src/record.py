def record(item):
    id_unique = item["UniqueId"]

    if item["Channels"]:
        channels = []
        for c in item["Channels"]:
            channels.append(c["Value"])
        channels.sort()
        channels = ",".join(channels)
    else:
        channels = None

    fipe_percent = item["FipePercent"]

    if item["HotDeal"]:
        hot_deal = []
        for c in item["HotDeal"]:
            hot_deal.append(c["Value"])
        hot_deal.sort()
        hot_deal = ",".join(hot_deal)
    else:
        hot_deal = None

    price = item["Prices"]["Price"]
    search_price = item["Prices"]["SearchPrice"]

    seller_ad_type = item["Seller"]["AdType"]["Value"]
    seller_budget_invest = item["Seller"]["BudgetInvestimento"]
    seller_car_delivery = item["Seller"]["CarDelivery"]
    seller_city = item["Seller"]["City"]
    seller_dealer_score = item["Seller"]["DealerScore"]
    seller_exceeded_plan = item["Seller"]["ExceededPlan"]
    seller_type = item["Seller"]["SellerType"]
    seller_state = item["Seller"]["State"]
    seller_troca_com_troco = item["Seller"]["TrocaComTroco"]

    spec_armored = item["Specification"]["Armored"]
    spec_armored = 0 if spec_armored == "N" else 1
    spec_body_type = item["Specification"]["BodyType"]
    spec_color_primary = item["Specification"]["Color"]["Primary"]
    spec_make = item["Specification"]["Make"]["Value"]
    spec_model = item["Specification"]["Model"]["Value"]
    spec_ports = item["Specification"]["NumberPorts"]
    spec_odometer = item["Specification"]["Odometer"]
    spec_title = item["Specification"]["Title"]
    spec_transmission = item["Specification"]["CVT"]
    
    if item["Specification"]["VehicleAttributes"]:
        spec_attrs = []
        for c in item["Specification"]["VehicleAttributes"]:
            spec_attrs.append(c["Name"])
        spec_attrs.sort()
        spec_attrs = ",".join(spec_attrs)
    else:
        spec_attrs = None
    
    spec_version = item["Specification"]["Version"]["Value"]
    spec_year_fabrication = item["Specification"]["YearFabrication"]
    spec_year_model = item["Specification"]["YearModel"]

    new_record = {
        "id_unique": id_unique,
        "channels": channels,
        "fipe_percent": fipe_percent,
        "hot_deal": hot_deal,
        "price": price,
        "search_price": search_price,
        "seller_ad_type": seller_ad_type,
        "seller_budget_invest": seller_budget_invest,
        "seller_car_delivery": int(seller_car_delivery),
        "seller_city": seller_city,
        "seller_dealer_score": seller_dealer_score,
        "seller_exceeded_plan": int(seller_exceeded_plan),
        "seller_type": seller_type,
        "seller_state": seller_state,
        "seller_troca_com_troco": int(seller_troca_com_troco),
        "spec_armored": spec_armored,
        "spec_body_type": spec_body_type,
        "spec_color_primary": spec_color_primary,
        "spec_make": spec_make,
        "spec_model": spec_model,
        "spec_ports": spec_ports,
        "spec_odometer": spec_odometer,
        "spec_title": spec_title,
        "spec_transmission": spec_transmission,
        "spec_attrs": spec_attrs,
        "spec_version": spec_version,
        "spec_year_fabrication": spec_year_fabrication,
        "spec_year_model": spec_year_model
    }
    
    return(new_record)
