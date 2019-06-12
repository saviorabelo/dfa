# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:35:37 2019

@author: Savio Lopes Rabelo
"""

#Example of a simple DFA
#DFA only accepts odd-sized string
states = {0, 1}
alphabet = {'a','b'}
function_transition = {
  (0, 'a'): 1,
  (0, 'b'): 1,
  (1, 'a'): 0,
  (1, 'b'): 0,
}
start_state = 0
accept_states = {1}

#List of words
string = list('aba') #Accept
#string= list('baba') #Reject


#Start of the algorithm
current_state = start_state
for s in string:
    if (current_state, s) not in function_transition.keys():
        print('Error in function transition!')
        break
    current_state = function_transition[(current_state, s)]
if current_state in accept_states:
    print('Accept\nStop state:', current_state)
else:
    print('Reject\nStop state:', current_state)
#End of the algorithm