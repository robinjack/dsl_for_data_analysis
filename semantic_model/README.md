# Semantic Model for Analysis Flow

Analysis flow looks like:
1. Ingestion
2. Analysis
3. Manipulate
4. Train
5. Test --> return to step 2 and iterate until satisfied
6. Finalise analysis



#Ingestion
We will begin with only loading from a filepath.
$VARNAME LOAD $FP

#Analysis
This can involve a variety of different forms. However, we are going to
be starting with only NUMERICAL data, in order to simplify our
working.

There are several things you want to do when you first look
at some data. But they fall into three categories:
- Summary statistics of one column, or two columns compared
- Viewing individual rows
- plotting the data

## Summary statistics
We will begin with a simple language, that will just allow us to
do the SUM, COUNT and PERCENTILE functions.
We expose these three initially as you can derive many other
important functions through these.

These functions will be able to accept a column name and return a value.

## Viewing individual rows

In order to understand your data, the human eye is often better
than any machine. You need to look at the actual values
themselves.

We will expose the data through
$dataname VIEW $startindex:$end_index



#Manipulation

Once you have analysed the data and obtained some conclusions
you want to manipulate the data to improve your model.

You might do this in the following ways:
1. Filter
2. Map

We will look to manipulate the data in a SQL-like language.
SELECT *, col1 + 1 as new_col from $data
where col2 > 10

# Train
As the notion of training is embedded within the work we
are doing, the programmer will not have to calculate
a test set, as that will already be created
so the idea is to set the Y on the data, and then
allow the programmer to train  a model on the training data

We will initially only allow linear regression (as this DSL
will focus particularly on linear-regression) but we coulc
expand this out to include other

$DATA TRAIN


#Test

Same as training the data - we just need to train the data
on the right thing.

Similar to above, the majority of the work will be done in
the manipulation phase. This phase will be very simple,
you will evaluate the results on the test data
