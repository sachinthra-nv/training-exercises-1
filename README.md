# Training Exercises 1
---
> To run I used a package manager NPM and the following are some of the importent commands to run the projects. We can also run using the direct commands instead of using the npm. 
---
#### To run the main program(app.py)
```shell
python3 src/app.py [Source of the YAML file] [Destination of the YAML file/Optional]
```
#### To test the output file to the orginal file run test.sh
We should convert the test.sh to shell script executable then run the file.
```shell
chmod +x tests/test.sh 
tests/test.sh
```
or
```
which will run "chmod +x tests/test.sh && tests/test.sh
```
---

## Run !!

### 1. To run the file run
```
npm start
```
which will run "python3 src/app.py src/data/capk.yaml"

### 2. To test the Output file
```
npm run test
```
which will run "chmod +x tests/test.sh && tests/test.sh"

### 3. To get all the output files for all the test input files 
```
npm run runAppTestCase
```
which will run "chmod +x tests/runAppToTest.sh && tests/runAppToTest.sh"

### 4. To Unit Test all the test output files
```
npm run testUTC
```
this will run "chmod +x tests/testUTC.sh && tests/testUTC.sh"


## Exercise 3 - Creating docker Image (Volume Mount) 
Mount a Volume to the docker image and run the scripts. The yaml files will be located in the docker.

Run by using Docker inside a docker method.

#### Method 1
After creating the Ubuntu Container with all the necessary packages installed (Exercise 2),
> vim, traceroute, net-tools, iputils-ping, netbase, curl, sudo.

```dockerfile
RUN apt-get update
RUN apt-get install -y vim traceroute net-tools iputils-ping netbase curl sudo

# python
RUN sudo apt-get install -y software-properties-common
RUN sudo add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install -y python3.8 python3-pip
```
Then copy the project folder to the image and change directory to the project folder

```Dockerfile
ADD . /export
WORKDIR /export
```
#### Build Image

```shell
docker build -t auto-test-doc . 
```  
#### Creating the container
```shell
docker run -it --name yaml_tag_che auto-test-doc 
```
now that we will inside the ubuntu container and now we can run the project.
Output
```shell
% docker run -it --name yaml_tag_che auto-test-doc
root@f2bbb77f3fa0:/export# ls
Dockerfile  README.md  entry.sh  ex1  ex2  package.json  requirements.txt  src
root@f2bbb77f3fa0:/export# python3 src/app.py src/data/capk.yaml
Found a Line With Image Tag in Line No. 3227  --> Done
Found a Line With Image Tag in Line No. 3906  --> Done
Found a Line With Image Tag in Line No. 7700  --> Done
Found a Line With Image Tag in Line No. 8443  --> Done
Found a Line With Image Tag in Line No. 9200
      - This tag has a Link
      - Next Tag: 9201  --> Done
Found a Line With Image Tag in Line No. 9215
      - This tag has a Link
      - Next Tag: 9216
      - It is a imagePullPolicy tag
      - Tag imagePullPolicy have IfNotPresent  --> Done

OUTFILE:  src/data/final.yaml
root@f2bbb77f3fa0:/export# 
```
### Method 2
In this method we use volume mount method. We will import the just the input data from a host machine to the ubuntu and run the program for the input.

Do all the steps in method 1 from step 1 to 3

Now to create the container we need to volume mount the the folder which has the input file.

```shell
docker run -v "$(pwd)":[volume_name] [docker_image]
```
So i have a folder namer ex-1-vol in root folder of the projects location

If we need to run the entry Command the add the command at the end
```shell
docker run -it \
        -v "/Users/sachinthranv/projects/ex-1-vol":/export/src/hostData \
        --name yaml_tag_che auto-test-doc \
        python3 src/app.py src/hostData/test.yaml
```
or
```shell
sachinthranv@sachinthras-MacBook-Pro training-exercises-1 % docker run -it \
        -v "/Users/sachinthranv/projects/ex-1-vol":/export/src/hostData \
        --name yaml_tag_che auto-test-doc

root@96da39c92910:/export# ls
Dockerfile  README.md  entry.sh  ex1  ex2  package.json  requirements.txt  src
root@96da39c92910:/export# python3 src/app.py src/hostData/test.yaml
Found a Line With Image Tag in Line No. 3227  --> Done
Found a Line With Image Tag in Line No. 3906  --> Done
Found a Line With Image Tag in Line No. 7700  --> Done
Found a Line With Image Tag in Line No. 8443  --> Done
Found a Line With Image Tag in Line No. 9200
      - This tag has a Link
      - Next Tag: 9201  --> Done
Found a Line With Image Tag in Line No. 9215
      - This tag has a Link
      - Next Tag: 9216
      - It is a imagePullPolicy tag
      - Tag imagePullPolicy have IfNotPresent  --> Done
OUTFILE:  src/data/final.yaml
root@96da39c92910:/export# cd src/hostData
root@96da39c92910:/export/src/hostData# ls
ftest.yaml  test.yaml
root@96da39c92910:/export/src/hostData# 
```

### Method 3
In this method lets mount the full project folder to the Ubuntu container

Do all the steps except coping the project files to container, i.e. Step 1 and 3 not 2.

To run from the root directory of the project folder

```shell
docker run -it \
        -v "$(pwd)":/import \
        --name yaml_tag_che auto-test-doc
```
Output

```shell
sachinthranv@sachinthras-MacBook-Pro training-exercises-1 % docker run -it \
        -v "$(pwd)":/import \
        --name yaml_tag_che auto-test-doc
root@c90bb75690f8:/# ls
bin  boot  dev  etc  home  import  lib  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@c90bb75690f8:/# cd import/
root@c90bb75690f8:/import# ls
Dockerfile  README.md  entry.sh  ex1  ex2  package.json  requirements.txt  src  tests
root@c90bb75690f8:/import# python3 src/app.py src/data/capk.yaml
Found a Line With Image Tag in Line No. 3227  --> Done
Found a Line With Image Tag in Line No. 3906  --> Done
Found a Line With Image Tag in Line No. 7700  --> Done
Found a Line With Image Tag in Line No. 8443  --> Done
Found a Line With Image Tag in Line No. 9200
      - This tag has a Link
      - Next Tag: 9201  --> Done
Found a Line With Image Tag in Line No. 9215
      - This tag has a Link
      - Next Tag: 9216
      - It is a imagePullPolicy tag
      - Tag imagePullPolicy have IfNotPresent  --> Done
OUTFILE:  src/data/final.yaml
root@c90bb75690f8:/import# 
```