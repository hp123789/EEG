# EEG
collecting and processing EEG signals

lsl_stream.py initializes lsl stream with OpenBCI Cyton Board.

lsl_print.py prints data as timestamp, data (as a list).

lsl_csv.py saves the data in the format of each channel separated by a comma per line. The data is saved in 5 second chunks and every two chunks have a third overlapping them. File name is ite#.csv where # increases starting at 1 as the files increase. Files saved in directory in downloads with date as name.

note: needs to be changed into saving new line and deleting old line and only keeping one file that the algorithm can keep checking.
