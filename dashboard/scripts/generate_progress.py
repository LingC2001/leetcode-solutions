#!/usr/bin/env python3
"""Generate SVG progress bars and dashboard charts for LeetCode problems"""

import os
import json
import re
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

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

def analyze_topics():
    """Analyze topics/patterns across all problems"""
    problems_dir = Path("problems")
    topic_counts = defaultdict(int)
    topic_totals = defaultdict(int)
    
    # Define common LeetCode topics and their approximate total counts
    leetcode_topic_totals = {
        "Array": 400,
        "Hash Table": 200,
        "String": 250,
        "Two Pointers": 80,
        "Sliding Window": 60,
        "Stack": 100,
        "Binary Search": 90,
        "Dynamic Programming": 300,
        "Tree": 200,
        "Graph": 150,
        "Linked List": 80,
        "Math": 150,
        "Backtracking": 80,
        "Greedy": 120,
        "Heap": 60
    }
    
    # Scan all problems for topics
    for difficulty_dir in ["1-easy", "2-medium", "3-hard"]:
        diff_path = problems_dir / difficulty_dir
        if not diff_path.exists():
            continue
            
        for problem_dir in diff_path.iterdir():
            if not problem_dir.is_dir():
                continue
                
            readme_path = problem_dir / "README.md"
            if readme_path.exists():
                try:
                    content = readme_path.read_text()
                    # Extract topics from problem name and content
                    topics = extract_topics_from_content(content)
                    for topic in topics:
                        if topic in leetcode_topic_totals:
                            topic_counts[topic] += 1
                except:
                    pass
    
    # Add topics based on problem names (fallback)
    for difficulty_dir in ["1-easy", "2-medium", "3-hard"]:
        diff_path = problems_dir / difficulty_dir
        if not diff_path.exists():
            continue
            
        for problem_dir in diff_path.iterdir():
            if not problem_dir.is_dir():
                continue
                
            problem_name = problem_dir.name.lower()
            # Infer topics from problem names
            if any(word in problem_name for word in ["sum", "array", "duplicate"]):
                topic_counts["Array"] += 1
            if any(word in problem_name for word in ["anagram", "palindrome", "string", "substring"]):
                topic_counts["String"] += 1
            if "parentheses" in problem_name:
                topic_counts["Stack"] += 1
            if "search" in problem_name:
                topic_counts["Binary Search"] += 1
            if any(word in problem_name for word in ["buy", "sell", "stock"]):
                topic_counts["Dynamic Programming"] += 1
            if "window" in problem_name:
                topic_counts["Sliding Window"] += 1
            if "two" in problem_name and "sum" in problem_name:
                topic_counts["Two Pointers"] += 1
    
    # Merge with totals
    for topic, total in leetcode_topic_totals.items():
        topic_totals[topic] = total
    
    return dict(topic_counts), dict(topic_totals)

def extract_topics_from_content(content):
    """Extract topics from README content"""
    topics = []
    # Look for common topic patterns in content
    topic_patterns = {
        "Array": r"\barray|arrays\b",
        "Hash Table": r"\bhash\s+table|hash\s+map|dictionary\b",
        "String": r"\bstring|strings\b",
        "Two Pointers": r"\btwo\s+pointers?\b",
        "Sliding Window": r"\bsliding\s+window\b",
        "Stack": r"\bstack\b",
        "Binary Search": r"\bbinary\s+search\b",
        "Dynamic Programming": r"\bdynamic\s+programming|dp\b",
        "Tree": r"\btree|trees\b",
        "Graph": r"\bgraph|graphs\b"
    }
    
    content_lower = content.lower()
    for topic, pattern in topic_patterns.items():
        if re.search(pattern, content_lower):
            topics.append(topic)
    
    return topics

