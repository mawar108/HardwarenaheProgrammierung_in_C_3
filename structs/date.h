#ifndef HARDPROG_DATE_H
#define HARDPROG_DATE_H

enum weekday
{
    sunday = 0,
    monday = 1,
    tuesday = 2,
    wednesday = 3,
    thursday = 4,
    friday = 5, 
    saturday = 6};

typedef struct
{
    int day;
    int month;
    int year;
    enum weekday weekday;
} date;

date* create_date(int day, int month, int year, enum weekday weekday);
char* date_to_string(date* d);
int is_friday_13th(date* d);

#endif /* HARDPROG_DATE_H */
