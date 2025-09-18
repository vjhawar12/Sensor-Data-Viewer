import pandas as pd
import matplotlib.pyplot as plt
import argparse
from os.path import exists, splitext

def read_csv(file_path):
  df = pd.read_csv(file_path)
  return df

def read_json(file_path):
  df = pd.read_json(file_path)
  return df

def save_csv(df, output_file_path):
  df.to_csv(output_file_path)

def save_json(df, output_file_path):
  df.to_json(output_file_path)

def drop_duplicates(df, columns):
  df = df.drop_duplicates(subset=columns)
  return df

def remove_nan(df):
  df = df.dropna(axis=0)
  return df

def filter_outliers(df, col, min_range, max_range, inclusive):
  if col not in df.columns:
    raise ValueError(f"Error: Column {col} does not exist")
  if min_range > max_range:
    raise ValueError(f"Error: min range cannot be > max range")

  if inclusive == 0:
    mask = ((df[col] > min_range) & (df[col] < max_range))
  else:
    mask = ((df[col] >= min_range) & (df[col] <= max_range))

  df = df[mask]

  return df

def interpolate_missing(df, cols=["vehicle_speed", "engine_rpm", "throttle_position"]):
  df[cols] = df[cols].interpolate(method='linear', limit_direction='forward')
  return df

def high_rpm(df):
  df["high_rpm"] = False
  df["high_rpm"] = df["engine_rpm"] > 6000
  return df

def rpm_vs_time(df):
  plt.plot(df["timestamp"], df["engine_rpm"])
  plt.xlabel("time")
  plt.ylabel("rpm")
  plt.title("RPM vs Time")
  plt.grid(True)
  plt.show()

def rpm_vs_throttle(df):
  plt.plot(df["engine_rpm"], df["throttle_position"])
  plt.xlabel("rpm")
  plt.ylabel("throttle")
  plt.title("Throttle vs RPM")
  plt.grid(True)
  plt.show()

def get_file_ext(filepath):
  return splitext(filepath)[1].lower()

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('-v', '--view', action='store_true')
parser.add_argument('-s', '--save')
parser.add_argument('-d', '--drop_duplicates')
parser.add_argument('-n', '--remove_nan', action='store_true')
parser.add_argument(
    '-f', '--filter_outliers',
    nargs=4,
    metavar=('col', 'min', 'max', 'inclusive'),
    help="Filter outliers in COL between MIN and MAX inclusive if INCLUSIVE is 1"
)

parser.add_argument('-i', '--interpolate_missing')
parser.add_argument('-H', '--high_rpm', action='store_true')
parser.add_argument('-r', '--rpm_vs_time', action='store_true')
parser.add_argument('-t', '--rpm_vs_throttle', action='store_true')

args = parser.parse_args()

if not exists(args.filename):
  raise ValueError(f"Error: File {args.filename} not found")

file_ext = get_file_ext(args.filename)

if file_ext == ".csv":
  df = read_csv(args.filename)
elif file_ext == ".json":
  df = read_json(args.filename)
else:
  raise ValueError(f"Error: invalid file extension -- '{file_ext}' not supported")

if args.view:
  print(df)

if args.drop_duplicates:
  cols = args.drop_duplicates.split(",")
  for col in cols:
    if col not in df.columns:
      raise ValueError(f"Error: Column '{col}' does not exist")

  df = drop_duplicates(df, cols)

if args.remove_nan:
  df = remove_nan(df)

if args.filter_outliers:
  col = args.filter_outliers[0]
  min_range = float(args.filter_outliers[1])
  max_range = float(args.filter_outliers[2])
  inclusive = int(args.filter_outliers[3])
  df = filter_outliers(df, col, min_range, max_range, inclusive)

if args.interpolate_missing:
  cols = args.interpolate_missing.split(",")
  df = interpolate_missing(df, cols)

if args.high_rpm:
  df = high_rpm(df)

if args.rpm_vs_time:
  rpm_vs_time(df)

if args.rpm_vs_throttle:
  rpm_vs_throttle(df)

if args.save:
  if args.save.endswith(".csv"):
    save_csv(df, args.save)
  elif args.save.endswith(".json"):
    save_json(df, args.save)

