  ____        _     ____                          ____  _  __  __    ____      _            _       _             
 / ___| _   _| |__ |  _ \ __ _ _ __   __ _  ___  |  _ \(_)/ _|/ _|  / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __ 
 \___ \| | | | '_ \| |_) / _` | '_ \ / _` |/ _ \ | | | | | |_| |_  | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
  ___) | |_| | |_) |  _ < (_| | | | | (_| |  __/ | |_| | |  _|  _| | |__| (_| | | (__| |_| | | (_| | || (_) | |   
 |____/ \__,_|_.__/|_| \_\__,_|_| |_|\__, |\___| |____/|_|_| |_|    \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                     |___/                                                                        

OVERVIEW:

The following is the problem statement:

We have been given N days of average home sale price data, and a fixed window size K. For each window of K days, from left to right, we have to compute the number of increasing subranges within the window minus the number of decreasing subranges within the window.

Constraints are as follows:

1 ≤ N ≤ 200,000 days
1 ≤ K ≤ N days

INPUT FORMAT

The solution should accept an input file (input.txt) with the following contents: 

Line 1: 	Two integers, N and K
Line 2: 	N positive integers of average home sale price, each less than 1,000,000

OUTPUT FORMAT

The output must be one integer for each window’s result, with each integer on a separate line, either to an output file or to the console.


WHAT DOES THIS PROGRAM DO:

This application would return patterns across windows of certain sizes, and will efficiently track trends such as increasing and decreasing subranges.