import sqlite3
import pandas as pd
from excel_importer import get_competitor_prices

DB_PATH = "./assets/price_database/price_comparison.db"

def compare_prices(product_name):
    """Compare scanned price with competitors"""
    # Get competitor data
    comp_prices = get_competitor_prices(product_name)
    
    if comp_prices.empty:
        print(f"No competitor data found for {product_name}")
        return None
    
    # Calculate savings
    avg_price = comp_prices['price'].mean()
    min_price = comp_prices['price'].min()
    
    # Connect to scanned data
    conn = sqlite3.connect(DB_PATH)
    scanned_price = pd.read_sql_query(
        f"SELECT price FROM scanned_data WHERE product LIKE '%{product_name}%'",
        conn
    )['price'].iloc[0]
    
    # Generate report
    report = {
        'product': product_name,
        'your_price': scanned_price,
        'average_price': round(avg_price, 2),
        'best_price': min_price,
        'potential_savings': round(scanned_price - min_price, 2),
        'retailers': comp_prices[['retailer', 'price']].to_dict('records')
    }
    
    print(f"Price comparison for {product_name}:")
    print(f"  You paid: R{scanned_price}")
    print(f"  Best price: R{min_price} (Save R{report['potential_savings']})")
    
    # Trigger marketing content creation
    from marketing_agent.content_creator import generate_comparison_content
    generate_comparison_content(report)
    
    return report
