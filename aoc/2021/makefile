#compiler to use
CC = g++

# flags to pass compiler
FLAGS = -std=c++17 -Wall -Werror

%: %.cc
	$(CC) $(FLAGS) $@.cc -o $@.out

clean: 
	rm -f *.out


