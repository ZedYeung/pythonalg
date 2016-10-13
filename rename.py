import os
folder = 'F:\\'
print('Renaming')
for foldername, subfolders, filenames in os.walk(folder):
	for filename in filenames:
		full_filename = os.path.join(foldername, filename)
		os.renames(filename, filename.replace(' ', '_'))
print('Done.')

