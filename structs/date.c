#include "date.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

date* create_date(int day, int month, int year, enum weekday weekday){
    date *datum = malloc(5*sizeof(int));
    datum->day= day;
    datum->month= month;
    datum->year= year;
    datum->weekday=weekday;
    return datum;
}

char *date_to_string(date *d){
    int day = d->day;
    int month= d->month;
    int year = d->year;
    char *format = malloc(11*sizeof(char));
    sprintf(format, "%02d.%02d.%04d", day, month, year);
    return format;
}

int is_friday_13th(date *d){
    int day = d->day;
    int weekday = d->weekday;
    if(day == 13 && weekday == 5){
        return 1;
    }
    return 0;
}
