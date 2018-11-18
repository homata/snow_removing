#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
python utilities
'''

__author__  = 'Hiroshi Omata <op.homata@gmail.com>'
__version__ = '0.1'
__date__    = '01 Jan 2018'

# for Python3

import csv # CSVファイル
import sys # モジュール属性 argv を取得するため
import codecs
#from datetime import datetime as dt
from operator import itemgetter
#import configparser
#import argparse
import os

from datetime import datetime as dt
from datetime import datetime, timedelta, timezone

#from czml import czml
#from pygeoif import geometry
import time
#from datetime import date
#from datetime import datetime, timezone, timedelta

#import numpy as np
#import e as e
#import pandas as pd
#import scipy as sp

#import geopy
#import geopy.distance
#from geopy.distance import vincenty
#from geopy.geocoders import Nominatim

import json
#import dateutil.parser
import math

import sys, os
import glob
import random
import zipfile

import traceback

#-----------------------------------------
class utils:
    """
    utilsクラス
    """

    #-----------------------------------------
    def __init__(self):
        """
        クラスの初期化時
        """
        return

    #-----------------------------------------
    @staticmethod
    def conv_iso8601(date):
        """
        JST -> ISO8601日時フォーマット変換 (文字列)
        input date: 2015/09/01 05:01:25 ->  2014-02-12T08:33:20+0900
        """

        tdate = str(date)
        tloc  = datetime.strptime(tdate, '%Y/%m/%d %H:%M:%S')
        tout = tloc.strftime('%Y-%m-%dT%H:%M:%S+0900')
        return tout

    #-----------------------------------------
    @staticmethod
    def conv_date(date):
        """
        JST文字列 -> datetimeオブジェクト
        input date: 20140212083320 ->  2014-02-12　08:33:20+0900
        """
        ldate = str(date) + "+0900"
        dtime = datetime.strptime(ldate, '%Y%m%d%H%M%S%z')        # datetimeオブジェクトを作成
        return dtime

    #-----------------------------------------
    @staticmethod
    def conv_utc(tstr):
        """
        JST -> UTC変換 (文字列)
        input str: "2015/08/01 5:00:00"
        """

        tloc = datetime.strptime(tstr, '%Y/%m/%d %H:%M:%S')

        ttime = time.mktime(tloc.timetuple())
        jst   = timezone(timedelta(hours=+9), 'JST')

        loc = datetime.fromtimestamp(ttime, jst)
        utc = datetime.fromtimestamp(loc.timestamp(), timezone.utc)

        tout = utc.strftime('%Y-%m-%dT%H:%M:%SZ')
        return tout

    #-----------------------------------------
    @staticmethod
    def dfinfo(df):
        """
        DataFrameの情報表示 (デバッグ用)
        """

        print("-"*10)
        print(type(df))

        # 各列の基礎統計量の確認 (平均、分散、4分位など)
        # Rでいうところのsummary()
        print(df.describe())

        # 行数の確認
        print(len(df))

        # 次元数の確認
        print(df.shape) #（行数、列数）の形で返す

        # カラム情報の一覧
        print(df.info()) #カラム名とその型の一覧

        # head / tail
        print(df.head(5)) #先頭5行を確認
        print(df.tail(5)) #先頭5行を確認

        #単純集計
        #for col in df:
        #    print(pd.value_counts(df[col]))
        #    print("\n")

    #-----------------------------------------
    @staticmethod
    def get_basename(infilename):
        """
        ファイルベース名取得
        """

        # ファイル名
        filename = os.path.basename(infilename)
        filebase = filename.split(".")
        basename = filebase[0]
        return basename

    #-----------------------------------------
    @staticmethod
    def write_json(filename, jsonData, indent=False):
        """
        JSONファイル書き込み
        """
        try:
            # Write the JSON(CZML) document to a file
            with codecs.open(filename, 'w', "utf-8") as f:
                if indent:
                    json.dump(jsonData, f, sort_keys=True, indent=4, ensure_ascii=False)
                    #json.dump(jsonData, f, indent=4, ensure_ascii=False)
                else:
                    json.dump(jsonData, f, ensure_ascii=False)

        except IOError as e:
            #sys.exit('system error: {}'.format(e))
            traceback.print_exc()
            raise Exception(str(e))

        return True

    #-----------------------------------------
    @staticmethod
    def read_json(filename):
        """
        JSONファイル読み込む
        """
        try:
            with codecs.open(filename, 'r', "utf-8") as f:
            #with open(filename) as f:
                #jsonData = json.loads(f.read(), "utf-8")
                jsonData = json.loads(f.read())

            #print(json.dumps(jsonData, sort_keys=True, indent = 4, ensure_ascii=False))

        except IOError as e:
            #sys.exit('system error: {}'.format(e))
            traceback.print_exc()
            raise Exception(str(e))

        return jsonData

    #-----------------------------------------
    @staticmethod
    def read_csv(filename):
        """
        CSVファイル読み込み
        """

        try:
          #with codecs.open(filename, "r", "cp932") as f:
          with codecs.open(filename, "r", "utf-8") as f:
                #rfp = csv.reader(f)
                rfp = csv.DictReader(f)

                csvdata = []
                for row in rfp:
                    row = dict(row)
                    csvdata.append(row)

                return csvdata

        except IOError as e:
            traceback.print_exc()
            raise Exception('system error: %s' % (e))

    #-----------------------------------------
    @staticmethod
    def write_csv(filename, plist):
        """
        CSVファイル書き込み
        """

        if os.path.exists(filename):
            os.remove(filename)

        try:
            # CSVファイル書き込み
            #with codecs.open(filename, 'w', "cp932") as f:
            with codecs.open(filename, 'w', "utf-8") as f:
                wfp = csv.writer(f, lineterminator='\n')  # 改行コード（\n）を指定しておく

                for ii, row in enumerate(plist):
                    wfp.writerow(row)       # 1次元配列書き込み
                    #writer.writerows(row)  # 2次元配列書き込み

                # f.close() # with文があるのでいらない

        except IOError as e:
            traceback.print_exc()
            raise Exception(str(e))
    #-----------------------------------------
    @staticmethod
    def read_dict_csv(filename):
        """
        辞書型CSVファイル読み込み
        """

        try:
          #with codecs.open(filename, "r", "cp932") as f:
          with codecs.open(filename, "r", "utf-8") as f:
                rfp = csv.DictReader(f)

                csvdata = []
                for row in rfp:
                    csvdata.append(row)

                return csvdata

        except IOError as e:
            traceback.print_exc()
            raise Exception('system error: %s' % (e))

    # ---------------------------
    @staticmethod
    def write_dict_csv(filename, plist):
        """
        辞書型CSVファイル書き込み
        """

        if os.path.exists(filename):
            os.remove(filename)

        try:
            header = plist[0].keys()  # ヘッダー用のデータを作っておく

            #with open(filename, "w") as f:
            with codecs.open(filename, 'w', "utf-8") as f:
                # headerを渡す
                writer = csv.DictWriter(f, header)

                # ヘッダー書き込み
                writer.writeheader()

                # データ書き込み
                for row in plist:
                    writer.writerow(row)

        except IOError as e:
            traceback.print_exc()
            raise Exception(str(e))

    #-----------------------------------------
    @staticmethod
    def generate_random_color():
        """
        16/256階調RGBカラーをランダムに出力
        @return RGB配列
        @see    https://www.lifewithpython.com/2015/03/generate-random-color-with-python.html
        """
        return '#{:X}{:X}{:X}'.format(*[random.randint(0, 255) for _ in range(3)])

    #-----------------------------------------
    @staticmethod
    def rgb2hex(color):
        """
        カラーコードの変換: RGB配列から16進数に変換
        @param  color RGB配列
        @return 16進数文字列
        """
        return '#%02X%02X%02X' % (color[0],color[1],color[2])

    #-----------------------------------------
    @staticmethod
    def hex2rgb(hex):
        """
        カラーコードの変換: 16進数からRGB配列に変換
        @param  hex 16進数文字列
        @return RGB配列
        """
        return [int(hex[1:3],16),int(hex[3:5],16),int(hex[5:7],16)]

    #-----------------------------------------
    @staticmethod
    def unzip(zip_filename):
        """
        unzip
        """
        try:
            with open(zip_filename, 'rb') as f:
                z = zipfile.ZipFile(f)
                for name in z.namelist():
                    #print("    Extracting file", name)
                    z.extract(name, "./")

        except IOError as e:
            traceback.print_exc()
            raise Exception(str(e))

    #-----------------------------------------
    @staticmethod
    def isEmpty(string):
        """
        文字列が空？
        """
        if string and string.strip():
            return False

        return True
