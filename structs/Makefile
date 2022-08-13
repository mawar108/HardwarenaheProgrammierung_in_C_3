CC=gcc
CFLAGS=-std=c99 -Og -g -Wall -Wextra -Werror
CHECKFLAGS=$(shell pkg-config --libs --cflags check)
LDFLAGS=-fsanitize=address -fsanitize=undefined

.SECONDARY: date_tests exam_tests

test: codestyle run_date_tests run_exam_tests

exam_tests: exam.o date.o exam_tests.o
	$(CC) -o $@ $^ $(LDFLAGS) $(CHECKFLAGS)

%_tests: %.o %_tests.o
	$(CC) -o $@ $^ $(LDFLAGS) $(CHECKFLAGS)

%_tests.c: %_tests.ts
	checkmk $< > $@

run_%_tests: %_tests
	@printf "\n"  
	./$<
	@printf "\n"

codestyle:
	./codestyle.py
	@printf "\n"

clean:
	rm -f *.o *_tests.c *_tests a.out
