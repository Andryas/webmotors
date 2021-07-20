CREATE DATABASE IF NOT EXISTS crawler;
USE crawler;
CREATE TABLE IF NOT EXISTS `warm` (
    id_unique BIGINT UNIQUE,
    channels TEXT,
    fipe_percent INT, 
    hot_deal TEXT,
    price DOUBLE,
    search_price DOUBLE,
    seller_ad_type VARCHAR(50),
    seller_budget_invest DOUBLE,
    seller_car_delivery TINYINT,
    seller_city TEXT,
    seller_dealer_score DOUBLE,
    seller_exceeded_plan TINYINT,
    seller_type CHAR(2),
    seller_state TEXT,
    seller_troca_com_troco TINYINT,
    spec_armored CHAR(1),
    spec_body_type TEXT,
    spec_color_primary TEXT,
    spec_make TEXT,
    spec_model TEXT,
    spec_ports INT,
    spec_odometer DOUBLE,
    spec_title TEXT,
    spec_transmission VARCHAR(20),
    spec_attrs TEXT,
    spec_version TEXT,
    spec_year_fabrication INT,
    spec_year_model INT 
);