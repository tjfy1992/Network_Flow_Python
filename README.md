A python implemenation of calculating the max flow of a flow network.
The implementation uses two algorithms: Simplex Algorithm(linear programming) and Ford-Fulkerson Algorithm.

The project is written in Pycharm for Windows. Python version is 3.7.4 x64, pytest version is 5.1.2.
The project uses the graph library at https://github.com/tjfy1992/GraphLibraryPython as its library for Ford-Fulkerson Algorithm.

To run the program with Simplx Algorithm, run
runner.bat simplex

To run the program with Ford-Fulkerson Algorithm, run
runner.bat Ford-Fulkerson

The input network flow is as following.
![alt text](https://github.com/tjfy1992/Network_Flow_Python/blob/master/Input.PNG)

The two algorithms will give same results.
The output network flow is as following. The max flow is 10 + 5 + 13 = 9 + 9 + 10 = 28.
![alt text](https://github.com/tjfy1992/Network_Flow_Python/blob/master/Output.PNG)
