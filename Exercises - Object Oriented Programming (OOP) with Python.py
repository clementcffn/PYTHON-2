#Exercises - Object Oriented Programming (OOP) with Python

#Exercice 1
class Test:
    def __init__(self, n, a):
        self.full_name=n
        self.age=a
    def get_age(self):
        return self.age
    def set_age(self, num):
        self.age=num 
    def __repr__(self):
        return f'Name: {self.full_name}, Age : {self.age}'

a = Test('Clément',24)

##############
import math

class object_1:
    def __init__(self,n):
        self.value = n
    def convert_to_string(self):
        self.value = str(self.value)

instance1 = object_1(10)
instance1.convert_to_string()
instance1.value

#Exercice 2
import math

class Equity:
    def __init__(self,ticker,spot,drift):
        self.ticker = ticker
        self.spot = spot
        self.drift = drift
        
    def __repr__(self):
        return f'Ticker = {self.ticker}, Spot = {self.spot}, Drif = {self.drift}'
    
    def compute_forward(self, T):
        return self.spot * math.exp(self.drift * T)
    
    def compute_spread_forward(self, equity_2, T):
        forward_1 = self.compute_forward(T)
        forward_2 = equity_2.compute_forward(T)
        return forward_1 - forward_2
    
X = Equity("Eurostoxx", 4500, 0.02)
Y = Equity("SPX", 4300, 0.03)
print(X)
X.compute_forward(2)
X.compute_spread_forward(Y, 2)

#Exercice 3

from random import shuffle

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.suit} of {self.value}"

X = Card("Hearts", 7)
print(X)

def create_cards():
    suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
    value = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    list_card = []
    for s in suit:
        for v in value:
            list_card.append(Card(s,v))
            
    return list_card

class Game: 
    def __init__(self):
        self.desk = create_cards()
    def shuffle(self):
        shuffle(self.desk)
        
    def draw(self, n):
        self.hand = []
        for i in range(n):
           temporary_card = self.desk[i]
           self.hand.append(temporary_card) #new card hand
           self.desk.remove(temporary_card)
            
G = Game()
G.shuffle()
G.desk
G.draw(5)
G.hand


#Exercice 4

class Underlying:
    def __init__(self, spot):
        self.spot = spot
        
class Deal:
    def __init__(self, ticker, currency, nominal, strike, underlying):
        self.ticker = ticker
        self.currency = currency
        self.nominal = nominal
        self.strike = strike
        self.underlying = underlying
        
class Call(Deal):
    def __init__(self, ticker, currency, nominal, strike, underlying):
        Deal.__init__(self, ticker, currency, nominal, strike, underlying)

    def get_payoff(self):
        return max(0, self.underlying.spot - self.strike)
    
class Put(Deal):
    def __init__(self, ticker, currency, nominal, strike, underlying):
        Deal.__init__(self, ticker, currency, nominal, strike, underlying)
    
    def get_payoff(self):
        return max(0, - self.underlying.spot + self.strike)
    
SX5E = Underlying(4500)
my_call = Call("call_1", "EUR", 1000, 4600, SX5E)
my_call.get_payoff()