import ' sys ':
import 'time':
import 'random':
import 'os':
import 'shutil':
import { FileSystemEventHandler } from 'watchdog.events':
import { Observer } from 'watchdog.observers':

from_dir = "<Set Path For Tracking File Services>"

class FileEventHandler(FileSystemEventHandler):

  def on_created(self, event):
    print(f"Hey, {event.src_path} has been created!")

  def on_deleted(self, event):
    print(f"Oops! Someone deleted {event.src_path}")
  
  def on_modified(self, event):
    print(f"Hey, {event.src_path} has been modified!")

  def on_moved(self, event):
    print(f"Hey, {event.src_path} has been moved!")

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()

list_of_files = os.listdir(from_dir)
print(list_of_files)

if os.path.exists(path2):
    print("Moving" + file_name + ".....")

    shutil.move(path1, path3)


else:
  os.makesdirs(path2)
  print("Moving" + file_name + ".....")
  shutil.move(path1, path3)