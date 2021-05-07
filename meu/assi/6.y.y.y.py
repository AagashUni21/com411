def source_data_path():
    """
    Task 6: Retrieve a file path to the source data file.
    The function should prompt the user to enter the file path for a data file (e.g. 'data/sol_data.csv').
    If the file path entered by the user does not end in 'csv' then a suitable error message should be displayed
    and the value None should be returned.
    Otherwise, the file path entered by the user should be returned.
    :return: None if the file path does not end in 'csv' otherwise return the file path entered by the user
    """
    # TODO: Your code here

    print("Please enter the file path for a data file :\n")
    file_path = input()
    if ".csv" not in file_path:
      print ("Sorry, the program only accepts .csv files")
      return None
    else:
      return file_path


x = source_data_path()
print(x)




#consider endswith()