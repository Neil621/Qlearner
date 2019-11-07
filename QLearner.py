"""  		   	  			  	 		  		  		    	 		 		   		 		  
Template for implementing QLearner  (c) 2015 Tucker Balch  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		   	  			  	 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		   	  			  	 		  		  		    	 		 		   		 		  
All Rights Reserved  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		   	  			  	 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		   	  			  	 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		   	  			  	 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		   	  			  	 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		   	  			  	 		  		  		    	 		 		   		 		  
or edited.  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		   	  			  	 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		   	  			  	 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		   	  			  	 		  		  		    	 		 		   		 		  
GT honor code violation.  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
Student Name: Neil Watt(replace with your name)  		   	  			  	 		  		  		    	 		 		   		 		  
GT User ID: nwatt (replace with your User ID)  		   	  			  	 		  		  		    	 		 		   		 		  
GT ID: 903476861  (replace with your GT ID)  		   	  			  	 		  		  		    	 		 		   		 		  
"""  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
import numpy as np  		   	  			  	 		  		  		    	 		 		   		 		  
import random as rand  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
class QLearner(object):  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
    
    def author(self):
        return "nwatt3"
    
    def __init__(self, 
        num_states=100, 
        num_actions = 4, 
        alpha = 0.2, 
        gamma = 0.9, 
        rar = 0.5, 
        radr = 0.999, 
        dyna = 200, 
        verbose = False):  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
        self.verbose = verbose  		   	  			  	 		  		  		    	 		 		   		 		  
        self.num_actions = num_actions  		   	  			  	 		  		  		    	 		 		   		 		  
        self.s = 0  		   	  			  	 		  		  		    	 		 		   		 		  
        self.a = 0 
        
        
        self.num_states = num_states
        self.num_actions = num_actions
        self.verbose = verbose
        self.num_actions = num_actions
        self.alpha = alpha
        self.gamma = gamma
        self.rar = rar
        self.radr = radr
        self.dyna = dyna
        
        self.s = 0  		   	  			  	 		  		  		    	 		 		   		 		  
        self.a = 0  
        self.Q = np.zeros((num_states, num_actions))
        
        if dyna > 0:
            self.T = np.zeros((num_states, num_actions, num_states))
            self.Tc = np.full((num_states, num_actions, num_states), 0.00001)
            self.R = np.zeros((num_states, num_actions))
            
            
        
  		   	  			  	 		  		  		    	 		 		   		 		  

        
        
    def query(self,s_prime,r):  		   	  			  	 		  		  		    	 		 		   		 		  
        """  		   	  			  	 		  		  		    	 		 		   		 		  
        @summary: Update the Q table and return an action  		   	  			  	 		  		  		    	 		 		   		 		  
        @param s_prime: The new state  		   	  			  	 		  		  		    	 		 		   		 		  
        @param r: The ne state  		   	  			  	 		  		  		    	 		 		   		 		  
        @returns: The selected action  		   	  			  	 		  		  		    	 		 		   		 		  
        """  		   	  			  	 		  		  		    	 		 		   		 		  
        
        self.Q[self.s, self.a] = (1 - self.alpha) * self.Q[self.s, self.a] + self.alpha * (r +self.gamma*self.Q[s_prime,:].max())

        if self.dyna > 0:
            # T and R update
            self.Tc[self.s, self.a, s_prime] += 1
            self.T[self.s, self.a, :] = self.Tc[self.s, self.a, :] / self.Tc[self.s, self.a, :].sum()
            self.R[self.s, self.a] = (1 - self.alpha) * self.R[self.s, self.a] + self.alpha * r

            # Hallucinate
            dyna_s = np.random.randint(0, self.num_states, size=self.dyna)
            dyna_a = np.random.randint(0, self.num_actions, size=self.dyna)
            dyna_s_prime = self.T[dyna_s, dyna_a, :].argmax(axis=1)
            dyna_action = self.Q[dyna_s_prime, :].argmax(axis=1)
            dyna_r = self.R[dyna_s, dyna_a]

            # Update
            self.Q[dyna_s, dyna_a] = (1 - self.alpha) * self.Q[dyna_s, dyna_a] + self.alpha * (dyna_r + self.gamma * self.Q[dyna_s_prime, dyna_action])

        
        #action = rand.randint(0, self.num_actions-1)  		   	  			  	 		  		  		    	 		 		   		 		
        #move to next action
        action = self.querysetstate(s_prime)
        
        #update random state
        self.rar *= self.radr
        
        if self.verbose: print(f"s = {s_prime}, a = {action}, r={r}")  		   	  			  	 		  		  		    	 		 		   		 		  
        return action  		   	  			  	 		  		  		    	 		 		   		 		  


    def querysetstate(self, s):  		   	  			  	 		  		  		    	 		 		   		 		  
        """  		   	  			  	 		  		  		    	 		 		   		 		  
        @summary: Update the state without updating the Q-table  		   	  			  	 		  		  		    	 		 		   		 		  
        @param s: The new state  		   	  			  	 		  		  		    	 		 		   		 		  
        @returns: The selected action  		   	  			  	 		  		  		    	 		 		   		 		  
        """  		   	  			  	 		  		  		    	 		 		   		 		  
        
        
        
        # decision is made on action 
        action = self.Q[s, :].argmax()
        if rand.uniform(0.0, 1.0) <= self.rar:
            action = rand.randint(0, self.num_actions-1)  		   	  			  	 		  		  		    	 		 		   		 		  
        
        #if self.verbose: print(f("s = {s}, a = {action}")) 
        
        if self.verbose: print(("{},{}".format(a, action)))    
            
         #print("Date Range: {} to {}".format(sd, ed))
           
        
            
           
        self.s = s
        self.a = action
            
            
        return action  		   	  			  	 		  		  		    	 		 		   		 		  
  		 
    
    
if __name__=="__main__":  		   	  			  	 		  		  		    	 		 		   		 		  
    print("Remember Q from Star Trek? Well, this isn't him")  		   	  			  	 		  		  		    	 		 		   		 		  
