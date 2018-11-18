#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
#import math

import glob

import csv
import codecs

#import datetime
#import date
#import time
#from datetime import timedelta
#from math import sin, cos, acos, radians

#関連ライブラリの読み込み
#import numpy as np
#import pandas as pd
#import scipy as sp

from operator import itemgetter


# http://qiita.com/okadate/items/c36f4eb9506b358fb608

'''''''''''''''''''''''''''''''''''''''''''''
CSVファイル読み込み
'''''''''''''''''''''''''''''''''''''''''''''
def read_csv(filename):

    rowlist = []

    try:
        #with codecs.open(filename, "r", "cp932") as f:
        with codecs.open(filename, "r", "utf-8") as f:
            # rfp = csv.reader(f)
            rfp = csv.DictReader(f)

            for row in rfp:
                rowlist.append(row)
                #print(row, sep=",")

    except IOError as e:
        sys.exit('system error: {}'.format(e))

    return rowlist

'''''''''''''''''''''''''''''''''''''''''''''
CSVファイル書き込み
'''''''''''''''''''''''''''''''''''''''''''''
def write_csv(filename, data):

    if os.path.exists(filename):
        os.remove(filename)

    try:
        header = data[0].keys()  # ヘッダー用のデータを作っておく

        # CSVファイル書き込み
        #with codecs.open(filename, 'w', "cp932") as f:
        with codecs.open(filename, 'w', "utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=header, lineterminator='\n')

            # そのままだとヘッダーは書き込まれないので、ここで書く
            #header0 = {}
            #for n in writer.fieldnames:
            #    header0[n] = n
            #writer.writerow(header0)
            writer.writerow(dict((fn, fn) for fn in writer.fieldnames))

            for row in data:
                writer.writerow(row)

    except IOError as e:
        sys.exit('system error: {}'.format(e))

    return True

'''''''''''''''''''''''''''''''''''''''''''''
CSVファイル書き込み
'''''''''''''''''''''''''''''''''''''''''''''
def write_csv_list(filename, data):

    if os.path.exists(filename):
        os.remove(filename)

    try:
        header = ["pref_id","city_id","name","name_ja","name_en","pref_name","pref_name_ja","pref_name_en","status",
                  "lon","lat","zoom_level","jcode","geom","created","updated" ]

        # CSVファイル書き込み
        #with codecs.open(filename, 'w', "cp932") as f:
        with codecs.open(filename, 'w', "utf-8") as f:
            writer = csv.writer(f, lineterminator='\n')  # 改行コード（\n）を指定しておく

            writer.writerow(header)

            for row in data:
                rdata = [row["pref_id"],row["city_id"],row["name"],row["name_ja"],row["name_en"],row["pref_name"],row["pref_name_ja"],
                        row["pref_name_en"],row["status"],row["lon"],row["lat"],row["zoom_level"],row["jcode"],row["geom"],
                        row["created"],row["updated"]]
                writer.writerow(rdata)

    except IOError as e:
        sys.exit('system error: {}'.format(e))

    return True

'''''''''''''''''''''''''''''''''''''''''''''
自治体の人口と施設数リストを保存
'''''''''''''''''''''''''''''''''''''''''''''
'''
def writePopulationsData(filename, pop_list):

    header = ["pref_name", "city_name", "pref_id", "city_id", "mesh", "population", "facility", "traveltimes", "size", "total_size"]

    with open(filename, 'w') as f:
        writer = csv.writer(f, lineterminator='\n')  # 改行コード（\n）を指定しておく
        writer.writerow(header)     # heaer（1次元配列）
        writer.writerows(pop_list)  # data（2次元配列）
'''
'''''''''''''''''''''''''''''''''''''''''''''
リストデータ読み込み
'''''''''''''''''''''''''''''''''''''''''''''
'''
def read_list(listfile):

    try:
        pop_list = []

        # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
        # f = open(infilename, 'r', newline='\r\n')
        f = open(listfile, 'r')
        lines2 = f.readlines()
        f.close()

        # lines2: リスト。要素は1行の文字列データ
        #for line in lines2:
        for ii, line in enumerate(lines2):
            #print("index = {0}".format(index))
            line = line.strip(" \r\n")
            #print(line)

            if len(line) != 0 and line[0] != '#':
                id = re.split('[,\s\t]', line)
                city_id  = int(id[0])

                pref_id = mcf.getPrefId(city_id)
                print("pref_id=%d, city_id=%d" % (pref_id, city_id))

                #pop = getPopulations(pref_id, city_id)
                #pop_list.append(pop)

        return pop_list

    except IOError as e:
        sys.exit('system error: {}'.format(e))
'''

'''''''''''''''''''''''''''''''''''''''''''''
ディレクトリのファイル読み込み
'''''''''''''''''''''''''''''''''''''''''''''
'''
def read_dir(dirpath):
    files = glob.glob(dirpath) # ワイルドカードが使用可能

    pop_list = []
    for file in files:
        if "test" in file:
            continue

        pop = read_list(file)
        pop_list.extend(pop)

    return pop_list
'''
