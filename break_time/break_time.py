import time
import webbrowser

def break_time(url, wait_sec, num):
	i = 0
	while i < num:
		time.sleep(wait_sec)
		webbrowser.open(url)
		i += 1

break_time('https://www.youtube.com/watch?v=YBHWLGkt1hI', 10, 3)