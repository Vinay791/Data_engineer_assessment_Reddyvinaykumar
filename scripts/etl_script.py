import json
import pandas as pd
from sqlalchemy import create_engine
import os


# Database connection configuration

DB_USER = os.getenv("MYSQL_USER", "root")
DB_PASS = os.getenv("MYSQL_PASSWORD", "6equj5_root")
DB_HOST = os.getenv("MYSQL_HOST", "localhost")
DB_NAME = os.getenv("MYSQL_DATABASE", "home_db")
DB_PORT = os.getenv("MYSQL_PORT", "3306")

# Create SQLAlchemy engine
engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")


# Load JSON file

json_file = "/home/shyam/data_engineer_assessment/data/fake_property_data_new.json"

with open(json_file, "r") as f:
    data = json.load(f)


# Process Property Data

property_rows = []
valuation_rows = []
hoa_rows = []
rehab_rows = []

for prop in data:
    # Insert into property table
    property_id = len(property_rows) + 1
    property_rows.append({
        "property_id": property_id,
        "Property_Title": prop.get("Property_Title"),
        "Address": prop.get("Address"),
        "Reviewed_Status": prop.get("Reviewed_Status") or None,
        "Most_Recent_Status": prop.get("Most_Recent_Status"),
        "Source": prop.get("Source"),
        "Market": prop.get("Market"),
        "Occupancy": prop.get("Occupancy"),
        "Flood": prop.get("Flood"),
        "Street_Address": prop.get("Street_Address"),
        "City": prop.get("City"),
        "State": prop.get("State"),
        "Zip": prop.get("Zip"),
        "Property_Type": prop.get("Property_Type"),
        "Highway": prop.get("Highway"),
        "Train": prop.get("Train"),
        "Tax_Rate": prop.get("Tax_Rate"),
        "SQFT_Basement": prop.get("SQFT_Basement"),
        "HTW": prop.get("HTW"),
        "Pool": prop.get("Pool"),
        "Commercial": prop.get("Commercial"),
        "Water": prop.get("Water"),
        "Sewage": prop.get("Sewage"),
        "Year_Built": prop.get("Year_Built"),
        "SQFT_MU": prop.get("SQFT_MU"),
        "SQFT_Total": prop.get("SQFT_Total"),
        "Parking": prop.get("Parking"),
        "Bed": prop.get("Bed"),
        "Bath": prop.get("Bath"),
        "Basement_yes_no": prop.get("Basement_yes_no"),
        "Layout": prop.get("Layout"),
        "Net_Yield": prop.get("Net_Yield"),
        "IRR": prop.get("IRR"),
        "Rent_Restricted": prop.get("Rent_Restricted"),
        "Neighborhood_Rating": prop.get("Neighborhood_Rating"),
        "Latitude": prop.get("Latitude"),
        "Longitude": prop.get("Longitude"),
        "Subdivision": prop.get("Subdivision"),
        "Taxes": prop.get("Taxes"),
        "Selling_Reason": prop.get("Selling_Reason"),
        "Seller_Retained_Broker": prop.get("Seller_Retained_Broker"),
        "Final_Reviewer": prop.get("Final_Reviewer"),
        "School_Average": prop.get("School_Average")
    })

    # Insert Valuation
    if prop.get("Valuation"):
        for v in prop["Valuation"]:
            valuation_rows.append({
                "property_id": property_id,
                "List_Price": v.get("List_Price"),
                "Previous_Rent": v.get("Previous_Rent"),
                "ARV": v.get("ARV"),
                "Rent_Zestimate": v.get("Rent_Zestimate"),
                "Low_FMR": v.get("Low_FMR"),
                "High_FMR": v.get("High_FMR"),
                "Redfin_Value": v.get("Redfin_Value"),
                "Zestimate": v.get("Zestimate"),
                "Expected_Rent": v.get("Expected_Rent")
            })

    # Insert HOA
    if prop.get("HOA"):
        for h in prop["HOA"]:
            hoa_rows.append({
                "property_id": property_id,
                "HOA": h.get("HOA"),
                "HOA_Flag": h.get("HOA_Flag")
            })

    # Insert Rehab
    if prop.get("Rehab"):
        for r in prop["Rehab"]:
            rehab_rows.append({
                "property_id": property_id,
                "Underwriting_Rehab": r.get("Underwriting_Rehab"),
                "Rehab_Calculation": r.get("Rehab_Calculation"),
                "Paint": r.get("Paint"),
                "Flooring_Flag": r.get("Flooring_Flag"),
                "Foundation_Flag": r.get("Foundation_Flag"),
                "Roof_Flag": r.get("Roof_Flag"),
                "HVAC_Flag": r.get("HVAC_Flag"),
                "Kitchen_Flag": r.get("Kitchen_Flag"),
                "Bathroom_Flag": r.get("Bathroom_Flag"),
                "Appliances_Flag": r.get("Appliances_Flag"),
                "Windows_Flag": r.get("Windows_Flag"),
                "Landscaping_Flag": r.get("Landscaping_Flag"),
                "Trashout_Flag": r.get("Trashout_Flag")
            })


# Load Data into MySQL

df_property = pd.DataFrame(property_rows)
df_valuation = pd.DataFrame(valuation_rows)
df_hoa = pd.DataFrame(hoa_rows)
df_rehab = pd.DataFrame(rehab_rows)

# Insert into MySQL tables
with engine.begin() as conn:
    df_property.to_sql('property', conn, if_exists='append', index=False)
    df_valuation.to_sql('valuation', conn, if_exists='append', index=False)
    df_hoa.to_sql('hoa', conn, if_exists='append', index=False)
    df_rehab.to_sql('rehab', conn, if_exists='append', index=False)

print("✅ ETL completed successfully! Data loaded into MySQL.")

