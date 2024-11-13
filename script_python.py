import time
import platform
import psutil
from datetime import datetime

while True:
    print("Ora și data curentă:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Sistem de operare:", platform.system(), platform.release())
    
    # Informații despre procesor
    print("Informații despre CPU:", platform.processor())
    
    # Informații despre memorie RAM
    ram_info = psutil.virtual_memory()
    print("RAM total:", round(ram_info.total / (1024**3), 2), "GB")
    print("RAM disponibil:", round(ram_info.available / (1024**3), 2), "GB")
    
    # Informații despre disk
    disk_info = psutil.disk_usage('/')
    print("Spațiu pe disk total:", round(disk_info.total / (1024**3), 2), "GB")
    print("Spațiu pe disk folosit:", round(disk_info.used / (1024**3), 2), "GB")
    print("Spațiu pe disk disponibil:", round(disk_info.free / (1024**3), 2), "GB")
    
    print("---------------------------------------")
    time.sleep(5)  # modifică 5 cu numărul de secunde dorit

