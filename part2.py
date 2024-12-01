time = int(input("Enter the time (in hours, 24-hour clock): "))

hours_to_wait = int(input("Enter the number of hours to wait for your alarm: "))

alarm_time = (time + hours_to_wait) % 24

print(f"The alarm will go off at {alarm_time}:00 hours.")