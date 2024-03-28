# stoc market data analysis

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]

def average_price(data):
    num = 0
    for i in range(len(data)):
        num += data[i][2]    
    return format(num / len(data), ".1f")

print(average_price(stock_data))


# event attendance tracker
attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),
    # More attendees...
]

def all_attendees(attendees):
    count = {}
    for name, occupation in attendees:
        if occupation not in count:
            count[occupation] = 1
        else:
            count[occupation] += 1
        print(f"{name} is attending {occupation}")
        
    return count

print(all_attendees(attendees))