def analyze_languages():
    """Analyze language coverage across problems"""
    problems_dir = Path("problems")
    language_counts = {"Python": 0, "C++": 0, "Java": 0}
    total_problems = 0
    
    for difficulty_dir in ["1-easy", "2-medium", "3-hard"]:
        diff_path = problems_dir / difficulty_dir
        if not diff_path.exists():
            continue
            
        for problem_dir in diff_path.iterdir():
            if not problem_dir.is_dir():
                continue
                
            total_problems += 1
            if (problem_dir / "solution.py").exists():
                language_counts["Python"] += 1
            if (problem_dir / "solution.cpp").exists():
                language_counts["C++"] += 1
            if (problem_dir / "solution.java").exists():
                language_counts["Java"] += 1
    
    return language_counts, total_problems

def analyze_status():
    """Analyze completion status of problems"""
    problems_dir = Path("problems")
    status_counts = {"Complete": 0, "Solutions Only": 0}
    
    for difficulty_dir in ["1-easy", "2-medium", "3-hard"]:
        diff_path = problems_dir / difficulty_dir
        if not diff_path.exists():
            continue
            
        for problem_dir in diff_path.iterdir():
            if not problem_dir.is_dir():
                continue
                
            has_readme = (problem_dir / "README.md").exists()
            has_solution = any([
                (problem_dir / "solution.py").exists(),
                (problem_dir / "solution.cpp").exists(),
                (problem_dir / "solution.java").exists()
            ])
            
            if has_readme and has_solution:
                status_counts["Complete"] += 1
            elif has_solution:
                status_counts["Solutions Only"] += 1
    
    return status_counts

def generate_progress_svg(solved, total, color, label):
    """Generate SVG for circular progress bar with dark mode support"""
    
    percentage = (solved / total) * 100 if total > 0 else 0
    
    # Calculate circumference and stroke dash offset
    radius = 45
    circumference = 2 * 3.14159 * radius
    offset = circumference - (percentage / 100) * circumference
    
    svg = f'''<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg-circle {{ stroke: #e5e7eb; }}
    .text-primary {{ fill: #374151; }}
    .text-secondary {{ fill: #6b7280; }}
    .text-tertiary {{ fill: #9ca3af; }}
    
    @media (prefers-color-scheme: dark) {{
      .bg-circle {{ stroke: #374151; }}
      .text-primary {{ fill: #f9fafb; }}
      .text-secondary {{ fill: #9ca3af; }}
      .text-tertiary {{ fill: #6b7280; }}
    }}
  </style>
  <!-- Background circle -->
  <circle cx="60" cy="60" r="45" fill="none" class="bg-circle" stroke-width="8"/>
  
  <!-- Progress circle -->
  <circle cx="60" cy="60" r="45" fill="none" stroke="{color}" stroke-width="8"
          stroke-dasharray="{circumference}" stroke-dashoffset="{offset}" 
          stroke-linecap="round" transform="rotate(-90 60 60)"/>
  
  <!-- Text -->
  <text x="60" y="55" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" font-weight="bold" class="text-primary">
    {solved}
  </text>
  <text x="60" y="75" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" class="text-secondary">
    {label}
  </text>
  <text x="60" y="90" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" class="text-tertiary">
    {percentage:.1f}%
  </text>
</svg>'''
    
    return svg

