from datetime import timezone
from datetime import datetime
import time

currentTime = time.time()
print("currentTime is : " , str(currentTime))

Day = int(input("Enter Day: "))
Month = int(input("Enter Month: "))
Year = int(input("Enter Year: "))

dt = datetime(Year, Month, Day)
timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
print("timestamp is : ", str(timestamp))

print(round(currentTime))
print(round(timestamp))

r_currentTime = round(currentTime)
r_timestamp = round(timestamp)

age_in_s = r_currentTime - r_timestamp

print("You have lived ", str(age_in_s), " seconds so far!")
print("You have lived ", str(age_in_s / 60), " minutes so far!")
print("You have lived ", str((age_in_s / 60) / 60), " hours so far!")
print("You have lived ", str(((age_in_s / 60) / 60) / 24), " days so far!")
print("You have lived ", str(((age_in_s / 60) / 60) / 24 / 30), " months so far!")
print("You have lived ", str(((age_in_s / 60) / 60) / 24 / 30 / 12), " years so far!")

