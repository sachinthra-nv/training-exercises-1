# cat src/data/capk.yaml | grep image: -A1

# cat src/data/final.yaml | grep imagePullPolicy: | wc -l
# cat src/data/capk.yaml | grep imagePullPolicy: | wc -l

echo UT1 - Number of image Tag
echo UT2 - Number of imagePullPolicy Tag
echo \\n

ORGINAL_IMAGE_TAG=`cat src/data/final.yaml | grep image: | wc -l`
FINAL_IMAGE_TAG=`cat src/data/capk.yaml | grep image: | wc -l`

if [ $ORGINAL_IMAGE_TAG == $FINAL_IMAGE_TAG ]; then
    echo "UT1 Passed"
else
    echo "UT1 Failed"
fi

ORGINAL_IPP_TAG=`cat src/data/final.yaml | grep imagePullPolicy: | wc -l`
FINAL_IPP_TAG=`cat src/data/capk.yaml | grep imagePullPolicy: | wc -l`
CHANGED=$(expr $ORGINAL_IPP_TAG - $FINAL_IPP_TAG)

if [ $CHANGED != 0 ]; then
    echo "UT2 - Changed/Added $CHANGED imagePullPolicy Tag"
else
    echo "UT2 - No additional imagePullPolicy Tag"
fi