def generate_combined_difficulty_ring_svg(counts):
    """Generate combined difficulty ring chart SVG with dark mode support"""
    
    total = sum(counts.values())
    
    if total == 0:
        svg = '''<svg width="200" height="240" viewBox="0 0 200 240" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg-ring { stroke: #e5e7eb; }
    .text-primary { fill: #374151; }
    .text-secondary { fill: #6b7280; }
    
    @media (prefers-color-scheme: dark) {
      .bg-ring { stroke: #374151; }
      .text-primary { fill: #f9fafb; }
      .text-secondary { fill: #9ca3af; }
    }
  </style>
  <circle cx="100" cy="100" r="80" fill="none" class="bg-ring" stroke-width="16"/>
  <text x="100" y="95" text-anchor="middle" font-family="Arial, sans-serif" font-size="24" font-weight="bold" class="text-primary">0</text>
  <text x="100" y="115" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" class="text-secondary">Problems</text>
</svg>'''
        return svg
    
    # Calculate angles for each difficulty
    easy_angle = (counts.get('easy', 0) / total) * 360
    medium_angle = (counts.get('medium', 0) / total) * 360
    hard_angle = (counts.get('hard', 0) / total) * 360
    
    # Color mapping
    colors = {
        'easy': '#22c55e',
        'medium': '#f59e0b', 
        'hard': '#ef4444'
    }
    
    # Helper function to generate SVG path for arc
    def generate_arc_path(start_angle, end_angle, inner_radius, outer_radius):
        import math
        start_rad = math.radians(start_angle - 90)  # -90 to start from top
        end_rad = math.radians(end_angle - 90)
        
        x1 = 100 + outer_radius * math.cos(start_rad)
        y1 = 100 + outer_radius * math.sin(start_rad)
        x2 = 100 + outer_radius * math.cos(end_rad)
        y2 = 100 + outer_radius * math.sin(end_rad)
        
        x3 = 100 + inner_radius * math.cos(end_rad)
        y3 = 100 + inner_radius * math.sin(end_rad)
        x4 = 100 + inner_radius * math.cos(start_rad)
        y4 = 100 + inner_radius * math.sin(start_rad)
        
        large_arc = "1" if end_angle - start_angle > 180 else "0"
        
        return f"M {x1:.2f} {y1:.2f} A {outer_radius} {outer_radius} 0 {large_arc} 1 {x2:.2f} {y2:.2f} L {x3:.2f} {y3:.2f} A {inner_radius} {inner_radius} 0 {large_arc} 0 {x4:.2f} {y4:.2f} Z"
    
    svg = '''<svg width="380" height="240" viewBox="0 0 380 240" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg-ring { stroke: #f3f4f6; }
    .text-primary { fill: #374151; }
    .text-secondary { fill: #6b7280; }
    
    @media (prefers-color-scheme: dark) {
      .bg-ring { stroke: #374151; }
      .text-primary { fill: #f9fafb; }
      .text-secondary { fill: #9ca3af; }
    }
  </style>
  <!-- Background ring -->
  <circle cx="100" cy="100" r="80" fill="none" class="bg-ring" stroke-width="30"/>
'''
    
    # Generate paths for each difficulty
    current_angle = 0
    
    for difficulty in ['easy', 'medium', 'hard']:
        count = counts.get(difficulty, 0)
        if count > 0:
            angle = (count / total) * 360
            path = generate_arc_path(current_angle, current_angle + angle, 50, 80)
            color = colors[difficulty]
            svg += f'  <path d="{path}" fill="{color}"/>\n'
            current_angle += angle
    
    # Center text
    svg += f'''
  <!-- Center text -->
  <text x="100" y="95" text-anchor="middle" font-family="Arial, sans-serif" font-size="28" font-weight="bold" class="text-primary">
    {total}
  </text>
  <text x="100" y="115" text-anchor="middle" font-family="Arial, sans-serif" font-size="13" class="text-secondary">
    Problems Solved
  </text>
  <!-- Legend (to the right) -->
  <g transform="translate(220, 70)">
    <circle cx="0" cy="0" r="7" fill="{colors['easy']}"/>
    <text x="18" y="5" font-family="Arial, sans-serif" font-size="15" class="text-primary">Easy ({counts.get('easy', 0)})</text>
  </g>
  <g transform="translate(220, 110)">
    <circle cx="0" cy="0" r="7" fill="{colors['medium']}"/>
    <text x="18" y="5" font-family="Arial, sans-serif" font-size="15" class="text-primary">Medium ({counts.get('medium', 0)})</text>
  </g>
  <g transform="translate(220, 150)">
    <circle cx="0" cy="0" r="7" fill="{colors['hard']}"/>
    <text x="18" y="5" font-family="Arial, sans-serif" font-size="15" class="text-primary">Hard ({counts.get('hard', 0)})</text>
  </g>
</svg>'''
    
    return svg

