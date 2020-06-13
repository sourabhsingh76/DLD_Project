# This file enables the user to write the test-bench code 

# Lets write the test.v to the verilog code folder
bitwidth=64
folder_path="./verilog_code_bitsize_$bitwidth"
filename="test_bench.v"

python3 make_test_bench.py --path $folder_path \
                            --filename $filename \
                            --bitwidth $bitwidth


# Now lets compile the verilog source and see the result 
function compile_source(){
    out_name="compiled_here"
    iverilog -o $out_name $folder_path/*   
}

compile_source