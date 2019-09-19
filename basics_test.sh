test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest
pycodestyle style.py

pycodestyle get_column_stats.py


(for j in `seq 1 100`; do 
    (for i in `seq 1 100`; do 
        echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
    done )> data.txt

    run random_data python3 get_column_stats.py --file_name data.txt --col_num 2
    assert_exit_code 0
done )


V=1
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

run all_ones python3 get_column_stats.py --file_name data.txt --col_num 2
assert_in_stdout 'mean: 1.0
stdev: 0.0'
assert_exit_code 0

(for j in `seq 1 100`; do 
    (for i in `seq 1 100`; do 
        echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
    done )> data.txt

    run random_data_random_column python3 get_column_stats.py --file_name data.txt --col_num $(($RANDOM % 5))
    assert_exit_code 0
done )

echo -e "$RANDOM\n$RANDOM\nbad\n$RANDOM" > data.txt
run non_number python3 get_column_stats.py --file_name data.txt --col_num 0
asser_in_stdout "Non number found in data."
assert_exit_code 1

run bad_file python3 get_column_stats.py --file_name badfilethatshouldnt.exist --col_num 0
assert_in_stdout 'File does not exist or read access is not given.'
assert_exit_code 1

BADCOLUMN=$(($RANDOM + 5))
echo -e $BADCOLUMN;
run bad_column python3 get_column_stats.py --file_name data.txt --col_num $BADCOLUMN
assert_in_stdout "Column does not exist in data file.
Ensure that every line has $BADCOLUMN values.
Reminder that columns are zero-indexed."
assert_exit_code 1

run style_test pycodestyle get_column_stats.py
assert_no_stdout

