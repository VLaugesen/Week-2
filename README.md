# Week-2
Repository for the week 2 assignment

## Description
This is the repository containing solutions to each of the four sub-tasks for the first week's
data management assignment. Each task is located in its own directory as a Jupyter Notebook,
as well as a regular python script.

- Data: Contains data used by all the sub-tasks
- Delopgave-1: Contains code related to the name list sub-task
- Delopgave-2: Contains code related to the loganalysis sub-task
- Delopgave-3: Contains code related to the error handling sub-task
- Delopgave-4: Contains code related to the pandas sub-task

## Dependencies
Required python packages can be found in *requirements.txt*
The main used packages are matplotlib, wordcloud, and pandas.

## Running the program
In order to run each program, navigate to one of the "delopgave" directories. The either run the corresponding notebook 
or the identical python script with for example:

`python navneliste.py`

## Reflections on difficulties
For the most part it was a relatively straight forward assignment. However, there were still a few things I struggled with:

- Clarification on what task 3 was asking for. I found it a bit difficult to interpret what the task was asking for in terms of requirements.
    For example, what format is considered "wrong" for the data, what exactly to do when encountering the errors.
    In the end I opted to report invalid lines in the console, while saving all the valid lines to the destination file. 

- Unfamiliarty with pandas. I've mainly worked with numpy before and not much with pandas, so understanding the dataframes and groupby function took some time to figure out

- Figuring out how to approach opening the files for writing in sub-task 2. My first instinct was to open a writeable file for each type of log and go through the full log, one at a time. However, this seemed very inefficient, so I instead open a file for all of them at once and only go through the log once. I wanted to include an option to provide which log types to analyse, but struggled with figuring out how to open a dynamic number of files without knowing ahead of time, and opted to hard-code opening the four types present.