# ... (previous imports)
from scanner_agent.excel_importer import import_excel_data

# ... (existing code)

def daily_tasks():
    # Import latest competitor data
    import_excel_data()
    
    # ... (existing content creation tasks)
    
    # Process new scans
    from scanner_agent.receipt_scanner import process_pending_scans
    process_pending_scans()
