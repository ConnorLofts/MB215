# Activity 4

# Ask for column titles
col1_title = input("Enter the first column title: ")
col2_title = input("Enter the second column title: ")
col3_title = input("Enter the third column title: ")

# Ask for data for the first row
row1_col1 = input(f"Enter data for first row, {col1_title}: ")
row1_col2 = input(f"Enter data for first row, {col2_title}: ")
row1_col3 = input(f"Enter data for first row, {col3_title}: ")

# Ask for data for the second row
row2_col1 = input(f"Enter data for second row, {col1_title}: ")
row2_col2 = input(f"Enter data for second row, {col2_title}: ")
row2_col3 = input(f"Enter data for second row, {col3_title}: ")

# Display the formatted table
# Print header
print(f"{col1_title:<20}{col2_title:<20}{col3_title:<20}")

# Print separator line
print("-" * 60)

# Print rows
print(f"{row1_col1:<20}{row1_col2:<20}{row1_col3:<20}")
print(f"{row2_col1:<20}{row2_col2:<20}{row2_col3:<20}")