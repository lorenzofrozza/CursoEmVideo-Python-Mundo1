import os

os.system('cls')
trip_distance = float(input('Type the distance of the trip (Km/h): '))

if trip_distance <= 200:
    print(
        f'\nTrip distance: - {trip_distance} kph -\nTicket price: U${trip_distance * 0.50}')
else:
    print(
        f'\nTrip distance: - {trip_distance} kph -\nTicket price: U${trip_distance * 0.45}')
