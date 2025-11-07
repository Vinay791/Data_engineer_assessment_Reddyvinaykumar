# Data Engineering Assessment

Welcome!  
This exercise evaluates your core **data-engineering** skills:

| Competency | Focus                                                         |
| ---------- | ------------------------------------------------------------- |
| SQL        | relational modelling, normalisation, DDL/DML scripting        |
| Python ETL | data ingestion, cleaning, transformation, & loading (ELT/ETL) |

---

## 0 Prerequisites & Setup

> **Allowed technologies**

- **Python ≥ 3.8** – all ETL / data-processing code
- **MySQL 8** – the target relational database
- **Pydantic** – For data validation
- List every dependency in **`requirements.txt`** and justify selection of libraries in the submission notes.

---

## 1 Clone the skeleton repo

```
git clone https://github.com/100x-Home-LLC/data_engineer_assessment.git
```

✏️ Note: Rename the repo after cloning and add your full name.

**Start the MySQL database in Docker:**

```
docker-compose -f docker-compose.initial.yml up --build -d
```

- Database is available on `localhost:3306`
- Credentials/configuration are in the Docker Compose file
- **Do not change** database name or credentials

For MySQL Docker image reference:
[MySQL Docker Hub](https://hub.docker.com/_/mysql)

---

### Problem

- You are provided with a raw JSON file containing property records is located in data/
- Each row relates to a property. Each row mixes many unrelated attributes (property details, HOA data, rehab estimates, valuations, etc.).
- There are multiple Columns related to this property.
- The database is not normalized and lacks relational structure.
- Use the supplied Field Config.xlsx (in data/) to understand business semantics.

### Task

- **Normalize the data:**

  - Develop a Python ETL script to read, clean, transform, and load data into your normalized MySQL tables.
  - Refer the field config document for the relation of business logic
  - Use primary keys and foreign keys to properly capture relationships

- **Deliverable:**
  - Write necessary python and sql scripts
  - Place your scripts in `src/`
  - The scripts should take the initial json to your final, normalized schema when executed
  - Clearly document how to run your script, dependencies, and how it integrates with your database.

---

## Submission Guidelines

- Edit the section to the bottom of this README with your solutions and instructions for each section at the bottom.
- Ensure all steps are fully **reproducible** using your documentation
- DO NOT MAKE THE REPOSITORY PUBLIC. ANY CANDIDATE WHO DOES IT WILL BE AUTO REJECTED.
- Create a new private repo and invite the reviewer https://github.com/mantreshjain and https://github.com/siddhuorama

---

**Good luck! We look forward to your submission.**

## Solutions and Instructions (Filed by Candidate)

**Document your solution here:**

Project Documentation – Data Engineer Assessment
### 1. Overview

This project processes property data from JSON, transforms it, and loads it into a MySQL database using an ETL Python script. The project demonstrates data cleaning, handling nested data, and database management.
### 2. Repository Contents

schema.sql – SQL schema to create required tables in MySQL.

etl_script.py – Python ETL script that reads JSON, cleans/transforms data, and loads it into the database.

data/fake_property_data_new.json – Sample property data in JSON format.

Field Config.xlsx – Reference for field names and data types.

### 3. Database Schema

Database: home_db 

Tables:

### property
| Column              | Type    | Description             |
| ------------------- | ------- | ----------------------- |
| Property_Title      | VARCHAR | Full property title     |
| Address             | VARCHAR | Full address            |
| Reviewed_Status     | VARCHAR | Review status           |
| Most_Recent_Status  | VARCHAR | Latest status           |
| Source              | VARCHAR | Data source             |
| Market              | VARCHAR | Market city/region      |
| Occupancy           | VARCHAR | Occupancy info          |
| Flood               | VARCHAR | Flood info              |
| Street_Address      | VARCHAR | Street address          |
| City                | VARCHAR | City name               |
| State               | VARCHAR | State code              |
| Zip                 | VARCHAR | Zip code                |
| Property_Type       | VARCHAR | Type of property        |
| Highway             | VARCHAR | Highway proximity       |
| Train               | VARCHAR | Train proximity         |
| Tax_Rate            | FLOAT   | Tax rate                |
| SQFT_Basement       | INT     | Basement area           |
| HTW                 | VARCHAR | Heat/Water info         |
| Pool                | VARCHAR | Pool availability       |
| Commercial          | VARCHAR | Commercial property     |
| Water               | VARCHAR | Water source            |
| Sewage              | VARCHAR | Sewage type             |
| Year_Built          | INT     | Year built              |
| SQFT_MU             | INT     | Main unit area          |
| SQFT_Total          | VARCHAR | Total square feet       |
| Parking             | VARCHAR | Parking type            |
| Bed                 | INT     | Number of bedrooms      |
| Bath                | INT     | Number of bathrooms     |
| Layout              | VARCHAR | Property layout         |
| Net_Yield           | FLOAT   | Net yield percentage    |
| IRR                 | FLOAT   | Internal Rate of Return |
| Rent_Restricted     | VARCHAR | Rent restriction info   |
| Neighborhood_Rating | INT     | Neighborhood rating     |
| Latitude            | FLOAT   | Latitude coordinate     |
| Longitude           | FLOAT   | Longitude coordinate    |
| Subdivision         | VARCHAR | Subdivision name        |
| Taxes               | FLOAT   | Property taxes          |
| Selling_Reason      | VARCHAR | Reason for sale         |
| Final_Reviewer      | VARCHAR | Reviewer name           |
| School_Average      | FLOAT   | School rating           |

### Table: valuation

Linked to: property (via property_id)

Purpose: Stores multiple valuation entries per property

| Column         | Description           |
| -------------- | --------------------- |
| List_Price     | Listing price         |
| Previous_Rent  | Previous rental value |
| ARV            | After Repair Value    |
| Rent_Zestimate | Rent Zestimate        |
| Low_FMR        | Low Fair Market Rent  |
| High_FMR       | High Fair Market Rent |
| Redfin_Value   | Redfin valuation      |

### Table: hoa

Linked to: property (via property_id)

Purpose: Stores multiple HOA records per property.

| Column   | Description           |
| -------- | --------------------- |
| HOA      | HOA amount            |
| HOA_Flag | HOA availability flag |

### Table: rehab

Linked to: property (via property_id)

Purpose: Stores rehab and maintenance-related information.

| Column             | Description              |
| ------------------ | ------------------------ |
| Underwriting_Rehab | Underwriting rehab value |
| Rehab_Calculation  | Rehab cost estimation    |
| Paint              | Paint flag               |
| Flooring_Flag      | Flooring flag            |
| Foundation_Flag    | Foundation flag          |
| Roof_Flag          | Roof flag                |
| HVAC_Flag          | HVAC flag                |
| Kitchen_Flag       | Kitchen flag             |
| Bathroom_Flag      | Bathroom flag            |
| Appliances_Flag    | Appliances flag          |
| Windows_Flag       | Windows flag             |
| Landscaping_Flag   | Landscaping flag         |
| Trashout_Flag      | Trashout flag            |


### 4. ETL Process

Extract – Read JSON data from fake_property_data_new.json.

Transform – Clean data, handle missing/null values, and flatten nested structures (valuation, HOA, rehab) to load into separate tables.

Load – Insert data into MySQL tables (property, valuation, hoa, rehab) with proper foreign key relationships.

### 5. Running the Project
   
   Start MySQL using Docker Compose
   Use the provided docker-compose.initial.yml file to build and run the MySQL container automatically:
  
   ```
     docker-compose -f docker-compose.initial.yml up --build -d
   ```
This command will:

Pull the MySQL image if not already available.

Build using Dockerfile.final_db.

Create and start a container named mysql_ctn.

Set up the database home_db

database runs on port 3306.

Step 2: Apply SQL Schema

Run the following command to create the tables inside the database:
```
docker exec -i mysql_ctn_final mysql -uusername -ppassword home_db < schema.sql
```
This command connects to the MySQL container and executes all the SQL statements in schema.sql.

✏️ Note: Take database user name and password from docker compose file

Step 3: Run the ETL Script

Now, execute the Python ETL script that reads the JSON file, cleans the data, and loads it into the MySQL tables:
```
python3 etl_script.py
```
Step 4: Connect to the Database (Inside Container)

To open the MySQL shell inside the running container:
```
docker exec -it container_id  -u username -p
```
You’ll be inside the MySQL command-line interface (CLI).

✏️ Note: enter the password of the database user ,then you will connected to mysql

You can now run SQL queries

Next connect Database home_db by typing 
```
USE home_db;
```
Then run the sql query to see tables
```
SHOW tables;
```
you can see four tables

| Tables in `home_db` |
|----------------------|
| property             |
| valuation            |
| rehab                |
| hoa                  |


To see the data in the tables run this query 
```
SELECT * FROM {tablename};
```
To exit MySQL, type:
```
exit
```
Step 5: Stop the Container

When you are done, stop and remove the running container:
```
sudo docker-compose -f docker-compose.initial.yml down
```
   
