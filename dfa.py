# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:00:31 2019

@author: Savio
"""

class DFA:
    
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state
        return
    
    def transition(self, string):
        self.current_state = self.transition_function[(self.current_state, string)]
        return
    
    def accept_state(self):
        if(self.current_state in self.accept_states):
            return print('Accepted\nStop state:',self.current_state)
        return print('Rejected\nStop state:',self.current_state)
    
    def run(self, string):
        for s in string:
            self.transition(s)
            continue
        return self.accept_state()
#End