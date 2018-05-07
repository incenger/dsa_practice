#compiler to use
CC = g++

# flags to pass compiler
FLAGS = -std=c++11 -Wall 

# name for executable
EXE = main

# space-separated list of source files
SRCS = 230B.cpp 


# default target
$(EXE) : $(SRCS)  makefile
	$(CC) $(FLAGS) -o  $@ $(SRCS) 


# housekepping
clean: 
	rm -f core $(EXE) *.o
