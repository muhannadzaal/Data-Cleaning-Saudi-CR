# Saudi Commercial Registration Data Cleaning 🇸🇦

This project focuses on cleaning and processing raw Saudi commercial 
registration data (2023) using Python, preparing it for analysis 
and extracting accurate insights.

## 🛠 Tools Used
* **Language:** Python 3.x
* **Libraries:** Pandas
* **Environment:** VS Code

## 🧹 Operations Performed
1. **Column Filtering:** Removed low-quality columns with missing 
   values reaching 63% (48,997 rows) to ensure data integrity.
2. **Handling Missing Values:** Filled capital values with (0) 
   instead of nulls, and replaced missing legal entity values 
   with "Unknown".
3. **Text Cleaning:** Stripped leading/trailing whitespace from 
   Arabic text fields and standardized formatting.
4. **Duplicate Removal:** Ensured no duplicate records exist 
   to guarantee reliable results.

## 📊 Impact
* **Data Quality:** Identified and removed columns with 63% 
  missing values (48,997 rows), ensuring analytical reliability.
* **Analysis-Ready Data:** Transformed raw, unstructured data 
  into a clean dataset ready for direct use in analysis.

## 📁 Repository Contents
* `Saudi_CR_Cleaning.py` — Main data processing script.
* `cleaned_data.csv` — Final cleaned dataset.

## 👤 Contact
**Mohannad Al-Shammari**
[LinkedIn](https://www.linkedin.com/in/muhannad-al-shammari-)
