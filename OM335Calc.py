# written by Jonathan Kizer; solves Newsvendor (https://en.wikipedia.org/wiki/Newsvendor_model) problems within Normal, Poisson statistical distributions; also solves other related Operations Management problems; requires Scipy
import math
import scipy.stats as stats

def normal():

  CoNormal = float(input("What is the cost of overage, Co (Unit Cost - Salvage)?\n"))
  CuNormal = float(input("What is the cost of underage, Cu (Unit Price - Unit Cost; margin)?\n"))
  critRatioNorm = (CuNormal/(CoNormal + CuNormal))

  stdDev = float(input("What is the Standard Deviation?\n"))
  mean = float(input("What is the mean?\n"))
  zStat = stats.norm.ppf(critRatioNorm)
  zStat = round(zStat,4)
  orderNum = mean + (stdDev * zStat)
  orderNum = round(orderNum, 3)
  print("\n----> Order", orderNum, "units.\n\nNote that this is an exact answer;\nother solutions may differ slightly by rounding/use of table.\n")

def poisson():
  CoPoisson = float(input("What is the cost of overage, Co (Unit Cost - Salvage)?\n"))
  CuPoisson = float(input("What is the cost of underage, Cu (Unit Price - Unit Cost; margin)?\n"))
  critRatioPoisson = (CuPoisson/(CoPoisson + CuPoisson))

# solves EOQ problems (https://en.wikipedia.org/wiki/Economic_order_quantity)
def eoq():
  r = float(input("What is R, the demand rate or flow rate? (note: keep units of time constant throughout)\n"))
  k = float(input("What is K, the fixed ordering cost?\n"))
  p = float(input("What is P, the purchasing cost per unit?\n"))
  h = float(input("What is H, the holding cost (percentage cost multiplied by P) per unit?\n"))
  qStar = math.sqrt((2*r*k)/h)
  qStar = round(qStar, 3)
  qStarCost = (h*(qStar/2)) + (k*(r/qStar))
  
  qStarTotCost = qStarCost + (p*r)
  qStarCost = round(qStarCost,2)
  qStarTotCost = round(qStarTotCost,2)
  print("---->The optimal order quantity is", qStar, ".")
  print("---->The holding and setup cost will be: $", qStarCost)
  print("---->The total cost will be: $", qStarTotCost,"\n")
  
# solves EPQ problems (https://en.wikipedia.org/wiki/Economic_production_quantity)
def epq():
  r = float(input("What is R, the demand rate or flow rate?\n"))
  s = float(input("What is S, the production rate? (note: keep units of time constant throughout)\n"))
  k = float(input("What is K, the fixed ordering cost?\n"))
  p = float(input("What is P, the purchasing cost per unit? (note: can make up if just solving for number of units)\n"))
  h = float(input("What is H, the holding cost (percentage cost multiplied by P) per unit?\n"))
  qStar = math.sqrt((2*r*k)/h)*(math.sqrt(s/(s-r)))
  qStarCost = ((h*(qStar/2))*((s-r)/s)) + (k*(r/qStar))
  qStarTotCost = qStarCost + (p*r)
  qStar = round(qStar,3)
  qStarCost = round(qStarCost,2)
  qStarTotCost = round(qStarTotCost,2)
  print("---->The optimal order quantity is", qStar, ".")
  print("---->The holding and setup cost will be: $", qStarCost)
  print("---->The total cost will be: $", qStarTotCost,"\n")
  
# Solves queue time problems based on Tq formula 
def queueTime():
  m = float(input("What are the number of servers, m?\n"))
  p = float(input("What is the processing time, p? (note: keep units of time constant throughout)\n"))
  a = float(input("What is the interarrival time, a?\n"))
  u = p/(m*a)
  modelType = input("Is the model normal? (Y or N)\n")
  if (modelType == "yes" or modelType == "Yes" or modelType == "y" or modelType == "Y"):
    stdDeva = float(input("What is the standard deviation for interarrival time?\n"))
    stdDevp = float(input("What is the standard deviation for processing time?\n"))
    cVa = stdDeva / a
    cVp = stdDevp / p
  else:
    cVa = float(input("What is the coefficient of variation for interarrival time?\n"))
    cVp = float(input("What is the coefficient of variation for processing time?\n"))
  timeQueue = (p/m) * (u**(math.sqrt(2*(m+1))-1))/(1-u) * ((cVa**2 + cVp**2)/2)
  timeQueue = round(timeQueue,3)
  print("---->Total time in queue:", timeQueue, "units of time.\n")
  
def main():
  print("Accepted input: Normal, Poisson, EOQ, EPQ, Queue Time, Help, About\n")
  model = ""
  while (model != "exit"):
    model = input("What model should be used?\n")
    
    if (model == "normal" or model == "Normal"):
      normal()
    
    elif (model == "poisson" or model == "Poisson"):
      poisson()
      
    elif (model == "EOQ" or model == "eoq"):
      eoq()
    
    elif (model == "EPQ" or model == "epq"):
      epq()
    
    elif (model == "queue time" or model == "wait time" or model == "Queue Time" or model == "Wait Time"):
      queueTime()
    
    elif (model == "about" or model == "About" or model == "help" or model == "Help"):
      print("\nThis program is designed to provide solutions to Newsvendor problems, useful in economics and Operations Management.\n")
      print("Version 0.0.2, written by Jonathan Kizer, and last updated on 12/18/16.\n")
      print("Models for Newsvendor currently include: Normal, Poisson")
      print("Can also solve EOQ, EPQ, and Queue Time problems")
      print("______________________________________\n")
  print("Exiting...") 
main()