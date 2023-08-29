import time
import random
import threading
import os
import matplotlib.pyplot as plt
import numpy as np

def failure():
    print(" Timer is over, too slow !")
    os._exit(0)

def compute_EV(info,maxi,extreme = None):
    #compute the expected value for the exercise
    sumValue = 0
    for element in info: 
        if (element is np.nan) and (extreme is None):
            sumValue += maxi/2
        elif ((element is np.nan) and (extreme=='max')):
            sumValue+=maxi
        elif ((element is np.nan) and (extreme=='min')): 
            sumValue+=0
        else: 
            sumValue+=element

    return round(sumValue/len(info),1)

def test_price(value):
    try:
        value = float(value)
        if value <0:
            raise "Price cannot be negative"
    except :
        raise "Price needs to be a float"
    return round(value,1)


def main():
    print("Welcome in this market making mental game")
    print("Prices will be rounded to 1 decimal")
    print("=====SETUP========")
    print("Select the number of steps")
    nb_step_needed=True
    #wait for a correct number of step input
    while nb_step_needed :
        nb_step = input()
        try :
            nb_step = int(nb_step)
            print("You have picked "+ str(nb_step) + " steps")
            if (nb_step <=0):
                print("The number needs to be more than 0")
            else:
                nb_step_needed = False
        except : 
            print("Please give an integer 1 or above")
    print("Select the range of the price:")
    nb_range_needed = True 

    #wait for a correct range input
    while nb_range_needed:
        nb_range=input()
        try: 
            nb_range=int(nb_range)
            print("You have chosen a range from 0 to "+str(nb_range))
            if(nb_range<=0):
                print("Please provide a number above 0")
            else :
                nb_range_needed = False
        except: 
            print("Please give an integer 1 or above")

    #wait for a valid timer input
    timer_needed = True
    print("Select the amount of time you want per round to calculate your bid/ask (in seconds)")
    while timer_needed:
        timer_s=input()
        try: 
            timer_s=int(timer_s)
            print("You have chosen a calculating time per round of "+str(timer_s) + " seconds")
            if(timer_s<=0):
                print("Please provide a number above 0")
            else :
                timer_needed = False
        except: 
            print("Please give an integer 1 or above")
    #GAME
    print()
    print("PRESS ENTER WHEN READY")
    input()
    print("GAME STARTING, YOU HAVE "+ str(timer_s) +"S TO COMPLETE ROUND")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    informations = [np.nan]*nb_step #value information, updated each round
    choices = [x for x in range(0,nb_range+1)] #data to randomly pick from

    #info for graph
    Delta = []
    Spreads = []
    Spread_balance = []
    Bids =[]
    Asks = []
    Times = []
    Mids = []
    Highers = []
    Lowers=[]
    #rounds
    for i in range(nb_step):
        t = threading.Timer(timer_s, lambda:failure())
        #compute EV
        Highers.append(compute_EV(informations,nb_range,"max"))
        Lowers.append(compute_EV(informations,nb_range,"min"))
        Mids.append(compute_EV(informations,nb_range))

        start = time.time()
        print("=== Round "+str(i+1)+" ===")
        print("Current information:",informations)
        t.start()
        bid = input("Buy stock at maximum: ")
        bid = test_price(bid)
        ask = input("Sell stock at mininum: ")
        ask = test_price(ask)
        t.cancel() #end of timer
        end = time.time()
        Bids.append(bid)
        Asks.append(ask)
        Times.append(end-start)
        if i != nb_step:
            informations[i] = random.choice(choices)
        Spreads.append(ask-bid)
    #Plotting results
    X = [x+1 for x in range(nb_step)]
    mxs = [nb_range]*nb_step
    mns = [0]*nb_step
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(X,Highers,label="Higher limit of uncertainty",color='red',linestyle='--')
    plt.plot(X,Lowers,label='Lower limit of uncertainty',color='red')
    plt.plot(X,Mids,color="green",label="True expected value")
    plt.plot(X,Bids,color="blue",label="Your Bids")
    plt.plot(X,Asks,color="blue",linestyle="--",label="Your Asks")
    plt.fill_between(X, Asks, Bids, color='mintcream')
    plt.fill_between(X, mns, Lowers, color='lightcoral') #highlighting zone outside of possible expected values at time
    plt.fill_between(X, mxs, Highers, color='lightcoral')




    plt.title("Performance of Game | Average calculation time: "+str(round(np.mean(Times),1))+'s')
    plt.legend()
    plt.ylabel('Value')

    plt.xlabel('Rounds')
    plt.ylim(0, nb_range) 
    for i, v in enumerate(Mids):
        ax.annotate(str(v), xy=(i+1,v), xytext=(-7,7), textcoords='offset points',color='green')
    plt.show()

main()
