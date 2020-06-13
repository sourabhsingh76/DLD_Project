#!/bin/bash

# Bitwidth
bitwidth=64
# Output Path
output_path="./verilog_code_bitsize_$bitwidth"
# Adder Type
addertype="brent_kung"

python3 main.py --adder-type $addertype \
                --path $output_path \
                --bitwidth $bitwidth 