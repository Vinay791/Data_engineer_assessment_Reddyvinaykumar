USE home_db;

/********** PROPERTY TABLE **********/

CREATE TABLE property (
  property_id INT AUTO_INCREMENT PRIMARY KEY,
  property_title VARCHAR(255),
  address VARCHAR(255),
  reviewed_status VARCHAR(100),
  most_recent_status VARCHAR(100),
  source VARCHAR(100),
  market VARCHAR(100),
  occupancy VARCHAR(50),
  flood VARCHAR(50),
  street_address VARCHAR(255),
  city VARCHAR(100),
  state CHAR(2),
  zip VARCHAR(10),
  property_type VARCHAR(100),
  highway VARCHAR(50),
  train VARCHAR(50),
  tax_rate DECIMAL(5,2),
  sqft_basement INT,
  htw VARCHAR(10),
  pool VARCHAR(10),
  commercial VARCHAR(10),
  water VARCHAR(50),
  sewage VARCHAR(50),
  year_built INT,
  sqft_mu INT,
  sqft_total VARCHAR(50),
  parking VARCHAR(50),
  bed INT,
  bath INT,
  basement_yes_no VARCHAR(10),
  layout VARCHAR(50),
  net_yield DECIMAL(5,2),
  irr DECIMAL(5,2),
  rent_restricted VARCHAR(10),
  neighborhood_rating INT,
  latitude DECIMAL(10,6),
  longitude DECIMAL(10,6),
  subdivision VARCHAR(100),
  taxes DECIMAL(10,2),
  selling_reason VARCHAR(255),
  seller_retained_broker VARCHAR(255),
  final_reviewer VARCHAR(255),
  school_average DECIMAL(5,2)
);


/************** VALUATION TABLE *************/

CREATE TABLE valuation (
  valuation_id INT AUTO_INCREMENT PRIMARY KEY,
  property_id INT,
  list_price DECIMAL(12,2),
  previous_rent DECIMAL(12,2),
  arv DECIMAL(12,2),
  zestimate DECIMAL(12,2),
  expected_rent DECIMAL(12,2),
  rent_zestimate DECIMAL(12,2),
  low_fmr DECIMAL(12,2),
  high_fmr DECIMAL(12,2),
  redfin_value DECIMAL(12,2),
  FOREIGN KEY (property_id) REFERENCES property(property_id)
);


/************* HOA TABLE **********/

CREATE TABLE hoa (
  hoa_id INT AUTO_INCREMENT PRIMARY KEY,
  property_id INT,
  hoa DECIMAL(12,2),
  hoa_flag VARCHAR(10),
  FOREIGN KEY (property_id) REFERENCES property(property_id)
);


/************* REHAB TABLE ************/

CREATE TABLE rehab (
  rehab_id INT AUTO_INCREMENT PRIMARY KEY,
  property_id INT,
  underwriting_rehab DECIMAL(12,2),
  rehab_calculation DECIMAL(12,2),
  paint VARCHAR(10),
  flooring_flag VARCHAR(10),
  foundation_flag VARCHAR(10),
  roof_flag VARCHAR(10),
  hvac_flag VARCHAR(10),
  kitchen_flag VARCHAR(10),
  bathroom_flag VARCHAR(10),
  appliances_flag VARCHAR(10),
  windows_flag VARCHAR(10),
  landscaping_flag VARCHAR(10),
  trashout_flag VARCHAR(10),
  FOREIGN KEY (property_id) REFERENCES property(property_id)
);
