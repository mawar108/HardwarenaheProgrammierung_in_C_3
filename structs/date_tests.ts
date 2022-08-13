#include "date.h"

#include <stdlib.h>
#include <string.h>

#define ck_assert_ptr_nonnull_hwp(X) ck_assert_ptr_ne(X, NULL)

#test test_is_friday_13th
    date* d = create_date(13, 4, 2021, 5);
    ck_assert_ptr_nonnull_hwp(d);
    ck_assert(is_friday_13th(d));
    free(d);

#test test_is_not_friday_but_13th
    date* d = create_date(13, 4, 2021, 4);
    ck_assert_ptr_nonnull_hwp(d);
    ck_assert(!is_friday_13th(d));
    free(d);

#test test_is_friday_but_not_13th
    date* d = create_date(14, 4, 2021, 5);
    ck_assert_ptr_nonnull_hwp(d);
    ck_assert(!is_friday_13th(d));
    free(d);

#test test_is_nether_friday_nor_the_13th
    date* d = create_date(15, 4, 2021, 2);
    ck_assert_ptr_nonnull_hwp(d);
    ck_assert(!is_friday_13th(d));
    free(d);

#test test_string_len
    date* d = create_date(15, 12, 2002, 4);
    ck_assert_ptr_nonnull_hwp(d);
    char* s = date_to_string(d);
    ck_assert_ptr_nonnull_hwp(s);
    ck_assert_int_eq(strlen(s), 10);
    free(d);
    free(s);

#test test_string_day_padded
    date* d = create_date(5, 10, 2021, 0);
    ck_assert_ptr_nonnull_hwp(d);
    char* s = date_to_string(d);
    ck_assert_ptr_nonnull_hwp(s);
    ck_assert_str_eq(s, "05.10.2021");
    free(d);
    free(s);

#test test_string_year_padded_1
    date* d = create_date(15, 10, 123, 0);
    ck_assert_ptr_nonnull_hwp(d);
    char* s = date_to_string(d);
    ck_assert_ptr_nonnull_hwp(s);
    ck_assert_str_eq(s, "15.10.0123");
    free(d);
    free(s);

#test test_string_year_padded_2
    date* d = create_date(15, 10, 12, 0);
    ck_assert_ptr_nonnull_hwp(d);
    char* s = date_to_string(d);
    ck_assert_ptr_nonnull_hwp(s);
    ck_assert_str_eq(s, "15.10.0012");
    free(d);
    free(s);

#test test_string_year_padded_3
    date* d = create_date(15, 10, 1, 0);
    ck_assert_ptr_nonnull_hwp(d);
    char* s = date_to_string(d);
    ck_assert_ptr_nonnull_hwp(s);
    ck_assert_str_eq(s, "15.10.0001");
    free(d);
    free(s);

#test test_string_month_padded
    date* d = create_date(15, 4, 2021, 0);
    ck_assert_ptr_nonnull_hwp(d);
    char* s = date_to_string(d);
    ck_assert_ptr_nonnull_hwp(s);
    ck_assert_str_eq(s, "15.04.2021");
    free(d);
    free(s);

#test test_string_all_padded
    date* d = create_date(5, 4, 2, 0);
    ck_assert_ptr_nonnull_hwp(d);
    char* s = date_to_string(d);
    ck_assert_ptr_nonnull_hwp(s);
    ck_assert_str_eq(s, "05.04.0002");
    free(d);
    free(s);

#test test_string_earliest
    date* d = create_date(1, 1, 0, 0);
    ck_assert_ptr_nonnull_hwp(d);
    char* s = date_to_string(d);
    ck_assert_ptr_nonnull_hwp(s);
    ck_assert_str_eq(s, "01.01.0000");
    free(d);
    free(s);

#test test_string_latest
    date* d = create_date(31, 12, 9999, 0);
    ck_assert_ptr_nonnull_hwp(d);
    char* s = date_to_string(d);
    ck_assert_ptr_nonnull_hwp(s);
    ck_assert_str_eq(s, "31.12.9999");
    free(d);
    free(s);

