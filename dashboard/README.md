# 📊 LeetCode Dashboard

This directory contains all dashboard-related files for visualizing LeetCode problem-solving progress.

## 📁 Directory Structure

```
dashboard/
├── scripts/
│   └── generate_progress.py    # Dashboard generation script
├── assets/
│   ├── difficulty_progress.svg # Combined difficulty progress ring chart
│   ├── topic_mastery.svg       # Topic mastery horizontal bars
│   ├── language_coverage.svg   # Language coverage chart
│   ├── status_breakdown.svg    # Status breakdown donut chart
│   ├── activity_heatmap.svg    # GitHub-style activity heatmap
│   └── dashboard_stats.json    # Comprehensive analytics data
└── README.md                   # This file
```

## 🚀 Usage

### Generate Dashboard Charts
```bash
# From repository root
python3 dashboard/scripts/generate_progress.py
```

### Auto-Update via GitHub Actions
The dashboard automatically updates when you add new problems via the GitHub Actions workflow in `.github/workflows/update-progress.yml`.

## 📊 Generated Charts

### 1. **Combined Difficulty Progress Ring** 🟢🟡🔴
- Ring chart showing all difficulties in one view
- Center displays total problems solved
- Each segment represents a difficulty: Green (Easy), Orange (Medium), Red (Hard)
- Legend shows breakdown by count for each difficulty

### 2. **Topic Mastery Chart** 📈
- Horizontal bar chart showing algorithm pattern coverage
- Automatically detects topics from problem names and content
- Displays progress as count/total and percentage

### 3. **Language Coverage Chart** 💻
- Multi-language support visualization
- Tracks Python, C++, and Java implementations
- Shows coverage percentage for each language

### 4. **Status Breakdown Donut** ✅
- Completion status visualization
- Complete: Problems with both code and documentation
- Solutions Only: Problems with code but missing documentation

### 5. **Activity Heatmap** 🔥
- GitHub-style contribution graph
- 52 weeks of simulated activity
- Color intensity represents problem-solving frequency

## 🔧 Technical Details

### Dependencies
- Python 3.x (no external libraries required)
- Uses only standard library modules: `pathlib`, `json`, `re`, `datetime`, `collections`

### How It Works
1. **Analysis Phase**: Scans `problems/` directory structure
2. **Detection Phase**: Identifies topics, languages, and completion status
3. **Generation Phase**: Creates SVG charts with calculated metrics
4. **Output Phase**: Saves charts to `dashboard/assets/`

### Customization
You can modify the script to:
- Add new chart types
- Change colors and styling
- Adjust LeetCode total problem counts
- Add new topic detection patterns

## 📈 Integration

The dashboard is integrated into the main README.md with:
- Image references to `dashboard/assets/*.svg`
- Automatic updates via GitHub Actions
- Professional visual presentation

---

*Auto-generated dashboard providing comprehensive insights into LeetCode problem-solving progress* 🎯