def generate_topic_mastery_svg(topic_counts, topic_totals):
    """Generate topic mastery chart SVG with dark mode support"""
    
    if not topic_counts:
        return ""
    
    # Sort topics by mastery percentage (descending)
    sorted_topics = sorted(topic_counts.items(), key=lambda x: (x[1] / topic_totals.get(x[0], 1)), reverse=True)
    
    # Take top 8 topics
    top_topics = sorted_topics[:8]
    
    chart_width = 400
    chart_height = len(top_topics) * 35 + 60
    
    svg = f'''<svg width="{chart_width}" height="{chart_height}" viewBox="0 0 {chart_width} {chart_height}" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg-panel {{ fill: #f9fafb; }}
    .text-primary {{ fill: #374151; }}
    .text-secondary {{ fill: #6b7280; }}
    .bg-bar {{ fill: #e5e7eb; }}
    .bar-text {{ fill: white; }}
    
    @media (prefers-color-scheme: dark) {{
      .bg-panel {{ fill: #1f2937; }}
      .text-primary {{ fill: #f9fafb; }}
      .text-secondary {{ fill: #9ca3af; }}
      .bg-bar {{ fill: #374151; }}
      .bar-text {{ fill: #f9fafb; }}
    }}
  </style>
  <!-- Background -->
  <rect width="{chart_width}" height="{chart_height}" class="bg-panel" rx="8"/>
  
  <!-- Title -->
  <text x="20" y="25" font-family="Arial, sans-serif" font-size="14" font-weight="bold" class="text-primary">
    Topic Mastery
  </text>
'''
    
    # Color mapping for different topics
    colors = ["#3b82f6", "#10b981", "#f59e0b", "#ef4444", "#8b5cf6", "#ec4899", "#06b6d4", "#84cc16"]
    
    for i, (topic, count) in enumerate(top_topics):
        total = topic_totals.get(topic, count)
        percentage = (count / total) * 100
        
        y_offset = 50 + i * 35
        bar_width = int((percentage / 100) * 250)
        color = colors[i % len(colors)]
        
        svg += f'''
  <!-- Topic: {topic} -->
  <text x="20" y="{y_offset + 16}" font-family="Arial, sans-serif" font-size="11" class="text-secondary">
    {topic}
  </text>
  <rect x="120" y="{y_offset}" width="250" height="{20}" class="bg-bar" rx="4"/>
  <rect x="120" y="{y_offset}" width="{bar_width}" height="{20}" fill="{color}" rx="4"/>
  <text x="130" y="{y_offset + 16}" font-family="Arial, sans-serif" font-size="10" class="bar-text" font-weight="bold">
    {count}/{total} ({percentage:.1f}%)
  </text>
'''
    
    svg += '</svg>'
    return svg

def generate_language_coverage_svg(language_counts, total_problems):
    """Generate language coverage chart SVG with dark mode support"""
    
    if not language_counts:
        return ""
    
    chart_width = 300
    chart_height = len(language_counts) * 30 + 60
    
    svg = f'''<svg width="{chart_width}" height="{chart_height}" viewBox="0 0 {chart_width} {chart_height}" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg-panel {{ fill: #f9fafb; }}
    .text-primary {{ fill: #374151; }}
    .text-secondary {{ fill: #6b7280; }}
    .bg-bar {{ fill: #e5e7eb; }}
    
    @media (prefers-color-scheme: dark) {{
      .bg-panel {{ fill: #1f2937; }}
      .text-primary {{ fill: #f9fafb; }}
      .text-secondary {{ fill: #9ca3af; }}
      .bg-bar {{ fill: #374151; }}
    }}
  </style>
  <!-- Background -->
  <rect width="{chart_width}" height="{chart_height}" class="bg-panel" rx="8"/>
  
  <!-- Title -->
  <text x="20" y="25" font-family="Arial, sans-serif" font-size="14" font-weight="bold" class="text-primary">
    Language Coverage
  </text>
'''
    
    # Color mapping for different languages
    language_colors = {
        "python": "#3776ab",
        "javascript": "#f7df1e",
        "java": "#ed8b00",
        "cpp": "#00599c",
        "c": "#a8b9cc",
        "go": "#00add8",
        "rust": "#dea584",
        "typescript": "#3178c6"
    }
    
    y_offset = 50
    for lang, count in language_counts.items():
        percentage = (count / total_problems) * 100
        bar_width = int((percentage / 100) * 180)
        color = language_colors.get(lang.lower(), "#6b7280")
        
        svg += f'''
  <!-- Language: {lang} -->
  <text x="20" y="{y_offset + 16}" font-family="Arial, sans-serif" font-size="12" class="text-primary">
    {lang}
  </text>
  <rect x="80" y="{y_offset}" width="180" height="20" class="bg-bar" rx="10"/>
  <rect x="80" y="{y_offset}" width="{bar_width}" height="20" fill="{color}" rx="10"/>
  <text x="270" y="{y_offset + 14}" font-family="Arial, sans-serif" font-size="10" class="text-secondary">
    {count} ({percentage:.1f}%)
  </text>
'''
        y_offset += 30
    
    svg += '</svg>'
    return svg

