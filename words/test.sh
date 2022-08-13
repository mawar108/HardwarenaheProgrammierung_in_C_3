#!/usr/bin/env bash

CFLAGS="-g -fsanitize=address -fsanitize=undefined -std=c99 -Wall -Wextra -Werror"
name="words"

# check codestyle
if ! ./codestyle.py
then
    printf "ERROR: Code style violation."
    exit 1
fi

# check code for some errors
if ! ./check_code.py
then
    printf "ERROR: Code does not conform to exercise."
    exit 1
fi

printf '\n'

# Compile program
if ! gcc $CFLAGS main.c "$name.c" -o "$name"
then
    printf 'ERROR: Program could not be compiled.\n'
    exit 1
fi

function test_program() {
    input="$1"
    output="$2"
    expected="$3"
    diff_file="$4"

    # Limit stack size
    if ! ulimit -Ss 32
    then
        printf 'ERROR: The program "ulimit" does not appear to work on your computer..\n'
        exit 1
    fi

    "./$name" < "$input" > "$output"

    return_value="$?"

    # Reset stack size limit to default (probably 8192k)
    ulimit -Ss unlimited

    if [ $return_value -ne 0 ]
    then
        printf 'ERROR: The program failed (the return value was %s instead of 0).\n' "$return_value"
        exit 1
    fi

    if diff -y "$output" "$expected" > "$diff_file"
    then
        printf 'OK: %s matches %s.\n' "$expected" "$output"
    else
        printf 'ERROR:\nThe file %s is different from %s. Details in %s.\nThe first few different lines are:\n\n' "$expected" "$output" "$diff_file"
        diff -y --suppress-common-lines "$expected" "$output" | head -n 20
        exit 1
    fi
}

for i in 1 2 3 4
do
    test_program "input$i.txt" "output$i.txt" "expected_output$i.txt" "diff$i.txt"
done

yes | head -n 10000 | tr -d " \n" > 'long_word.txt'

if "./$name" < 'long_word.txt' > 'long_word_output.txt'
then
    printf 'OK: The program does not crash with a long word as input.\n'
else
    printf 'ERROR: The program failed with a long word as input (the return value is not 0).\n'
fi

rm -f 'long_word.txt'
