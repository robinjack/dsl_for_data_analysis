This section contains the grammar of the DSL and the evaluator class, along with 
tests.

https://github.com/textX/textX/issues/24

Notes:
TODO: the analysis_flow grammar is a PEG rather than a CFG, which means that 
there are some issues with parsing arithmetic expressions. 

I have managed to get expression parsing working in order to create an ast,
as long as  