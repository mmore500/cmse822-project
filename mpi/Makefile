EMP_DIR := ../../Empirical/source
CFLAGS_all := -Wall -I$(EMP_DIR)/
CFLAGS_nat := -O3 -DNDEBUG $(CFLAGS_all)

all: main.out

main.out: main.cpp
	h5pcc $(CFLAGS_all) -O3 -std=c++14 -o main.out main.cpp

run: main.out
	mpirun -n 4 main.out

clean:
	rm -f *.out *.o

.PHONY: clean run
