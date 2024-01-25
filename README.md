# SharePriceRandomWalk
A python script which encapsulates a Monte-Carlo simulation to simulate the progression of a share price for a company X as a random walk.

There are two main codes:
The first is called randomWalkInteger.py.
For randomWalkInteger.py, the share price starts from $1000 and at every time step of the it goes either up or down by $1. The user inputs the number of steps in each simulation and the number of simulations to take place. At the end, the code outputs the probability distribution for the specificied number of steps and the number of simulations as well as the probability that the price of the share will be equal to £1000.  

The second is called randomWalkPercent.py.
This is a more realistic simulation, where instead of the share price either increasing or decreasing by $1 at every time step, it increases or decreases by 1% of the current share price at every time step. 



# How to execute 
In order to execute, the user is advised to create a virtual environment so that the local system remains clean. Then the dependencies will be installed on the virtual environment. Here I describe how to set up a virtual envirnonment using conda. The requirements needed are also included in requirements.txt for clarity, in case the user prefers to use a different virtual environment, or any other methods.

1. First follow instructions and install conda on your local system (https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

2. Create a virtual environment using the command: 
    "conda create -n virtEnv python=3.9.12 anaconda". 
    Whenever prompted, write "yes" or "y" and press enter.
    For reference the virutal environment's name is "virtEnv"
    
3.  Activate the virutal environment using:
    "conda activate virtEnv"
    
4.  Install matplotlib in the virtual environment using the command:
    "conda install -n virtEnv matplotlib"
    
5.  Install numpy in the virtual environment using the command:
    "conda install -n virtEnv numpy"
    
6.  You are now ready to run the code. From the code directory run the code using:
    "python randomWalkInteger.py <S> <N>" to run it using the integer change method, or run 
    "python randomWalkPercent.py <S> <N>" to run it using the percentage change method. 
    The values of <S> and <N> must be replaced with integers. <S> is the number of steps of each simulation and <N> is the number of simulations. If this is not correct, the code will not execute.
    
8.  When finished, deactivate the virtual environment using:
    "conda deactivate"
    
9.  Finally, delete the environemnt using:
    "conda remove --name virtEnv --all"



# Results and files created
Once executed, the code will create the following files:

1. "ProbDistInt_S=<numberS>_N=<numberN>.png" produced by randomWalkInteger.py
   "ProbDistPer_S=<numberS>_N=<numberN>.png" produced by randomWalkPercent.py

2. "ProbInt_Price=1000_S=<numberS>_N=<numberN>.txt" produced by randomWalkInteger.py
   "ProbPer_Price=1000_S=<numberS>_N=<numberN>.txt" produced by randomWalkPercent.py

where <numberS> and <numberN> are the number of steps in each simulation and number of simulations respectively.  

The first file contains the probability distribution plotted as a bar chart, for the chosen S and N numbers.
The second file contains the probability that the share price will be equal to 1000 as a percentage for the chosen S and N numbers. It is important to note that since we are using Monte-Carlo simulations, the result will not be the same every time the code runs with the same N and S numbers. 
It is important to note that the "ProbPer_Price=1000_S=<numberS>_N=<numberN>.txt" file which is calculated using the "randomWalkPercent.py"
code, has the probability of the price to be between $1002 and $998. 



# Check the Monte-Carlo simulations works as intended
To checck the MC simulations converge to the true value for the randomWalkInteger.py code, use the binomial probability mass function to calculate the probability that the price is equal to $1000. Look at the below example.

Upon running the code randomWalkInteger.py many times with the values of S=10 and N=10000, the probability that the share price = $1000 is found to be in the range 24.01% and 25.42%. Of course, it could also be outside of this range since it is a random walk simulation. The inaccuracy will become smaller with a bigger N number, or by taking the average over many repetitions of the code. As the inaccuracy decreases the number should converge to 24.609375% which is the right answer calculated using the binomial probability mass function. This was found using the binomial mass function (found in https://en.wikipedia.org/wiki/Binomial_distribution) and using the values of n=10 and k=5, which means that out of the ten randomly generated values, 5 were +1 and 5 were -1, taking us back to the original value of $1000 for the share price. 



# Questions
For any questions or collaborations, please contact me at antonis.hadjipittas@gmail.com

