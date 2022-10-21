# python3 src/app.py src/data/capk.yaml src/data/abcfinal.yaml

BASE_INPUT="tests/unitTestCases/input"
BASE_OUTPUT="tests/unitTestCases/output"

function runAppForEach()
{
    # $1 contains the index
    FROM="$BASE_INPUT/ut$1.yaml"
    TO="$BASE_OUTPUT/final_ut$1.yaml"

    OUTPUT=`python3 src/app.py $FROM $TO` 
    echo $OUTPUT

    return 1
}

for i in $(seq 1 1 10)
do
    runAppForEach $i
done
