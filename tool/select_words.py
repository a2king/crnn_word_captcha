#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2020/10/11 0:17
# Project: 
# @Author: CYG
# @Email : siqi@yscredit.com
import argparse
import os
import sys

"""遍历文件夹"""


def select_word(folder_path):
    all_word = []
    root = folder_path
    for dirpath, dirnames, filenames in os.walk(root):
        for filepath in filenames:
            label = filepath.split("_")[0]
            for s in label:
                if s not in all_word:
                    all_word.append(s)
    return all_word


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--trainfolder', type=str, required=True, help='path to folder which contains the images')
    parser.add_argument('--testfolder', type=str, help='path to folder which contains the images')
    args = parser.parse_args()

    if args.trainfolder is not None and args.testfolder is not None:
        all_words = []
        all_words += select_word(args.trainfolder)
        all_words += select_word(args.testfolder)
        with open('all_word', 'w', encoding='utf-8') as f:
            for w in all_words:
                f.write("{}\n".format(w))
        print("All text has been written to the file")
    else:
        print('Please use --trainfolder and --testfolder to assign the input. Use -h to see more.')
        sys.exit()
