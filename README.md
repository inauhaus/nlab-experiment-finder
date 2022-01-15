# nlab-experiment-finder

The file to work with is a Jupyter notebook called 'build-dataframe.ipynb'. You need to have the /AnalyzerFiles/ folder somewhere on your local machine, and you need to include this path in the notebook. 

/AnalyzerFiles/ has a .analyzer file for just about every experiment ever performed in the Nauhaus Lab. An .analyzer file contains a MATLAB structure with over a hundred experimental parameters (columns). There are a few thousand of these .analyzer files (rows).


One of the first cells in the notebook loops through every file in .analyzer files, loads it, and transforms it so that it is ammenable to append as single row of a relational data base. 

Subsequent cells in the notebook gives examples of how to query from this data base. The first example shows you how to get all the Kalatsky widefield experiments.
