import math
import utils.utils as utils
import src.mainlogic.adderbrentkung as brentkung
import os


def _main(args):
    valid_adder_types = ['brent_kung']
    assert args.adder_type in valid_adder_types, 'Error in Adder Type:: Adder Types must be one of {}'.format(
        valid_adder_types)

    assert math.log2(args.bitwidth) == int(
        math.log2(args.bitwidth)), "MUST BE A POWER OF 2"

    if args.adder_type == 'brent_kung':
        if not os.path.exists(args.path):
            os.mkdir(args.path)
        brentkung.write(args.path, args.bitwidth)
    else:
        print('Some Error.')
        exit(-1)


if __name__ == "__main__":
    args = utils.get_args()
    _main(args)