#Case study - Eurostoxx / EURUSD Call Contingent pricing

import numpy as np, pandas as pd
import math
import matplotlib.pyplot as plt

class Underlying(): #create a class for Equity / FX underlyings with 3 properties
  def __init__(self, spot, drift, volatility):
    self.spot=spot
    self.drift=drift
    self.volatility=volatility

class MC_simulation():
  def __init__(self, underlying1, underlying2, T, correlation, N_simulations):
    self.underlying1=underlying1 #Underlying object
    self.underlying2=underlying2 #Underlying object
    self.T=T #Maturity in years
    self.correlation=correlation #correlation with udl1 and udl2
    self.N_simulations=N_simulations #number of monte carlo simulation

  def generate_gaussians(self):
    means=[0,0] #mean of each gaussian variable
    covariance_matrix=[[1, self.correlation], [self.correlation, 1]] #covariance matrix with variance 1
    x_gaussian=np.random.multivariate_normal(means, covariance_matrix, self.N_simulations).T #simulated correlated gaussian variables
    return x_gaussian

  def get_MC_distribution(self): #compute the distribution at time T of underlyings 1 and 2
    gaussian_1, gaussian_2=self.generate_gaussians()
    self.S1=self.underlying1.spot * np.exp(self.T * (self.underlying1.drift-0.5*self.underlying1.volatility**2)+self.underlying1.volatility*math.sqrt(T)*gaussian_1) #distribution of udl 1
    self.S2=self.underlying2.spot * np.exp(self.T * (self.underlying2.drift-0.5*self.underlying2.volatility**2)+self.underlying2.volatility*math.sqrt(T)*gaussian_2) #distribution of udl 1

#Class for the payoff
class CallContingent():
  def __init__(self, Strike, T, Notional, Barrier, Currency):
    self.Strike=Strike
    self.T=T
    self.Notional=Notional
    self.Barrier=Barrier
    self.Currency=Currency
  def compute_payoff(self, S1, S2): #payoff value = equity call if FX > barrier, 0 otherwise
    if S2>self.Barrier:
      return max(0, S1-self.Strike)
    else:
      return 0
#Main Class to launch a pricer
class Pricer():
  def __init__(self, MC, contract, discount_rate):
    self.MC=MC
    self.contract=contract
    self.discount_rate=discount_rate

  def compute_price(self):
    #build a 1 dimension vector which computes the final payoff of the contract at maturity for each potential realization of S1, S2
    payoff_vector=[self.contract.compute_payoff(x, y) for x,y in zip(self.MC.S1, self.MC.S2)]
    payoff_average=sum(payoff_vector)/len(payoff_vector) #average payoff at maturity
    PV = payoff_average * math.exp(-self.contract.T * self.discount_rate) #discounted average payoff  = present value
    return PV

SX5E = Underlying(4160, 0.02, 0.25)
EURUSD = Underlying(1.1, 0.01, 0.1)
T=1 #1 year
correlation = 0.3 # 30% positive correlation
NSimu=1000
K=4200
B=1.15
currency="EUR"
notional=1
r_EUR=0.025

new_MC=MC_simulation(SX5E, EURUSD, T, correlation, NSimu) #create the MC object
new_MC.generate_gaussians() #generate the correlated gaussian variables
new_MC.get_MC_distribution() #get the MC distribution for each underlying S1 and S2
ccall=CallContingent(K, T, notional, B, currency) #build a contingent call contract
my_pricer=Pricer(new_MC, ccall, r_EUR) #build a pricer depending on the MC object, contract, discounting rate
PV=my_pricer.compute_price()
print(PV)

####################
list_correlation=np.arange(-0.9, 0.9, 0.1) #list of correlation inputs
list_prices=[] #list of PVs to be completed

for correl in list_correlation:
  new_MC = MC_simulation(SX5E, EURUSD, T, correl, NSimu) #create the MC object
  new_MC.generate_gaussians() #generate the correlated gaussian variables
  new_MC.get_MC_distribution() #get the MC distribution for each underlying S1 and S2
  ccall = CallContingent(K, T, notional, B, currency) #build a contingent call contract
  my_pricer = Pricer(new_MC, ccall, r_EUR) #build a pricer depending on the MC object, contract, discounting rate
  PV = my_pricer.compute_price()
  list_prices.append(PV)
 
plt.plot(list_correlation, list_prices, "*")