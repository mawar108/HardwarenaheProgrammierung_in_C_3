// Diese Datei darf nicht verändert werden!
#include "words.h"
#include <stdio.h>

int main(){
    size_t num_words = 666666;
    char **words = read_words(&num_words);
    printf("There are %zu words:\n", num_words);

    print_words(words, num_words);
 
    free_words(words, num_words);

    return 0;
}
