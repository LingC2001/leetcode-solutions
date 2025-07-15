# 📊 LeetCode Dashboard

This directory contains all dashboard-related files for visualizing LeetCode problem-solving progress.

## 📁 Directory Structure

```
dashboard/
├── scripts/
│   └── generate_progress.py    # Dashboard generation script
├── assets/
│   ├── difficulty_progress.svg # Combined difficulty progress ring chart
│   ├── streak_counter.svg      # Current and longest streak counter
│   ├── activity_heatmap.svg    # Git activity heatmap (based on real commits)
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

### 2. **Streak Counter** 🔥
- Shows current consecutive days with commits
- Dynamic emoji and color based on streak length
- Displays motivational status messages
- Tracks personal best streak record

### 3. **Git Activity Heatmap** 🔥
- GitHub-style contribution graph based on real git commits
- 52 weeks of actual repository activity
- Color intensity represents commit frequency
- Tracks pushes/commits to main branch

## 🔧 Technical Details

### Dependencies
- Python 3.x (no external libraries required)
- Uses only standard library modules: `pathlib`, `json`, `re`, `datetime`, `collections`

### How It Works
1. **Analysis Phase**: Scans `problems/` directory structure
2. **Git Analysis**: Queries git log for actual commit activity
3. **Generation Phase**: Creates SVG charts with calculated metrics
4. **Output Phase**: Saves charts to `dashboard/assets/`

### Customization
You can modify the script to:
- Add new chart types
- Change colors and styling  
- Adjust git activity analysis period
- Modify activity level thresholds

## 📈 Integration

The dashboard is integrated into the main README.md with:
- Progress ring chart prominently displayed at the top
- Real git activity heatmap showing actual development patterns
- Automatic updates via GitHub Actions
- Clean, focused visual presentation

---

*Auto-generated dashboard providing comprehensive insights into LeetCode problem-solving progress* 🎯