def generate_status_donut_svg(status_counts):
    """Generate status donut chart SVG with dark mode support"""
    
    complete = status_counts.get("complete", 0)
    solutions_only = status_counts.get("solutions_only", 0)
    total = complete + solutions_only
    
    if total == 0:
        return ""
    
    chart_size = 200
    center = chart_size // 2
    outer_radius = 60
    inner_radius = 35
    
    svg = f'''<svg width="{chart_size}" height="{chart_size}" viewBox="0 0 {chart_size} {chart_size}" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg-panel {{ fill: #f9fafb; }}
    .text-primary {{ fill: #374151; }}
    .text-secondary {{ fill: #6b7280; }}
    
    @media (prefers-color-scheme: dark) {{
      .bg-panel {{ fill: #1f2937; }}
      .text-primary {{ fill: #f9fafb; }}
      .text-secondary {{ fill: #9ca3af; }}
    }}
  </style>
  <!-- Background circle -->
  <circle cx="{center}" cy="{center}" r="{outer_radius + 5}" class="bg-panel"/>
'''
    
    # Generate donut segments
    import math
    
    if complete > 0:
        complete_angle = (complete / total) * 360
        complete_rad = math.radians(complete_angle)
        
        # Calculate path for complete segment
        x1 = center + outer_radius * math.cos(-math.pi/2)
        y1 = center + outer_radius * math.sin(-math.pi/2)
        x2 = center + outer_radius * math.cos(complete_rad - math.pi/2)
        y2 = center + outer_radius * math.sin(complete_rad - math.pi/2)
        
        x3 = center + inner_radius * math.cos(complete_rad - math.pi/2)
        y3 = center + inner_radius * math.sin(complete_rad - math.pi/2)
        x4 = center + inner_radius * math.cos(-math.pi/2)
        y4 = center + inner_radius * math.sin(-math.pi/2)
        
        large_arc = 1 if complete_angle > 180 else 0
        complete_path = f"M {x1} {y1} A {outer_radius} {outer_radius} 0 {large_arc} 1 {x2} {y2} L {x3} {y3} A {inner_radius} {inner_radius} 0 {large_arc} 0 {x4} {y4} Z"
        
        svg += f'  <path d="{complete_path}" fill="#22c55e"/>\n'
    
    if solutions_only > 0:
        solutions_angle = (solutions_only / total) * 360
        solutions_rad = math.radians(solutions_angle)
        start_angle = complete_angle if complete > 0 else 0
        
        # Calculate path for solutions_only segment
        x1 = center + outer_radius * math.cos(math.radians(start_angle) - math.pi/2)
        y1 = center + outer_radius * math.sin(math.radians(start_angle) - math.pi/2)
        x2 = center + outer_radius * math.cos(math.radians(start_angle + solutions_angle) - math.pi/2)
        y2 = center + outer_radius * math.sin(math.radians(start_angle + solutions_angle) - math.pi/2)
        
        x3 = center + inner_radius * math.cos(math.radians(start_angle + solutions_angle) - math.pi/2)
        y3 = center + inner_radius * math.sin(math.radians(start_angle + solutions_angle) - math.pi/2)
        x4 = center + inner_radius * math.cos(math.radians(start_angle) - math.pi/2)
        y4 = center + inner_radius * math.sin(math.radians(start_angle) - math.pi/2)
        
        large_arc = 1 if solutions_angle > 180 else 0
        solutions_path = f"M {x1} {y1} A {outer_radius} {outer_radius} 0 {large_arc} 1 {x2} {y2} L {x3} {y3} A {inner_radius} {inner_radius} 0 {large_arc} 0 {x4} {y4} Z"
        
        svg += f'  <path d="{solutions_path}" fill="#f59e0b"/>\n'
    
    svg += f'''
  <!-- Center text -->
  <text x="{center}" y="{center - 5}" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" font-weight="bold" class="text-primary">
    {total}
  </text>
  <text x="{center}" y="{center + 12}" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" class="text-secondary">
    Problems
  </text>
  
  <!-- Legend -->
  <circle cx="20" cy="140" r="4" fill="#22c55e"/>
  <text x="30" y="144" font-family="Arial, sans-serif" font-size="10" class="text-primary">Complete ({complete})</text>
  <circle cx="20" cy="155" r="4" fill="#f59e0b"/>
  <text x="30" y="159" font-family="Arial, sans-serif" font-size="10" class="text-primary">Solutions Only ({solutions_only})</text>
</svg>'''
    
    return svg

