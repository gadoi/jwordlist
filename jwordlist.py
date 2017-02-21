#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, time
from datetime import datetime

# Console colors
W = '\033[1;0m'   # white 
R = '\033[1;31m'  # red
G = '\033[1;32m'  # green
O = '\033[1;33m'  # orange
B = '\033[1;34m'  # blue
Y = '\033[1;93m'  # yellow
P = '\033[1;35m'  # purple
C = '\033[1;36m'  # cyan
GR = '\033[1;37m'  # gray

os.system("clear")
current_path = os.path.dirname(os.path.realpath(__file__))
separate = "/" # use for linux
host = "http://j3ssiej.net23.net" # use for linux
version = '1.0'

filename = ''
list_words = []
list_birthday = []
list_symbol = ['-', '_']
dict_variation = {
	'a': ['4', '@'],
	'A': ['4', '@'],
	'i': ['1', '!'],
	'I': ['1', '!'],
	'l': ['1', '!'],
	'L': ['1', '!'],
	'e': ['3', '$'],
	'E': ['3', '$'],
	'1': ['i', 'l'],
	'4': ['a', 'A'],
	'3': ['e', 'E'],
	'0': ['o', 'O']
}

def banner():
	os.system("clear")
	print ("""{0}
      _                       _ _ _     _   
     (_)                     | | (_)   | |  
      ___      _____  _ __ __| | |_ ___| |_ 
     | \ \ /\ / / _ \| '__/ _` | | / __| __|{0}
 {1}    | |\ V  V / (_) | | | (_| | | \__ \ |_ 
     | | \_/\_/ \___/|_|  \__,_|_|_|___/\__|
    _/ |                                    
   |__/    Contact: {2}{3}{1}
	""".format(C, G, P,host))

def present():
	dash = '|/-\\'
	dot = ['.', '..', '...', '....']
	for i in range(4):
		os.system("clear")
		banner()
		print("{0}[{1}{2}{0}] Starting jwordlist version {3} [{1}{2}{0}]  ".format(G, R, dash[i], version))
		time.sleep(0.1)
	banner()

def import_input():
	words = input("{0}[{1}*{0}] {2}Enter your word separate by {1}';'{0} : ".format(G, R, C))
	filename = input("{0}[{1}*{0}] {2}Name of output file: {0}".format(G, R, B))
	filename = current_path + separate + filename.strip()
	words = words.split(';')
	words = [word.strip() for word in words]
	return words, filename

def birthday():
	day = ['0' + str(num) for num in range(0,10)] + list(range(0,32))
	day = [str(d) for d in day]
	month = ['0' + str(num) for num in range(0,10)] + list(range(0,13))
	month = [str(m) for m in month]
	year = ['0' + str(num) for num in range(0,10)] + list(range(0,100)) + list(range(0,datetime.now().year + 1))
	year = [str(y) for y in year]
	return day + month + year

def word_upper(word, result):
	for i in range(len(word)):
		result.append(word[:i] + word[i].upper() + word[i+1:])

def combine(result):
	for word in result[:]:
		for w in result[:]:
			print(word + w)
			# result.appen(word + w)

def add_birthday(birthday, word, result):
	for element in birthday:
		for s in list_symbol:
			result.append(word + element)
			result.append(element + word)
			result.append(word + s + element)
			result.append(element + s + word)

def replace_variation(variation, word, result):
	for word in result[:]:
		for key,values in variation.items():
			for letter in word:
				if letter == key:
					for v in values:
						result.append(word.replace(key, v))
			


def handle_input(birthday, variation, words):
	result = []
	for word in words:
		for w in words:
			result.append(word + w)

	for word in result[:]:
		word_upper(word,result)
		add_birthday(birthday,word, result)
	replace_variation(variation, word, result)
	return result

def handle_file(filename, final_list):
	with open(filename, "w+") as f:
		for word in final_list:
			f.write(word + '\n')
	f.close()
	print("{0}[{1}*{0}]  Check your file in {2}'{3}' ".format(G, R, B, filename))

if __name__ == '__main__':
	for i in range(3):
		present()
	list_words, filename = import_input()
	check_birthday = input("{0}You want to add brithday to your wordlist {1}(Y/N): {2} ".format(Y, C, G))
	if (check_birthday == 'Y' or check_birthday == 'y' or check_birthday == 'yes' or check_birthday == 'Yes'):
		list_birthday = birthday()
	final_list = handle_input(list_birthday, dict_variation, list_words) + list_words + list_birthday
	finall_list = set(final_list)
	handle_file(filename, final_list)