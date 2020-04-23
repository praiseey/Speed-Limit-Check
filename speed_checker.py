def check_speed():
    speed_limit = int(70)
    points = 0
    speed = int(input("Enter driver's speed: "))
    if speed > speed_limit:
        over_speed = speed - speed_limit
        count = int(over_speed / 5)
        points += count
        if points > 12:
            print(f"Points: {points} \nLicense suspended!")
        else:
            print(f"You have exceeded speed limit. \nPoints: {points}")
    else:
        print('Speed is OK!')


check_speed()