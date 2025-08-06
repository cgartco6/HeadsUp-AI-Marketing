import os
import pandas as pd
import sqlite3
from datetime import datetime

# Configuration
EXCEL_FOLDER = "./assets/price_database/"
DB_PATH = "./assets/price_database/price_comparison.db"

def import_excel_data():
    """Import all Excel files into SQLite database"""
    conn = sqlite3.connect(DB_PATH)
    
    for filename in os.listdir(EXCEL_FOLDER):
        if filename.endswith(('.xlsx', '.xls')):
            filepath = os.path.join(EXCEL_FOLDER, filename)
            retailer = os.path.splitext(filename)[0]
            
            try:
                # Read Excel file
                df = pd.read_excel(filepath)
                
                # Add retailer and timestamp
                df['retailer'] = retailer
                df['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Save to SQLite
                df.to_sql('competitor_prices', conn, if_exists='append', index=False)
                print(f"Imported {len(df)} records from {filename}")
                
            except Exception as e:
                print(f"Error importing {filename}: {str(e)}")
    
    conn.close()
    print("Price database updated successfully")

def get_competitor_prices(product_name):
    """Retrieve competitor prices for a product"""
    conn = sqlite3.connect(DB_PATH)
    query = f"""
    SELECT retailer, price, timestamp 
    FROM competitor_prices 
    WHERE product LIKE '%{product_name}%'
    ORDER BY timestamp DESC
    LIMIT 10
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

if __name__ == "__main__":
    import_excel_data()
