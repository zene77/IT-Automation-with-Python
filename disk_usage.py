import shutil

du = shutil.disk_usage("/")
print("Espacio total:", du.total)
print("Usado:", du.used)
print("Libre:", du.free)
print('Hola, este es mi archivo disk_usage')

