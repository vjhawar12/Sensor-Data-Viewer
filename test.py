def get_file_ext(filepath):
  dot_index = filepath.index(".")
  ext = filepath[dot_index:]
  return ext


print(get_file_ext("test.csv.json"))


