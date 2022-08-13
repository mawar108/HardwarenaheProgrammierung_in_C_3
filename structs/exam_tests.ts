#include "date.h"
#include "exam.h"

#include <stdlib.h>
#include <string.h>

#define ck_assert_ptr_nonnull_hwp(X) ck_assert_ptr_ne(X, NULL)

#test test_exam_normal
    date* d = create_date(12, 4, 2021, 3);
    ck_assert_ptr_nonnull_hwp(d);
    struct exam e = create_exam(d, 100);
    ck_assert_int_eq(pass_limit(&e), 50);
    free(d);

#test test_exam_friday_the_13th
    date* d = create_date(13, 9, 2024, 5);
    ck_assert_ptr_nonnull_hwp(d);
    struct exam e = create_exam(d, 100);
    ck_assert_int_eq(pass_limit(&e), 42);
    free(d);

#test test_exam_rounding
    date* d = create_date(12, 10, 2013, 3);
    ck_assert_ptr_nonnull_hwp(d);
    struct exam e = create_exam(d, 31);
    ck_assert_int_eq(pass_limit(&e), 15);
    free(d);

#test test_exam_rounding_friday_the_13th
    date* d = create_date(13, 11, 2033, 5);
    ck_assert_ptr_nonnull_hwp(d);
    struct exam e = create_exam(d, 42);
    ck_assert_int_eq(pass_limit(&e), 17);
    free(d);