def get_git_activity():
    """Get actual git commit activity for the last 52 weeks"""
    import subprocess
    from collections import defaultdict
    
    try:
        # Get commits from last year
        result = subprocess.run([
            'git', 'log', '--since=52 weeks ago', '--format=%ad', '--date=short'
        ], capture_output=True, text=True, cwd='.')
        
        if result.returncode != 0:
            return defaultdict(int)
        
        # Parse commit dates and count commits per date
        activity = defaultdict(int)
        for line in result.stdout.strip().split('\n'):
            if line:
                activity[line] += 1
        
        return activity
    except:
        return defaultdict(int)

def generate_activity_heatmap_svg():
    """Generate activity heatmap based on actual git commits with dark mode support"""
    
    weeks = 52
    days_per_week = 7
    cell_size = 11
    cell_spacing = 2
    
    chart_width = weeks * (cell_size + cell_spacing) + 100
    chart_height = days_per_week * (cell_size + cell_spacing) + 60
    
    # Get actual git activity
    git_activity = get_git_activity()
    
    svg = f'''<svg width="{chart_width}" height="{chart_height}" viewBox="0 0 {chart_width} {chart_height}" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg-panel {{ fill: #f9fafb; }}
    .text-primary {{ fill: #374151; }}
    .text-secondary {{ fill: #6b7280; }}
    .activity-0 {{ fill: #ebedf0; }}
    .activity-1 {{ fill: #c6e48b; }}
    .activity-2 {{ fill: #7bc96f; }}
    .activity-3 {{ fill: #239a3b; }}
    .activity-4 {{ fill: #196127; }}
    
    @media (prefers-color-scheme: dark) {{
      .bg-panel {{ fill: #1f2937; }}
      .text-primary {{ fill: #f9fafb; }}
      .text-secondary {{ fill: #9ca3af; }}
      .activity-0 {{ fill: #374151; }}
      .activity-1 {{ fill: #365314; }}
      .activity-2 {{ fill: #4d7c0f; }}
      .activity-3 {{ fill: #65a30d; }}
      .activity-4 {{ fill: #84cc16; }}
    }}
  </style>
  <!-- Background -->
  <rect width="{chart_width}" height="{chart_height}" class="bg-panel" rx="8"/>
  
  <!-- Title -->
  <text x="20" y="25" font-family="Arial, sans-serif" font-size="14" font-weight="bold" class="text-primary">
    Git Activity (Last 52 Weeks)
  </text>
  
  <!-- Day labels -->
  <text x="15" y="55" font-family="Arial, sans-serif" font-size="9" class="text-secondary">M</text>
  <text x="15" y="81" font-family="Arial, sans-serif" font-size="9" class="text-secondary">W</text>
  <text x="15" y="107" font-family="Arial, sans-serif" font-size="9" class="text-secondary">F</text>
'''
    
    # Calculate date range for the last 52 weeks
    from datetime import datetime, timedelta
    
    end_date = datetime.now().date()
    start_date = end_date - timedelta(weeks=52)
    
    # Generate heatmap based on actual git activity
    current_date = start_date
    week = 0
    
    while current_date <= end_date and week < weeks:
        for day in range(days_per_week):
            if current_date > end_date:
                break
                
            x = 30 + week * (cell_size + cell_spacing)
            y = 40 + day * (cell_size + cell_spacing)
            
            # Get activity level for this date
            date_str = current_date.strftime('%Y-%m-%d')
            commits = git_activity.get(date_str, 0)
            
            # Map commits to activity level (0-4)
            if commits == 0:
                activity_level = 0
            elif commits == 1:
                activity_level = 1
            elif commits <= 3:
                activity_level = 2
            elif commits <= 6:
                activity_level = 3
            else:
                activity_level = 4
            
            svg += f'  <rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" class="activity-{activity_level}" rx="2"/>\n'
            
            current_date += timedelta(days=1)
            
        week += 1
    
    # Legend
    legend_x = chart_width - 120
    svg += f'''
  <!-- Legend -->
  <text x="{legend_x}" y="25" font-family="Arial, sans-serif" font-size="9" class="text-secondary">Less</text>
'''
    
    for i in range(5):
        x = legend_x + 25 + i * 13
        svg += f'  <rect x="{x}" y="15" width="10" height="10" class="activity-{i}" rx="2"/>\n'
    
    svg += f'  <text x="{legend_x + 90}" y="25" font-family="Arial, sans-serif" font-size="9" class="text-secondary">More</text>\n'
    
    svg += '</svg>'
    return svg

