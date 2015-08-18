
# Script to generate random IMEI at every Emulator startup
		
import os
import shutil
import random

# Open files
with open('images/system.img','r+b') as old, open('buffer', 'wb') as new:
    for line in old:											# Line by line search
			if line.find('351')>1:
					if (line[line.find('351')+5]=='3' and line[line.find('351')+6]=='5' and line[line.find('351')+7]=='3'):
							old_imei=line[line.find('351')+10:line.find('351')+25]		# Old IMEI Number
							new_imei=''
							for i in range(1,16):				# Generate new IMEI Number
									new_imei+=str(random.randint(1,9))
							new.write(line.replace(old_imei,new_imei))	# Replace Old IMEI with New IMEI
							continue
			new.write(line)									#Write lines in buffer
shutil.move('buffer', 'images/system.img')								# Remove Buffer file
# Divya Shah