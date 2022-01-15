# nlab-experiment-finder
The main file is a Jupyter notebook, 'build-data-frame'. You need to have the /AnalyzerFiles/ folder somewhere on your local machine. AnalyzerFiles has a .analyzer file for just about every experiment ever performed in the Nauhaus Lab. An .analyzer file contains a MATLAB structure with over a hundred experimental parameters (columns). There are a few thousand of these .analyzer files (rows).


The first cell loops through all the files to create the Pandas data base. 

Subsequent files gives examples of how to query from this data base. The first example shows you how to get all the Kalatsky widefield experiments.
