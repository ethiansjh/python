import time
import webbrowser

break_time = 0
total_time = 3

print("Started on " + time.ctime())
while break_time < total_time:
    time.sleep(10)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    break_time = break_time + 1
