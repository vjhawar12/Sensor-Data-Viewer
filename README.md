# Vehicle Data Processing & Visualization

This project provides a command-line tool for **loading, cleaning, processing, and visualizing vehicle telemetry data** (e.g., speed, RPM, throttle position). It supports both CSV and JSON input formats and offers utilities for filtering, handling missing values, and generating plots.

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
