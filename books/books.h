typedef struct Book Book;

struct Book {
    char title[10 + 1];
    int year;
    char isbn[17 + 1];
    Book *next;
};

Book* read_library(void);
void print_library(Book *list);
void free_library(Book *list);
