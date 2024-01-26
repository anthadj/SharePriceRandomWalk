#Libraries
import sys                          #User interaction
import matplotlib.pyplot as plt     #Ploting of results
import timeit                       #Timing code performance
import numpy as np



#Method to plot probability distribution and output probability of price being 1000
def output_data(allPrices, n_steps, n_simulations):

    #Separate y-axis and x-axis data
    x_axis = list(allPrices.keys())
    y_axis = allPrices.values()

    #Normalise y_axis
    y_axis = list(map(lambda num: num/n_simulations , y_axis))

    #Make sure y-axis values add up to 1
    print ('Total probability adds up to: ', sum(y_axis))

    #Set figure size so that labels and axis are visible
    plt.figure(figsize = (18.5, 9))

    #Plot bar chart
    plt.bar(x_axis,y_axis,1.7)

    #Specify x-axis ticks
    plt.xticks(x_axis)

    #Label axis and add title
    plt.xlabel('Final Prices ($)', fontweight='bold', fontsize='17', horizontalalignment='center')
    plt.ylabel('Probability of final share price', fontweight='bold', fontsize='17', horizontalalignment='center')
    plt.title('Probability distribution of share price with ' + str(S) + ' steps and ' + str(N) + ' simulations.', fontweight='bold', fontsize='17')

    #Add text showing probability of each bar and store prob of price being 1000
    probOfPrice1000=0
    for i in range(len(x_axis)):
        plt.text(x_axis[i], y_axis[i], y_axis[i], ha='center')
        
        #Store probability of final price being 1000 +- 1%
        if x_axis[i] <= 1010 and x_axis[i] >= 990:
            probOfPrice1000 += y_axis[i]*100

    #plt.show()
    plt.savefig('../outputs/ProbDistPer_S='+str(n_steps)+'_N='+str(n_simulations),bbox_inches='tight')

    #Print result of probability for price being 1000
    print('Probability for final price to be 1000 is found to be:', probOfPrice1000, '%')

    #Output probability of price being 1000 to txt file
    with open('../outputs/ProbPer_Price=1000_S='+str(n_steps)+'_N='+str(n_simulations)+'.txt', 'w') as myFile:
        myFile.write(str(probOfPrice1000)+'%')



def monte_carlo_Simulations(n_steps, n_simulations):

    #Generate an NxS matrix of random numbers, of values feither 0.99 or 1.01
    #with equal probability. The two values repesent an increase and decrease of 1%
    #Rows represent simulations, columns represent random numbers for each step.
    #np.random.randint is the one of the fastest ways to generate loads of random ints.
    randomNumberMatrix = np.random.choice([0.99, 1.01], size=(n_simulations, n_steps))

    #Calculate final price for each simulation
    allPrices={}
    for simulationRandomNums in randomNumberMatrix:

        #numpy.prod multiplies all numbers in list. We also use the round function
        #we round our number to 4 decimal places because when we multiply numbers
        #sometimes small deviations occur i.e. 10 will be 10.000000001 which will
        #return wrong results
        price = round(1000 * np.prod(simulationRandomNums), 4)
        
        
        #Add price in dictionary of prices. If price exists incremenet counter by 1
        if price in allPrices: allPrices[price] += 1
        else: allPrices[price] = 1
    
    #Plot probability distribution and output probability of price being 1000
    output_data(allPrices, n_steps, n_simulations)



#Code always starts from this point. This is the main function
if __name__ == '__main__':

    '''Example usage:
        In terminal:
        python randomWalkPercent.py 100 10000
        100 = Steps in each simulation
        10000 = Number of simulations to run
    '''

    #Start timer
    start = timeit.default_timer()
    
    #Get values for steps in each simulations (S) and
    #number of simulations (N) through command line
    #try command attempts to get values from command lineand turn them into an int.
    #If that is not possible, it prints error messages and exits.
    try:
        S = int(sys.argv[1])
        N = int(sys.argv[2])
    except:
        print("\n!Error while running code!")
        print("To run the code use a command line as shown: \n")
        print("python randomWalkPercent.py 50 1000 \n")
        print("where 50 is the number of steps and 1000 the number of simulations.")
        print("Numbers must be ints.\n")
        exit(0)
    
    #Run MonteCarlo simulations for all N simulations with S steps
    monte_carlo_Simulations(S, N)

    stop = timeit.default_timer()
    execution_time = stop - start
    print("Code ran with", S, "steps and for", N, "simulations.")
    print("Program Executed in "+str(execution_time)+" seconds")
