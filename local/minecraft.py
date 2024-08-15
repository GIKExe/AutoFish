# системные
from difflib import SequenceMatcher

# глобальные
# локальные

sounds = [
	'Всплеск',
	'Всплеск от поплавка', # 01 <-- тригер на вытагивание
	'Плеск воды',
	'Поплавок вытащен', # 03 <-- статус попалвка
	'Получен опыт',
	'Найден предмет',
	'Кашалот шёлкает',
	None
]

# test = [
# 	['о Плеск воды'],                                                                                                                                                                    
# 	['и Плеск воды'],                                                                                                                                                                    
# 	['а Плеск воды', 'ве -ы'],                                                                                                                                                           
# 	['о Плеск воды №', '4'],                                                                                                                                                             
# 	['>. Плеск воды №'],                                                                                                                                                                 
# 	['мч < Плеск воды'],                                                                                                                                                                 
# 	['А', 'о Плеск воды'],                                                                                                                                                               
# 	['А.', 'а Плеск воды №'],                                                                                                                                                            
# 	['Плеск воды >'],                                                                                                                                                                    
# 	['Всплеск от поплавка', ':. Плеск воды ы'],                                                                                                                                          
# 	['Всплеск от поплавка', 'А. Плеск есоды ы'],                                                                                                                                         
# 	['Всплеск', 'Всплеск от поплавка', 'о Плеск воды ы'],                                                                                                                                
# 	['Поплавок вытащен', 'Всплеск', 'Всплеск от поплавка', 'Е < Плеск воды'],                                                                                                            
# 	['Поплавок вытащен', 'Всплеск', 'Беплеск от поплавка', 'Е < Плеск воды', '_| Я \\\\'],                                                                                               
# 	['Поплавок вытащен', 'Всплеск', 'Всплеск от поплавка', 'У < Плеск воды'],                                                                                                            
# 	['Поплавок вытащен', 'Всплеск', 'Беплеск от поплавка', 'Е < Плеск воды'],                                                                                                            
# 	['Поплавок вытащен', 'Всплеск', 'Всплеск от поплавка', 'Е ы Плеск воды х'],                                                                                                          
# 	['Поплавок вытащен', 'Всплеск', 'Всплеск от поплавка', 'к ы Плеск воды'],                                                                                                            
# 	['Поплавок вытащен', 'Всплеск', 'Беплеск от поплавка', 'к ы Плеск воды'],                                                                                                            
# 	['Поплавок вытащен', 'Всплеск', 'Всплеск от поплавка', 'Плеск воды'],                                                                                                                
# 	['< Плеск воды'],                                                                                                                                                                    
# 	['Всплеск', '< Плеск воды'],                                                                                                                                                         
# 	['Всплеск'],                                                                                                                                                                         
# 	['Всплеск', '< Плеск'],                                                                                                                                                              
# 	['Воплеск', 'Плеск воды'],                                                                                                                                                           
# 	['Боплеск', 'Плеск воды'],                                                                                                                                                           
# 	['Всплеск', 'Плеск воды'],                                                                                                                                                           
# 	['Всплеск', 'Плеск воды >'],                                                                                                                                                         
# 	['Всплеск', 'и < Плеск воды'],                                                                                                                                                       
# 	['Всплеск', 'и Плеск воды'],                                                                                                                                                         
# 	['Всплеск', 'Плеск вол'],                                                                                                                                                            
# 	['Всплеск от поплавка', 'Всплеск', 'о Плеск воды'],                                                                                                                                  
# 	['Всплеск от поплавка', 'Всплеск', 'и Плеск воды'],                                                                                                                                  
# 	['Полычен опыт', 'Поплавок вытащен', 'Всплеск от поплавка', 'Всплеск', 'А. Плеск воды'],                                                                                             
# 	['Полычен опыт', 'Поплавок вытащен', 'Всплеск от поплавка', 'Всплеск', 'Плеск воды', 'аа'],                                                                                          
# 	['Найден предмет', 'Полычен опыт', 'Поплавок вытащен', 'Беплеск от поплавка', 'Всплеск', 'Плеск воды', 'м', 'аа'],                                                                   
# 	['Найден предмет', 'Полычен опыт', 'Поплавок вытащен', 'Беплеск от поплавка', 'Всплеск', 'Плеск воды', 'м', 'ах'],                                                                   
# 	['Найден предмет', 'Полычен опыт', 'Поплавок вытащен', 'Беплеск от поплавка', 'Всплеск', 'Плеск воды', '№', 'аа'],                                                                   
# 	['Найден предмет', 'Полычен опыт', 'Поплавок вытащен', 'Всплеск от поплавка', 'Всплеск', 'А. Плеск воды'],                                                                           
# 	['Найден предмет', 'Полычен опыт', 'Поплавок вытащен', 'Беплеск от поплавка', 'Всплеск', 'А. Плеск воды'],                                                                           
# 	['Найден предмет', 'Полычен опыт', 'Поплавок вытащен', 'Беплеск от поплавка', 'Всплеск', 'А. Плеск воды', 'Я м'],                                                                    
# 	['Найден предмет', 'Полычен опыт', 'Поплавок вытащен', 'Беплеск от поплавка', 'Всплеск', 'Ь < Плеск воды', 'Я №'],                                                                   
# 	['Найден предмет', 'Полычен опыт', 'Поплавок вытащен', 'Беплеск от поплавка', 'Всплеск', 'Плеск воды'],                                                                              
# 	['Найден предмет', 'Полычен опыт', 'Поплавок вытащен', 'Всплеск от поплавка', 'Всплеск', 'Плеск воды'],                                                                              
# 	['Найден предмет', 'Полычен опыт', 'Поплавок вытащен', 'ы Плеск воды'],                                                                                                              
# 	['Найден предмет', 'Полычен опыт', 'Поплавок вытащен'],                                                                                                                              
# 	['Наяден предмет', 'Плеск есоды'],                                                                                                                                                   
# 	['Наяден предмет', 'Плеск воды'],   
# ]

def ratio(a, b):
	return SequenceMatcher(a=a, b=b).ratio()

def proc(lines):
	res = {}
	for line in lines:
		l = [ratio(line, b) for b in sounds[:-1]]
		r = max(l)
		if r < 0.36:
			index = -1
		else:
			index = l.index(r)
		sound = sounds[index]
		if sound:
			res[sound] = r
		# print(f'Исходный: {line}\nРаспознан: {sound}\n%: {r}, {l}\n')
	return res