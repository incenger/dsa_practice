#compiler to use
CC = g++

# flags to pass compiler
FLAGS = -std=c++11 -Wall -Werror

# name for executable
EXE = main

# space-separated list of header files
HDRS = 

# space-separated list of source files
SRCS = 415B.cpp 

# automatically generated list of object files
OBJS = $(SRCS:.cpp=.o)

# default target
$(EXE) : $(OBJS) $(HDRS) makefile
	$(CC) $(FLAGS) -o  $@ $(OBJS) 

# Dependencies
$(OBJS) : $(HDRS) makefile

# housekepping
clean: 
	rm -f core $(EXE) *.o
