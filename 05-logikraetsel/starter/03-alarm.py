door_closed = False
alarm_enabled = False

if not (door_closed and alarm_enabled):
    print("Alarm")
else:
    print("Kein Alarm")
