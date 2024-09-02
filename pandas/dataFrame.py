import pandas as pd

std_data = [
    (101, "Tayyab", 24, "Male", "Lahore"),
    (102, "Raafeh", 25, "Male", "Karachi"),
    (103, "Farah", 28, "Female", "Sukkur"),
    (104, "Hamna", 21, "Female", "Zhob"),
    (105, "Burair", 27, "Trans", "Islamabad")]

# new_data_frame = pd.DataFrame(std_data)
data_frame = pd.DataFrame(std_data, columns=["std_id", "name", "age", "gender", "Address"], index=["row1", "row2", "row3", "row4", "row5"])
print(data_frame)

# data_frame2 = pd.read_csv("students.csv") # This is to read a file internally or within this environment

# print(data_frame.head(2)) # Prints first 5 rows or as of fig i.e. 2 in this example
# print(data_frame.tail(1))
# print(data_frame.shape) # rows and columns
# print(data_frame[["age", "gender"]])
print(data_frame.loc[["row2"]])
# print(data_frame.age)
# print(data_frame.size) # Total elements
# print(data_frame.dtypes)
# print(data_frame.values) # print those as lists
# print(data_frame.index)
# print(data_frame.columns)