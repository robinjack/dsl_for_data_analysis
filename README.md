# dsl_for_data_analysis

This repository contains a DSL for data analysis, created for Birkbeck

## Instructions for Installation
Need to use pipenv + install the pipfile

need to do the below if you want to visualise the mode:
 
brew install graphviz


## Structure of the repo
Overall summary of the semantic model can be found in the README.md in the semantic model folder

In terms of the general plan for the code base:
* Semantic model Directory
    * Data -- class representing a dataset
    * Memento -- class representing the way we store the data
    * AnalysisFlow -- class that connects dataset to method of storing analysis history
* Utils Directory
    * const.py -- all the constants in the 
* Grammar Files
    * analysis_flow.tx
    * evaluator.py -- a file that reads the grammar, populates the AST
    and then evaluates it according to the semantic model
* Example Directory
    * simple_model.analysis -- this will be some example code
* Interpreter Files
    * repl.py



## Sources
The source library for the work here is the TextX Python Parser library.

The parser generator grammar docs can be found here 
http://textx.github.io/textX/stable/grammar/


##  Things to investigate / reading:
1. https://dbader.org/blog/writing-a-dsl-with-python#.

