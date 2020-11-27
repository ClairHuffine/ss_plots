import argparse

def get_args(description):
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('--width',
                        type=float,
                        default=3.0,
                        help='Plot width (defult 3)')

    parser.add_argument('--height',
                        type=float,
                        default=3.0,
                        help='Plot height (defult 3)')

    parser.add_argument('--in_file',
                        type=str,
                        required=True,
                        help='Input file')
    
    parser.add_argument('--in_file2',
                        type=str,
                        required=False,
                        help='Input file')

    parser.add_argument('--out_file',
                        type=str,
                        required=True,
                        help='Output file')

    parser.add_argument('--x_label',
                        type=str,
                        required=True,
                        help='X-axis label')

    parser.add_argument('--y_label',
                        type=str,
                        required=True,
                        help='Y-axis label')

    return parser.parse_args()
