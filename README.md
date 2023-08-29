# Market Making Mental Game #
This little project objective is to help you practice the market making rounds you might find at some trading shops or market makers during your interview process. </br>
The idea is to make market on a random item based on a price serie and provide a bid and ask for it. 
Each round you are provided with an additional information about the value of the item, picked randomly. You are then allowed you to refine the expected value your bid and your ask from there. 
It is single player and there is no AI involved yet, you are only racing against the clock. The faster you get at computing your spread, the better you will be at exploiting other candidates mistakes. 

## Setup ##
The game is coded in python and run directly from the command line. 
To run properly you should have a python 3 installed on your machine as well as the following packages: 
```
- time
- random
- threading
- os
- matplotlib
- numpy 
```

Once you have made sure the following packages are installed in your environment simply run the file with the following command:
```
>> python thefilename.py
```

## Running ##
The game let you choose different settings to adapt the difficulty to your own level. You can choose the number of rounds, the range of possible values for the item, the amount of time allocated to each round of calculation. <br>
At the end of the game, a graph is plotted, displaying the information of the run such as the uncertainty values, the spread, the exact expected value at each round. 

