from moviepy.editor import ImageClip, concatenate_videoclips
import textwrap
import requests

def generate_content(platform, business_tier, language="English"):
    """Creates 15-sec demo videos/GIFs showing receipt scanning"""
    # Step 1: Simulate receipt scanning
    scan_visual = ImageClip("assets/sample_receipt.jpg").set_duration(3)
    
    # Step 2: Show competitor price comparison
    comparison_screen = (ImageClip("assets/comparison_template.png")
                        .set_duration(5)
                        .text("Spar: R45\nCheckers: R39\nMakro: R37", 
                              fontsize=24, color='white'))
    
    # Step 3: Add savings calculation
    savings_frame = (ImageClip("assets/savings_bg.png")
                    .set_duration(4)
                    .text(f"Save 23% | R18 back!", 
                          fontsize=30, color='green'))
    
    # Step 4: Localized messaging
    messages = {
        "SMB": "Spaza shops: Never overpay again!",
        "Medium": "Optimize business purchases",
        "Enterprise": "Global procurement intelligence"
    }
    caption = textwrap.fill(messages[business_tier], width=30)
    
    # Compile video
    final_clip = concatenate_videoclips([scan_visual, comparison_screen, savings_frame])
    final_clip.write_videofile(f"{platform}_demo.mp4", fps=24)
    
    return f"{platform}_demo.mp4"
