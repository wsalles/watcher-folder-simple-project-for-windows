
#-*- coding: utf-8 -*-
import logging, shutil
from patience import watchers
import config.vars as vars

def action(file):
	print(file)
	filename = file.replace(watch_folder, '')
	logging.info(f'O arquivo {filename} foi capturado!')
	errors = 0
	while True:
		try:
			shutil.copy(file, destination_folder + filename)
			logging.info(f'O arquivo {filename} foi copiado para {destination_folder}')
			break
		except:
			errors += 1
			if errors == 3:
				logging.info(f'Falha ao copiar o arquivo para {destination_folder}')
				return False

if __name__ == '__main__':
	logging.basicConfig(filename="./watcher.log", filemode='a', datefmt='%d-%b-%y %H:%M:%S',
						format='%(asctime)s - %(message)s', level=logging.INFO)
	watch_folder = vars.config['SOURCE']
	destination_folder = vars.config['DESTINATION']
	watcher = watchers.PatternWatcher(
		callback=action,
		workdir=vars.config['SOURCE'],
		ext=vars.config['EXT'],
		timeout=vars.config['TIMEOUT'],
		blocking=True,
		recursive=False)
	watcher.start()