def calculate_streak():
    """Calculate current streak of consecutive days with commits"""
    from datetime import datetime, timedelta
    
    git_activity = get_git_activity()
    
    # Start from today and work backwards
    current_date = datetime.now().date()
    current_streak = 0
    longest_streak = 0
    temp_streak = 0
    
    # Check last 365 days for current and longest streak
    for i in range(365):
        date_str = current_date.strftime('%Y-%m-%d')
        commits = git_activity.get(date_str, 0)
        
        if commits > 0:
            temp_streak += 1
            if i == 0 or temp_streak > 0:  # If today or continuing streak
                current_streak = temp_streak
        else:
            if temp_streak > longest_streak:
                longest_streak = temp_streak
            temp_streak = 0
            if i == 0:  # If no commits today, current streak is 0
                current_streak = 0
        
        current_date -= timedelta(days=1)
    
    # Check if temp_streak is the longest (in case streak continues to the end)
    if temp_streak > longest_streak:
        longest_streak = temp_streak
        
    return current_streak, longest_streak

def generate_streak_counter_svg():
    """Generate streak counter SVG with dark mode support"""
    
    current_streak, longest_streak = calculate_streak()
    
    # Determine emoji and color based on streak
    if current_streak == 0:
        emoji = "😴"
        streak_color = "#6b7280"
        status_text = "No streak"
    elif current_streak < 3:
        emoji = "🔥"
        streak_color = "#f59e0b"
        status_text = "Getting started!"
    elif current_streak < 7:
        emoji = "🚀"
        streak_color = "#10b981"
        status_text = "On fire!"
    elif current_streak < 14:
        emoji = "⚡"
        streak_color = "#3b82f6"
        status_text = "Amazing!"
    else:
        emoji = "🏆"
        streak_color = "#8b5cf6"
        status_text = "Legendary!"
    
    width = 380  # Match the width of the pie chart for visual alignment
    height = 240  # Match the height of the pie chart
    
    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg-panel {{ fill: #f8fafc; stroke: #e2e8f0; stroke-width: 1; }}
    .text-primary {{ fill: #1e293b; }}
    .text-secondary {{ fill: #64748b; }}
    .text-accent {{ fill: {streak_color}; }}
    .text-muted {{ fill: #94a3b8; }}
    @media (prefers-color-scheme: dark) {{
      .bg-panel {{ fill: #0f172a; stroke: #334155; }}
      .text-primary {{ fill: #f1f5f9; }}
      .text-secondary {{ fill: #cbd5e1; }}
      .text-accent {{ fill: {streak_color}; }}
      .text-muted {{ fill: #64748b; }}
    }}
  </style>

  <!-- Background -->
  <rect width="{width}" height="{height}" class="bg-panel" rx="8"/>

  <!-- Streak emoji -->
  <text x="{width//2}" y="70" text-anchor="middle" font-size="40">{emoji}</text>

  <!-- Current streak number -->
  <text x="{width//2}" y="120" text-anchor="middle" font-family="Arial, sans-serif" font-size="48" font-weight="bold" class="text-accent">
    {current_streak}
  </text>

  <!-- "Day streak" text -->
  <text x="{width//2}" y="155" text-anchor="middle" font-family="Arial, sans-serif" font-size="20" class="text-primary">
    Day{'s' if current_streak != 1 else ''} streak
  </text>

  <!-- Status text -->
  <text x="{width//2}" y="185" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" class="text-secondary">
    {status_text}
  </text>

  <!-- Longest streak info -->
  <text x="{width//2}" y="215" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" class="text-muted">
    Best: {longest_streak} day{'s' if longest_streak != 1 else ''}
  </text>
</svg>'''
    return svg

def main():
    """Generate all dashboard charts and SVGs"""
    
    print("🔍 Analyzing repository...")
    
    # Count current problems
    counts = count_problems()
    
    # Analyze topics, languages, and status
    topic_counts, topic_totals = analyze_topics()
    language_counts, total_problems = analyze_languages()
    status_counts = analyze_status()
    
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
    
    # Create dashboard assets directory
    assets_dir = Path("dashboard/assets")
    assets_dir.mkdir(exist_ok=True)
    
    print("📊 Generating dashboard charts...")
    
    # Generate combined difficulty ring chart
    combined_ring_svg = generate_combined_difficulty_ring_svg(counts)
    with open(assets_dir / "difficulty_progress.svg", "w", encoding="utf-8") as f:
        f.write(combined_ring_svg)
    print("✅ Generated dashboard/assets/difficulty_progress.svg")
    
    # Generate activity heatmap (based on real git commits)
    activity_svg = generate_activity_heatmap_svg()
    with open(assets_dir / "activity_heatmap.svg", "w", encoding="utf-8") as f:
        f.write(activity_svg)
    print("✅ Generated dashboard/assets/activity_heatmap.svg")
    
    # Generate streak counter SVG
    streak_svg = generate_streak_counter_svg()
    with open(assets_dir / "streak_counter.svg", "w", encoding="utf-8") as f:
        f.write(streak_svg)
    print("✅ Generated dashboard/assets/streak_counter.svg")
    
    # Generate comprehensive stats file
    stats = {
        "counts": counts,
        "totals": totals,
        "topic_counts": topic_counts,
        "topic_totals": topic_totals,
        "language_counts": language_counts,
        "status_counts": status_counts,
        "total_problems": total_problems,
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    with open(assets_dir / "dashboard_stats.json", "w") as f:
        json.dump(stats, f, indent=2)
    
    print("📈 Dashboard generation complete!")
    print(f"📊 Summary: {total_problems} problems ({counts['easy']} easy, {counts['medium']} medium, {counts['hard']} hard)")
    print(f"🌟 Topics covered: {len([t for t, c in topic_counts.items() if c > 0])}")
    print(f"💻 Languages: Python({language_counts['Python']}), C++({language_counts['C++']}), Java({language_counts['Java']})")
    print(f"✅ Status: {status_counts.get('Complete', 0)} complete, {status_counts.get('Solutions Only', 0)} solutions only")

if __name__ == "__main__":
    main()