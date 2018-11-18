#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import environ

import config.settings as settings

import tools.logs as logs
import traceback

import pandas as pd
import numpy as np
import math

from django.core.management.base import BaseCommand, CommandError

import pprint
from tools.utils import utils
import traceback

from dashboard.apis.drm import setDrmCityRoad


#-----------------------------------
def main(city_id):
    """
    drmデータ設定

03205 岩手県  花巻市
13109 東京都  品川区
    """
    city_ids = [ city_id ]
    setDrmCityRoad(city_id, city_ids)

#-------------------------------------------
class Command(BaseCommand):
    """
    コマンド：drm_geojson
    """
    # python manage.py help count_entryで表示されるメッセージ
    help = 'make DRM geojson file from city_id'

    # コマンドライン引数を指定
    # see also: https://docs.python.org/3.6/library/argparse.html)
    def add_arguments(self, parser):
        # city_idという名前で取得する。（引数は最低でも1個, str型）
        parser.add_argument('city_id', nargs='+', type=str)

    # コマンドが実行された際に呼ばれるメソッド
    def handle(self, *args, **options):
        start = time.time()

        try:
            if not "city_id" in options:
                raise Exception('city_id not found')

            for city_id in options['city_id']:  # option はリスト
                print("city_id=%s" % (city_id))
                main(city_id)

            print("\ndone\n")

        except Exception as e:
            traceback.print_exc()
            print("Unexpected error:", sys.exc_info()[0])

        elapsed_time = time.time() - start
        print("elapsed_time: %d" % (elapsed_time) + "[sec]")

#-------------------------------------------
if __name__ == "__main__":
    """
    main()
    """
    argv = sys.argv   # コマンドライン引数を格納したリストの取得
    argc = len(argv)  # 引数の個数

