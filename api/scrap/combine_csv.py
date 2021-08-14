import os
import glob
import pandas as pd


def combine_csv():
    file_extension = '.csv'
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    prev_dname = os.getcwd()
    os.chdir(dname + r"\\out")
    all_filenames = [i for i in glob.glob(f"*{file_extension}")]
    # combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

    # Take back dir state 
    os.chdir(prev_dname)

    # export to csv

    combined_csv.to_csv("data/data.csv",
                        index=False, encoding='utf-8-sig')
