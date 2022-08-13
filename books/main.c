// Diese Datei darf nicht verändert werden!

#include "books.h"
#include <stdio.h>

void print_library(Book *list) {
    for (Book *book = list; book != NULL; book = book->next){
        printf("ISBN: %s, Year: %d, Title: %s\n", book->isbn, book->year, book->title);
    }
}

int main(void) {
    Book *list = read_library();

    print_library(list);

    free_library(list);

    return 0;
}
