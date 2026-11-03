hour = int(input("Enter hour (0-23): "))
minute = int(input("Enter minute (0-59): "))

if hour < 0 or hour > 23 or minute < 0 or minute > 59:
    print("Invalid time")

else:
    total_minutes = hour * 60 + minute

    if total_minutes < 600:
        print("On time +5")
    elif total_minutes < 1020:
        print("Late, no points")
    else:
        print("Training day is over")

# 10:00 is late because the condition uses < 600.