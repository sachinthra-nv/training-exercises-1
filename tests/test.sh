# cat src/data/capk.yaml | grep image: -A1
# cat src/data/final.yaml | grep imagePullPolicy: | wc -l
# cat src/data/capk.yaml | grep imagePullPolicy: | wc -l

BASE_INPUT="src/data"
BASE_OUTPUT="src/data"
declare -i failed=0


function testUT1() {

    # $1 Contains FROM file path
    # $2 Contains TO file path
    ORGINAL_IMAGE_TAG=`cat $1 | grep image: | wc -l`
    FINAL_IMAGE_TAG=`cat $2 | grep image: | wc -l`

    echo "Input file:$ORGINAL_IMAGE_TAG | Output File:$FINAL_IMAGE_TAG"

    if [ $ORGINAL_IMAGE_TAG == $FINAL_IMAGE_TAG ]; then
        echo "Unit Test 1 - Passed!!!"
    else
        echo "Unit Test 1 - Failed"
        failed=$(( failed + 1 ))
    fi

}

function testUT2() {

    # $1 Contains FROM file path
    # $2 Contains TO file path
    ORGINAL_IPP_TAG=`cat $1 | grep imagePullPolicy: | wc -l`
    FINAL_IPP_TAG=`cat $2 | grep imagePullPolicy: | wc -l`
    CHANGED=$(expr $FINAL_IPP_TAG - $ORGINAL_IPP_TAG)

    echo "Input file:$ORGINAL_IPP_TAG | Output File:$FINAL_IPP_TAG"

    if [ $CHANGED != 0 ]; then
        echo "Unit Test 2 - Changed/Added $CHANGED imagePullPolicy Tag"
    else
        echo "Unit Test 2 - No additional imagePullPolicy Tag"
    fi

}

function unitTeseCase()
{
    # $1 contains the index
    FROM="$BASE_INPUT/$1.yaml"
    TO="$BASE_OUTPUT/$2.yaml"

    echo "\n=================================================="
    echo "Tests between $1.yaml and $2.yaml file"
    testUT1 $FROM $TO 
    testUT2 $FROM $TO 

    return 1
}

echo "=================================================="
echo "Unit Test 1 - Number of image Tag"
echo "Unit Test 2 - Number of imagePullPolicy Tag Changed/Added"
echo "=================================================="

echo Base Input  : $BASE_INPUT
read BASE_INPUT_FILE
echo Base Output : $BASE_OUTPUT
read BASE_OUTPUT_FILE
unitTeseCase "$BASE_INPUT_FILE" "$BASE_OUTPUT_FILE"
# unitTeseCase "capk" "final"

echo "\n=================================================="
echo "TestCases Failed: $failed"
echo "=================================================="
