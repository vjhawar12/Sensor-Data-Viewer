# Vehicle Data Processing & Visualization

This project provides a command line tool for **loading, cleaning, processing, and visualizing vehicle telemetry data** such as RPM and throttle position. It supports both CSV and JSON input formats and offers utilities for filtering, handling missing values, and generating plots.

---

## Features

- **File I/O**
  - Read CSV and JSON datasets
  - Save processed data back to CSV or JSON  

- **Data Cleaning**
  - Drop duplicate rows (by column, default `timestamp`)
  - Remove rows containing `NaN` values
  - Interpolate missing values (default: `vehicle_speed`, `engine_rpm`, `throttle_position`)  

- **Filtering**
  - Filter outliers by numeric ranges (inclusive or exclusive)  

- **Feature Engineering**
  - Add a `high_rpm` flag when engine RPM > 6000  

- **Visualization**
  - Plot engine RPM over time  
  - Plot RPM vs throttle position  

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/vehicle-data-tool.git
   cd vehicle-data-tool
    ```  
2. Install dependencies
   ```bash
   pip install pandas matplotlib
   ```

## Usage
Run the script from the command line:
```bash
python main.py <filename> [options]
```

## Arguments

| Option | Description |
|--------|-------------|
| `filename` | Path to input file (`.csv` or `.json`) |
| `-s, --save` | Save processed data to file (`.csv` or `.json`) |
| `-d, --drop_duplicates` | Drop duplicates based on column(s) |
| `-n, --remove_nan` | Remove rows containing `NaN` values |
| `-f, --filter_outliers` | Filter outliers given ranges (requires dict) |
| `-i, --interpolate_missing` | Interpolate missing values for given columns |
| `-h, --high_rpm` | Add `high_rpm` flag (RPM > 6000) |
| `-r, --rpm_vs_time` | Plot RPM vs time |
| `-t, --rpm_vs_throttle` | Plot RPM vs throttle position |

## Examples

### 1. Basic load and clean
Remove rows with missing values and drop duplicates based on the `timestamp` column:
```bash
python main.py data.csv -n -d timestamp
```

### 2. Interpolate missing values and save to JSON
Interpolate missing values for vehicle_speed and engine_rpm, then save as cleaned.json:
```bash
python main.py data.csv -i vehicle_speed engine_rpm -s cleaned.json
```

### 3. Plot RPM over time
Generate a plot of engine RPM vs. timestamp:
```bash
python main.py data.csv -r
```

### 4. Add high RPM flag and save cleaned CSV
Mark rows where engine_rpm > 6000 and save the output to processed.csv:
```bash
python main.py data.csv -h -s processed.csv
```
