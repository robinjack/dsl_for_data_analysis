This section contains the grammar of the DSL and the evaluator class, along with 
tests.

https://github.com/textX/textX/issues/24

Notes:
TODO: the analysis_flow grammar is a PEG rather than a CFG, which means that 
there are some issues with parsing arithmetic expressions. 

I have managed to get expression parsing working in order to create an ast,
as long as 


As of 2020-07-15, there is now a functional version of the most simple form of data analysis.
Namely, you look at the data, you choose which variable to train it on, and you


Next steps:

As from the plan, the next big steps are as follows:
1. Manipulation of the columns
2. Filtering of the rows
3. Rewinding of the analysis to a previous point

What do I need for these three sections?
Manipulation

Filtering

Rewinding of the analysis