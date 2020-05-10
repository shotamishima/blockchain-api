# -*- coding: utf-8 -*-
"""
Created on Mon May  4 01:42:43 2020

@author: smshi
"""

import collections
"""
dictionaryの中身が同じでも順序が違うとハッシュは違うものになる
それを防ぐためにkeyの順番でソートし順序違いで別のハッシュと認識することを防ぐ

"""
def sorted_dict_by_key(unsorted_dict):
	return collections.OrderedDict(
			sorted(unsorted_dict.items(), key=lambda d: d[0]))

def pprint(chains):
	for i, chain in enumerate(chains):	
		print(f'{"="*25} Chain {i} {"="*25}')
		
	#chainの中身はdictionaryなのでitemsでkey,valueを取り出す
		for k, v in chain.items():
			if k == 'transactions':
				print(k)
				for d in v:
					print(f'{"-"*40}')
					for kk, vv in d.items():
						print(f' {kk:30}{vv}')
			else:
					print(f'{k:15}{v}')
	print(f'{"*"*25}')