#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import random
import sys

def sequential_search(my_list, search_elt):
	found = False
	start_time = time.time()
	for elt in my_list:
		if search_elt == elt:
			found = True
			break
	return (time.time() - start_time), found

def ordered_sequential_search(my_list, search_elt):
	found = False
	start_time = time.time()
	for elt in my_list:
		if search_elt == elt:
			found = True
			break
		elif search_elt > elt:
			break
	return (time.time() - start_time), found

def binary_search_iterative(my_list, search_elt):
	first = 0
	last = len(my_list) - 1
	found = False

	start_time = time.time()
	while first <= last and not found:
		midpoint = (first + last) // 2
		if my_list[midpoint] == search_elt:
			found = True
		elif search_elt < my_list[midpoint]:
			last = midpoint - 1
		else:
			first = midpoint + 1

	return (time.time() - start_time), found

def binary_search_rec(a_list, item):
	if len(a_list) == 0:
		return False
	else:
		midpoint = len(a_list) // 2
		if a_list[midpoint] == item:
			return True
		elif item < a_list[midpoint]:
			return binary_search_rec(a_list[:midpoint], item)
		else:
			return binary_search_rec(a_list[midpoint + 1:], item)

def binary_search_recursive(my_list, search_elt, start_time = time.time):
	start_time = time.time()
	return (time.time() - start_time), binary_search_rec(my_list, search_elt)

def generate_random_nb_my_list(nb, amount_my_list, maxNumber = sys.maxint):
	return [
		[random.randint(0, maxNumber) for _ in range (nb)]
			for _ in range (amount_my_list)
	]

def functionTimerAggregator(timeAggregator, fn, amt_of_nb, rnd_list):
	(fn_name, fn_function, fn_list_indx) = fn
	(timing, _) = fn_function(rnd_list[fn_list_indx], -1)

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
		('Sequential Search', sequential_search, 0),
		('Ordered Sequential Search', ordered_sequential_search, 1),
		('Binary Search Iterative', binary_search_iterative, 1),
		('Binary Search Recursive', binary_search_recursive, 1),
	]
	list_size = 100

	for amount_of_number in amount_of_numbers:
		my_randoms = generate_random_nb_my_list(amount_of_number, list_size)
		for unsorted_list in my_randoms:
			sorted_list = unsorted_list[:]
			sorted_list.sort()

			for fn in function_list:
				functionTimerAggregator(
					timeAggregator, fn, amount_of_number,
					(unsorted_list, sorted_list))

	printTimerAggregator(timeAggregator, list_size)
	