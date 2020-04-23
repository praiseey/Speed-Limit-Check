def check_speed():
    speed_limit = int(70)
    points = 0
    while points <= 12:
        speed = int(input("Enter driver's speed: "))
        if speed > speed_limit:
            over_speed = speed - speed_limit
            count = int(over_speed / 5)
            points += count
            print(f"Points: {points}")
            break
        else:
            print('Speed is OK!')
            break
    else:
        print("License suspended!")


check_speed()