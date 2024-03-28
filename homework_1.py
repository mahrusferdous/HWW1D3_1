# Formatting flight itineraries
def fight_itinerary(flight_to):
    count = 0
    for i in flight_to:
        count += 1
        print(f"Itinerary {count}: {i[0]} - from {i[1]} to {i[2]}")
        
flight_to = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
fight_itinerary(flight_to)
    
    