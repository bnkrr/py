import urllib, os, shutil

def main():
	url = 'https://dl.dropboxusercontent.com/u/39925787/'
	print 'Downloading PQR.exe'
	urllib.urlretrieve(url + 'PQR/PQR.exe', 'PQR/PQR.exe')
	print 'Downloading PQR.exe.config'
	urllib.urlretrieve(url + 'PQR/PQR.exe.config', 'PQR/PQR.exe.config')
	print 'Downloading Xelper_INTERRUPT_Abilities.xml'
	urllib.urlretrieve(url + 'PQR_Profiles/Xelper_INTERRUPT_Abilities.xml', 'PQR/Profiles/INTERRUPT/Xelper_INTERRUPT_Abilities.xml')
	print 'Downloading Xelper_INTERRUPT_Rotations.xml'
	urllib.urlretrieve(url + 'PQR_Profiles/Xelper_INTERRUPT_Rotations.xml', 'PQR/Profiles/INTERRUPT/Xelper_INTERRUPT_Rotations.xml')
	print 'Downloading Offsets'
	offsetlist = urllib.urlopen(url + 'PQR_Offsets/offsets.txt').read().split('|')
	for offset in offsetlist:
		urllib.urlretrieve(url + 'PQR_Offsets/' + offset, 'PQR/Offsets/' + offset)
	print 'Download Complete.'
	# if os.path.exists(hostsfolder + 'hosts.bak'):
	# 	print 'D'
	# 	os.remove(hostsfolder + 'hosts.bak')
	# os.rename(hostsfolder + 'hosts', hostsfolder + 'hosts.bak')
	# shutil.copyfile(downfolder + 'hosts', hostsfolder)
	# print 'Done.'

def dlof():
        offsetlist = urllib.urlopen('https://dl.dropboxusercontent.com/u/39925787/PQR_Offsets/offsets.txt').read().split('|')
        for offset in offsetlist:
                urllib.urlretrieve('https://dl.dropboxusercontent.com/u/39925787/PQR_Offsets/' + offset, offset)
        print 'Download Complete.'


if __name__ == "__main__":
	dlof()
