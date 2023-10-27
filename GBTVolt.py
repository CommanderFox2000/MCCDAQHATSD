from daqhats import mcc118
import pandas as pd
import time
from datetime import datetime

# Create an instance of the MCC 118 object
board_num = 0
mcc = mcc118(board_num)

# Read analog input values from different channels
channel_red = 4  # Specify the channel number for the 'Red' column
channel_black = 5  # Specify the channel number for the 'Black' column

data = []  # List to store the acquired data

# Set the total duration in seconds
total_duration = 172800 

# Set the time interval between readings in seconds
interval = 30

# Read voltage every interval until the specified duration is reached
while True:
    # Read voltage from 'Red' channel
    value_red = mcc.a_in_read(channel_red)

    # Read voltage from 'Black' channel
    value_black = mcc.a_in_read(channel_black)

    # Store the acquired data along with the timestamp
    timestamp = datetime.now()
    data.append([timestamp, value_red, value_black])

    # Create a DataFrame from the acquired data
    df = pd.DataFrame(data, columns=["Timestamp", "Red", "Black"])

    # Export DataFrame to Excel file
    output_file = "mcc118_data.xlsx"
    df.to_excel(output_file, index=False)

    # Print a confirmation message
    print(f"Data exported to {output_file}")

    # Wait for the specified interval
    time.sleep(interval)
