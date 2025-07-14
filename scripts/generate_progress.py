#!/usr/bin/env python3
"""Generate SVG progress bars for LeetCode problems"""

import os
import json
from pathlib import Path

def count_problems():
    """Count problems by difficulty"""
    problems_dir = Path("problems")
    
    counts = {
        "easy": 0,
        "medium": 0, 
        "hard": 0
    }
    
    # Count easy problems
    easy_dir = problems_dir / "1-easy"
    if easy_dir.exists():
        counts["easy"] = len([d for d in easy_dir.iterdir() if d.is_dir()])
    
    # Count medium problems  
    medium_dir = problems_dir / "2-medium"
    if medium_dir.exists():
        counts["medium"] = len([d for d in medium_dir.iterdir() if d.is_dir()])
    
    # Count hard problems
    hard_dir = problems_dir / "3-hard" 
    if hard_dir.exists():
        counts["hard"] = len([d for d in hard_dir.iterdir() if d.is_dir()])
    
    return counts

def generate_progress_svg(solved, total, color, label):
    """Generate SVG for circular progress bar"""
    
    if total == 0:
        percentage = 0
    else:
        percentage = (solved / total) * 100
    
    # Calculate stroke-dasharray for progress circle
    circumference = 2 * 3.14159 * 45  # radius = 45
    stroke_dasharray = circumference
    stroke_dashoffset = circumference - (percentage / 100) * circumference
    
    svg = f'''<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <!-- Background circle -->
  <circle cx="60" cy="60" r="45" fill="none" stroke="#e5e7eb" stroke-width="8"/>
  
  <!-- Progress circle -->
  <circle cx="60" cy="60" r="45" fill="none" stroke="{color}" stroke-width="8"
          stroke-dasharray="{stroke_dasharray}" 
          stroke-dashoffset="{stroke_dashoffset}"
          stroke-linecap="round"
          transform="rotate(-90 60 60)"/>
  
  <!-- Center text -->
  <text x="60" y="55" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#374151">
    {solved}/{total}
  </text>
  <text x="60" y="75" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#6b7280">
    {label}
  </text>
  <text x="60" y="90" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="#9ca3af">
    {percentage:.1f}%
  </text>
</svg>'''
    
    return svg

def main():
    """Generate all progress bar SVGs"""
    
    # Count current problems
    counts = count_problems()
    
    # LeetCode totals (approximate)
    totals = {
        "easy": 600,
        "medium": 1300, 
        "hard": 500
    }
    
    colors = {
        "easy": "#22c55e",     # Green
        "medium": "#f59e0b",   # Orange  
        "hard": "#ef4444"      # Red
    }
    
    labels = {
        "easy": "Easy",
        "medium": "Medium",
        "hard": "Hard"
    }
    
    # Create assets directory
    assets_dir = Path("assets")
    assets_dir.mkdir(exist_ok=True)
    
    # Generate SVGs
    for difficulty in ["easy", "medium", "hard"]:
        solved = counts[difficulty]
        total = totals[difficulty] 
        color = colors[difficulty]
        label = labels[difficulty]
        
        svg_content = generate_progress_svg(solved, total, color, label)
        
        # Save SVG file
        svg_path = assets_dir / f"progress_{difficulty}.svg"
        with open(svg_path, "w") as f:
            f.write(svg_content)
        
        print(f"Generated {svg_path}")
    
    # Also generate a combined stats file
    stats = {
        "counts": counts,
        "totals": totals,
        "last_updated": "Generated automatically"
    }
    
    with open(assets_dir / "progress_stats.json", "w") as f:
        json.dump(stats, f, indent=2)
    
    print("Progress bars generated successfully!")
    print(f"Problems found: Easy={counts['easy']}, Medium={counts['medium']}, Hard={counts['hard']}")

if __name__ == "__main__":
    main()