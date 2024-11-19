import time
 
def focus_clock(duration):
    start_time = time.time()
    end_time = start_time + duration * 60
 
    while time.time() < end_time:
        time_left = end_time - time.time()
        minutes = time_left // 60
        seconds = time_left % 60
        print(f"\r专注剩余时间: {minutes:02d}:{seconds:02d}", end="")
        time.sleep(1)
    print("\n专注时间到！")
