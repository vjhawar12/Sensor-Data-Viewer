import pandas as pd
import matplotlib.pyplot as plt
import argparse

def read_csv(file_path):
  df = pd.read_csv(file_path)
  print(df.head())
  return df

def read_json(file_path):
  df = pd.read_json(file_path)
  print(df.head())
  return df

def save_csv(df, output_file_path):
  df.to_csv(output_file_path)

def save_json(df, output_file_path):
  df.to_json(output_file_path)

def drop_duplicates(df, columns=['timestamp']):
  df = df.drop_duplicates(subset=columns)
  return df

def remove_nan(df):
  df = df.dropna(axis=0)
  return df

def filter_outliers(df, _dict, exclusive=False):
  cols = _dict.keys()

  for col in cols:
    min_range = _dict[col][0]
    max_range = _dict[col][1]

    if exclusive:
      mask = ((df[col] > min_range) & (df[col] < max_range))
    else:
      mask = ((df[col] >= min_range) & (df[col] <= max_range))

    df = df[mask]

  return df

def interpolate_missing(df, cols=["vehicle_speed", "engine_rpm", "throttle_position"]):
  df = df[cols].interpolate(method='linear', limit_direction='forward')
  return df

def high_rpm(df):
  df["high_rpm"] = False
  df["high_rpm"] = df["engine_rpm"] > 6000
  return df

def rpm_vs_time(df):
  plt.plot(df["timestamp"], df["engine_rpm"])
  plt.show()

def plot_rpm_vs_throttle(df):
  plt.plot(df["engine_rpm"], df["throttle_position"])
  plt.show()

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('-s', '--save')
parser.add_argument('-d', '--drop_duplicates')
parser.add_argument('-n', '--remove_nan')
parser.add_argument('-f', '--filter_outliers')
parser.add_argument('-i', '--interpolate_missing')
parser.add_argument('-h', '--high_rpm')
parser.add_argument('-r', '--rpm_vs_time')
parser.add_argument('-t', '--rpm_vs_throttle')

args = parser.parse_args()

if '.csv' in args.filename:
  df = read_csv(args.filename)
elif '.json' in args.filename:
  df = read_json(args.filename)

if args.drop_duplicates in df.columns:
  df = drop_duplicates(df, list(args.drop_duplicates))

if args.remove_nan:
  df = remove_nan(df)

if args.interpolate_missing in df.columns:
  df = interpolate_missing(df, args.interpolate_missing)

if args.high_rpm:
  df = high_rpm(df)

if args.rpm_vs_time:
  rpm_vs_time(df)

if args.rpm_vs_throttle:
  rpm_vs_throttle(df)

if args.save:
  if '.csv' in args.save:
    save_csv(df, args.save)
  elif '.json' in args.save:
    save_json(df, args.save)
