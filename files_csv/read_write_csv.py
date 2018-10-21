import csv
from datetime import datetime

b_dir = r"D:\old\e\learn\Python\Learn_h\files_csv"
path = r"{0}\Google Stock Market Data - google_stock_data.csv.csv".format(
    b_dir)

try:
    with open(path, newline='') as file:
        reader = csv.reader(file)

        header = next(reader)  # The first line is the harder

        data = []
        for row in reader:
            # row =['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
            date = datetime.strptime(row[0], "%m/%d/%Y")
            open_price = float(row[1])
            high = float(row[2])
            low = float(row[3])
            close = float(row[4])
            volume = int(row[5])
            adj_close = float(row[6])

            data.append([date, open_price, high, low,
                         close, volume, adj_close])

    # Compute and store daily stock returns
    return_path = r"{0}\google_returns.csv".format(b_dir)
    file = open(return_path, 'w', newline='')
    my_writer = csv.writer(file)
    my_writer.writerow(["Date", "Return"])

    for i in range(len(data) - 1):
        today_row = data[i]
        today_date = today_row[0]
        today_price = today_row[-1]
        yesterday_row = data[i+1]
        yesterday_price = yesterday_row[-1]

        daily_return = (today_price-yesterday_price)/yesterday_price
        formated_date = today_date.strftime('%m/%d/%Y')
        my_writer.writerow([formated_date, daily_return])

except FileNotFoundError as e:
    print("file no exists")
