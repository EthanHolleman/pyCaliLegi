import argparse


def get_args():
    parser = argparse.ArgumentParser('A small selenium based Python program built by the UC Davis Legeslative Affairs Committee to help automate California legistlation tracking.')
    parser.add_argument('outpath', metavar='O', help='Path to output file (csv).')
    parser.add_argument('-and', '--and_keywords', type=str, nargs='+', help='Keywords to search for bills by using "AND" qualifier. Specify up to three words.')
    parser.add_argument('-or', '--or_keywords', type=str, nargs='+', help='Keywords to search for bills by using "OR" qualifier. Specify up to three words.')
    parser.add_argument('-sum_size', '--max_summary_size', type=int, help='Max number of sentences in include in extended summary.')
    parser.add_argument('-headless', '--headless', action='store_true', help='Run browser in headless mode.')

    return parser.parse_args()