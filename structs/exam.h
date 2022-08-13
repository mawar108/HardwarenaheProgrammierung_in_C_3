#include "date.h"

struct exam
{
    date datum;
    int maxPoints;
};

struct exam create_exam(date* d, int points);

int pass_limit(struct exam* exam);
