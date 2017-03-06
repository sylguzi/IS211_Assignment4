#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
import random

def insertion_sort(a_list):
	start_time = time.time()
	for index in range(1, len(a_list)):
		current_value = a_list[index]
		position = index
		while position > 0 and a_list[position - 1] > current_value:
			a_list[position] = a_list[position - 1]
			position = position - 1
		a_list[position] = current_value
	return (time.time() - start_time), a_list

def shell_sort(a_list):
	start_time = time.time()
	sublist_count = len(a_list) // 2

	while sublist_count > 0:
		for start_position in range(sublist_count):
			gap_insertion_sort(a_list, start_position, sublist_count)
		sublist_count = sublist_count // 2
	return (time.time() - start_time), a_list

def gap_insertion_sort(a_list, start, gap):
	for i in range(start + gap, len(a_list), gap):
		current_value = a_list[i]
		position = i
		while position >= gap and a_list[position - gap] > current_value:
			a_list[position] = a_list[position - gap]
			position = position - gap
		a_list[position] = current_value

def python_sort(a_list):
	start_time = time.time()
	a_list.sort()
	return (time.time() - start_time), a_list

def generate_random_nb_my_list(nb, amount_my_list, maxNumber = sys.maxint):
	return [
		[random.randint(0, maxNumber) for _ in range (nb)]
			for _ in range (amount_my_list)
	]

def functionTimerAggregator(timeAggregator, fn, amt_of_nb, rnd_list):
	(fn_name, fn_function) = fn
	(timing, _) = fn_function(rnd_list)

	if amt_of_nb not in timeAggregator:
		timeAggregator[amt_of_nb] = {}
	if fn_name not in timeAggregator[amt_of_nb]:
		timeAggregator[amt_of_nb][fn_name] = 0	
	timeAggregator[amt_of_nb][fn_name] += timing

def printTimerAggregator(timeAggregator, list_size):
	for amount_of_number, fn_type in timeAggregator.iteritems():
		print('For %s size of list:' % amount_of_number)
		for fn_name, consumedTime in fn_type.iteritems():
			print('\t%s took %10.7f seconds to run, on average'
				% (fn_name, consumedTime / list_size))

if __name__ == '__main__':
	timeAggregator = {}
	amount_of_numbers = [500, 1000, 10000]
	function_list = [
		('Insertion Sort', insertion_sort),
		('Shell Sort', shell_sort),
		('Python Sort', python_sort),
	]
	list_size = 100

	for amount_of_number in amount_of_numbers:
		my_randoms = generate_random_nb_my_list(amount_of_number, list_size)
		for unsorted_list in my_randoms:
			for fn in function_list:
				functionTimerAggregator(
					timeAggregator, fn, amount_of_number, unsorted_list)

	printTimerAggregator(timeAggregator, list_size)
	