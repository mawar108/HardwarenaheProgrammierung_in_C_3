#include <stddef.h>

// Read all words from standard input and return them as a 2d-array.
// The number of words read is returned through the pointer num_words.
char** read_words(size_t *num_words);

// Print each word with a number in front like:
// 1 first
// 2 second
// 3 third
void print_words(char **words, size_t num_words);

// Release the allocated memory.
void free_words(char **words, size_t num_words);
