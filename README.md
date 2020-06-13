## Problem Statement
To implement a NxN Brent-Kung-Adder where N is defined by the user


## Installation requirements 
1. python3 
2. iverilog 
3. GtkWave only if you know how to modify the test-bench code and insert $Display there and <br />
to save the file as .vcd. 

## Installation steps 
### This system was tested on Ubuntu-18.04 so can't say explicitly about WIndows
1. sudo apt install iverilog
2. sudo apt-get install python3 
3. sudo apt install gtkwave


### How it works ?
All the source is present in ```/src```. The module ```/src/base_module``` acts as Base Class that <br /> different modules like Black, Gray, Buffer, SumLOgic, PGLogic etc. inherets and expand its definition and input/output ports, different instructions to print in the actual {source}.v

### What you have to do ?
1. You can change the bit-width such that it is always 2**k where k is a positive integer , <br />
2. After that run ```bash make_verilog_code.bash```. This will create a directory ```verilog_size_bitsize_{bit-width}```. 
3. After that you have to create the test-bench code to test if the code actually runs.  
4. To create the test-bench-code checkout ```make_verilog_test_bench.bash```. 
5. Run this bash file that compiles an object ```compiled_here``` in the root of the repo .
6. Finally run ```./compiled_here``` to check if the addition operation is correct or not. 

### Gray, Black and Buffer Boxes Exaplined
![Image](Images/boxes_image.png?raw=true "Title")
