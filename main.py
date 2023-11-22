import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:\\IoT Network Intrusion Dataset Undersampled.csv')
print(data.head())

num_rows, num_columns = data.shape

# Print the results
print(f'Number of rows: {num_rows}')
print(f'Number of columns: {num_columns}')

# Specify the columns you want to plot
columns_to_plot = ['Protocol', 'AM/PM', 'Normal']

# Plot each specified column
for column in columns_to_plot:
    plt.plot(data[column], label=column)

# Add labels and title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Title of the Plot')

# Show legend
plt.legend()
# Show the plot
plt.show()
# Plot the histogram
plt.hist(data['Normal'], bins=10, color='blue', edgecolor='black')

# Add labels and title
plt.xlabel('AM/PM')
plt.ylabel('Frequency')
plt.title(f'Histogram of AM/PM')

# Show the plot
plt.show()


columns_to_drop = ['Tot_Fwd_Pkts', 'Tot_Bwd_Pkts', 'TotLen_Fwd_Pkts']

# Drop the specified columns
data.drop(columns=columns_to_drop, inplace=True)
# Drop duplicate rows
data_no_duplicates = data.drop_duplicates()
print(data.head())
print(f'Number of rows: {num_rows}')
print(f'Number of columns: {num_columns}')
# the information of datasets without duplicated
print(data.info())
# Drop the specified of list columns
list = ['Dst_0', 'Dst_1', 'Dst_2', 'Dst_3']
data_no_duplicates1 = data.drop_duplicates(subset=list, keep='first', inplace=True)
print(data.info())
print(data.describe())
# Count the null cells in each column
null_counts = data.isnull().sum()

# Display the count of null cells for each column
print(null_counts)

# Drop rows with null values
data_cleaned = data.dropna()
data.dropna(inplace=True)
# Display the DataFrame without null values
print(data_cleaned)
print(data.describe())

# Fill null values in multiple columns with the mean of each column
columns_to_fill = ['AM/PM', 'Src_Port']
data[columns_to_fill] = data[columns_to_fill].apply(lambda x: x.fillna(x.std()))

# Display the DataFrame with null values filled with means in specified columns
print(data.describe())


# Plot the noisy data
att = ['Flow_IAT_Mean', 'Flow_IAT_Std', 'Flow_IAT_Max', 'Flow_IAT_Min']
plt.figure(figsize=(20, 10))
data[att].boxplot()
plt.title('noise in data')
plt.show()
