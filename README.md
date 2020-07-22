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
* Top Level
    * repl.py - includes a REPL for the DSL
    * Config files(Pipfile for dependencies, pytest settings, gitignore)
* Semantic model Directory
    * Data -- class representing a dataset
    * Memento -- class representing the way we store the analysis flow and allows us to load the previous state
* DSL Directory
    * analysis_flow.tx
    * data_sql.tx -- we add in a way for analysts to use a language they are familiar with
    * evaluator.py -- a file that reads the grammar, populates the AST
    and then evaluates it according to the semantic model
* Example Directory
    * simple_model.analysis -- this will be some example code
    * All other .analysis models. These are in order to demonstrate the DSL
* Utils
    * visualisation -- includes code to visualise a model
    * const.py -- includes the constants for the project



## Sources
The source library for the work here is the TextX Python Parser library.

The parser generator grammar docs can be found here 
http://textx.github.io/textX/stable/grammar/


##  Things to investigate / reading:
1. https://dbader.org/blog/writing-a-dsl-with-python#.


# Plan

* Submit proposal - 5/5 [DONE]
* Design minimally viable semantic model - 5/5 [DONE]
* Create tests for semantic model - 5/21 [DONE - for the data model]
    * TODO - create finalised tests for memento
    * Implement Semantic Model as class model - 5/31 [DONE - for data model + memento]
* Work to pass tests for semantic model - 6/21 [DONE - for data]
    * TODO - pass tests for memento
    * Finalise DSL syntax design - 7/1 [REDO]
    * NOTES - had finished this, but then saw feedback on my proposal. Currently in the process of redoing the analysis.
    * Need to design a BNF/CFG for the language. Can then easily create this in TextX
* Create tests for DSL syntax - 7/6 [DONE v1]
    * TODO - 1. create tests for evaluator class. Notes on 
    * TODO - 2. create tests for program  
    * TODO - 3. rewrite the sample code pieces to run
* Implement DSL syntax in TextX - 7/12 [V1 done - redo]
    * TODO - 1. implement evaluator class [v1 done, except manipulation]
    * TODO - 2. implement the DSL grammar [v1 done, except manipulation]
* Work to pass tests - 7/31
    * TODO - 1. IN PROGRESS
* Gather user feedback - 8/11
* Summarise user feedback - 8/15
* Incorporate updates to DSL - 8/15
* Write report 8/30


