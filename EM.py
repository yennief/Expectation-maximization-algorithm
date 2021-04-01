
import numpy as np

def get_prob(throw, theta):
	return pow(theta, throw.count('H')) * pow(1 -theta, len(throw) - throw.count('H'))

def step_E(throws, theta_A, theta_B):

	tab_bayesA=[]
	tab_bayesB=[]
	tab_headsA =[]
	tab_headsB = []

	prob_A = 0.0
	prob_B = 0.0
	bayes_A = 0.0
	bayes_B = 0.0
	num_headsA = 0.0
	num_headsB = 0.0


	for i in throws:

		count_H = i.count('H')
		count_T = i.count('T')

		prob_A = get_prob(i, theta_A)
		prob_B = get_prob(i, theta_B)

		bayes_A= prob_A/(prob_A + prob_B)
		tab_bayesA.append(bayes_A)

		bayes_B = prob_B/(prob_A + prob_B)
		tab_bayesB.append(bayes_B)

		num_headsA = bayes_A * count_H
		tab_headsA.append(num_headsA)

		num_headsB = bayes_B * count_H
		tab_headsB.append(num_headsB)

	return tab_bayesA, tab_bayesB, tab_headsA, tab_headsB

def step_M(heads_A, heads_B, prob_A, prob_B, length):

	new_thetaA = sum(map(float,heads_A))/ (length * (sum(map(float,prob_A))))
	new_thetaB = sum(map(float,heads_B))/ (length * (sum(map(float,prob_B))))

	return new_thetaA, new_thetaB



def EM(throws, theta_A, theta_B, iters=6):
    theta_A = theta_A or random.random()
    theta_B = theta_B or random.random()
    thetas = [(theta_A,theta_B)]

    for n in range(iters):
    	print("%d:\t%0.2f %0.2f" % (n, theta_A, theta_B))
    	probA, probB, heads_A,heads_B = step_E(throws,theta_A,theta_B)
   
    	for i in throws:
    		length = len(i)


    	theta_A, theta_B = step_M(heads_A, heads_B, probA, probB, length)
    	thetas.append((theta_A,theta_B))
    
    return thetas


throws = [ "HTTTHHTHTH", "HHHHTHHHHH", "HTHHHHHTHH", 
          "HTHTTTHHTT", "THHHTHHHTH" ]

thetas = EM(throws, 0.6, 0.5, iters=6)