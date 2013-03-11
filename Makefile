# Keeps a few frequent commands
#
cleantemp = rm -rf build; rm -f *.c
TAR = apphot.tar.gz

.PHONY : clean all build

all: clean build

build:  
	python setup.py build_ext --inplace
	$(cleantemp)


clean: 
	$(cleantmp)
	find . -name '*pyc' -exec rm -f {} \;
	rm -f *.so

tar: clean
	tar zcf $(TAR) * 
