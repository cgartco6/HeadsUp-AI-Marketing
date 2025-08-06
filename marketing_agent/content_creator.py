# ... (previous imports)
from scanner_agent.price_comparator import compare_prices

# ... (existing functions)

def generate_comparison_content(report):
    """Create visual content based on price comparison"""
    # Create comparison graphic
    comp_text = "\n".join([f"{r['retailer']}: R{r['price']}" 
                          for r in report['retailers'][:3])
    
    # Generate visual
    img = Image.new('RGB', (800, 600), color='white')
    d = ImageDraw.Draw(img)
    
    # Add product title
    d.text((50, 50), f"Price Comparison: {report['product']}", fill='black', font=font_large)
    
    # Add price comparison
    d.text((50, 150), f"Your Price: R{report['your_price']}", fill='red', font=font_medium)
    d.text((50, 200), "Competitor Prices:", fill='black', font=font_medium)
    d.text((70, 250), comp_text, fill='black', font=font_small)
    
    # Add savings
    d.text((50, 400), f"Potential Savings: R{report['potential_savings']}", 
           fill='green', font=font_large)
    
    # Save and return
    img.save(f"comparison_{report['product']}.png")
    return img
