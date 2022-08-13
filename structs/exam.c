#include "date.h"
#include "exam.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct exam create_exam(date *d, int points){
    struct exam klausur;
    klausur.datum = *d;
    klausur.maxPoints = points;
    return klausur;
}

int pass_limit(struct exam *exam){
    int points = exam->maxPoints;
    if(is_friday_13th(&exam->datum)== 1){
        return (points*42/100);
    }
    return (points * 50 / 100);
}



// int main(void)
// {
//     date *a = create_date(13, 12, 53, friday);
//     char *b = date_to_string(a);
//     // printf("%s\n", b);
//     // printf("%d\n", a->day);
//     // printf("%s\n", b);
    
//     // int i = is_friday_13th(a);
//     // printf("%d", i);
//     struct exam test = create_exam(a, 100);
//     struct exam *test2 = &test;
//     printf("%d\n", test.maxPoints);

//     int minpoints= pass_limit(test2);
//     printf("%d\n", minpoints);
// }
