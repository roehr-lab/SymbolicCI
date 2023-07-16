# This is a Make file to build and run cgcCALC 

# in both testing and library
CC = g++ -O3  -I./include -shared -std=c++17 -fPIC
#CC = em++ -O3  -I./include  -s "EXPORTED_RUNTIME_METHODS=['ccall','cwrap']" -s NO_EXIT_RUNTIME=1 -sEXPORTED_FUNCTIONS=_main,_CG,_DecToFrac
#added for the testing files
CFLAGSTEST = -std=c++17 -Wall -Wextra -Wconversion 
 
#source files 
SRCCGCCALC = src/utilities.cpp \
                 src/cgc.cpp \
                 src/latex.cpp \
                 src/layout.cpp
#include files 
INCLUDECGCCALC = include/utilities.h \
                 include/cgc.h \
                 include/latex.h \
                 include/layout.h                               
#tes
TESTCGCCALC = getCGC
#em++ a1.cpp  -o a1.html  -s "EXPORTED_RUNTIME_METHODS=['ccall','cwrap']" -s NO_EXIT_RUNTIME=1 -sEXPORTED_FUNCTIONS=_main,_sum
#build the test executable
OUTFILE = cgcCALC$(shell python3-config --extension-suffix)
$(TESTCGCCALC): %: src/%.cpp  
	$(CC) $(CFLAGSTEST)  $(SRCCGCCALC)   $(shell python3 -m pybind11 --includes) -o  $(OUTFILE) $< 
#    $(CC) $(CFLAGSTEST)  $(SRCCGCCALC)  -o cgcCALC.out $< 

#remove executable 

clean:
	rm $(OUTFILE)
    