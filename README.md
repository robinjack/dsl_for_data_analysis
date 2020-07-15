# dsl_for_data_analysis

This repository contains a DSL for data analysis, created as a project by Robin Jack for his MSC Computer Science at Birkbeck.

The DSL's language is discussed further in the grammar section,
but there are three main parts to this repo:
1. A grammar for data analysis 
2. A semantic model describing a Data object and an Analysis Flow (a record of the state of the data after each function is applied to it)
3. An evaluator to run the code written in this language
4. A REPL that allows us to execute code in this language in an iterative fashion // stretch goal 

## Instructions for Installation
Need to use pipenv + install the pipfile

need to do the below if you want to visualise the model:
 
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
* DSL Directory
    * analysis_flow.tx
    * data_sql.tx -- we add in a way for analysts to use a language they are familiar with
    * evaluator.py -- a file that reads the grammar, populates the AST
    and then evaluates it according to the semantic model
* Example Directory
    * simple_model.analysis -- this will be some example code
* Utils
    * repl.py - includes a REPL for the DSL
    * visualisation -- includes code to visualise a model
    * const.py -- includes the constants for the project



## Sources
The source library for the work here is the TextX Python Parser library.

The parser generator grammar docs can be found here 
http://textx.github.io/textX/stable/grammar/


##  Things to investigate / reading:
1. https://dbader.org/blog/writing-a-dsl-with-python#.

