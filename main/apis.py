from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import ugettext as _

import tools.logs as logs
from tools.utils import utils
import traceback

import config.settings as settings

from datetime import datetime,timedelta

import os
import csv, json

import dashboard.apis.drm as drm
import dashboard.apis.romen as romen
import dashboard.apis.repair as repair
from dashboard.apis.drm import filledZero

# cost
import dashboard.apis.cost as cost
import dashboard.apis.evaluation as eva
import dashboard.apis.construction as construction

# work
import dashboard.apis.trajectory as trajectory
import dashboard.apis.damage as damage

import dashboard.apis.done as done
import dashboard.apis.recommend as recommend

# @see:
# * [Django REST framework: non-model serializer](https://stackoverflow.com/questions/13603027/django-rest-framework-non-model-serializer)
# * [Django REST framework ViewSet when you don’t have a Model](https://medium.com/django-rest-framework/django-rest-framework-viewset-when-you-don-t-have-a-model-335a0490ba6f)
#

#----------------------------------------------------------------
# calculation model table
#----------------------------------------------------------------

# -----------------------------------------
class calcEvaluationAPIView(APIView):
    """
    路線評価
    """
    def get(self, request, *args, **keywords):
        city_id  = filledZero(request.GET.get('city_id', "12100"))

        result = {}

        try:
            result = eva.setEvaluationData(city_id)
            response = Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            traceback.print_exc()
            response = Response(result, status=status.HTTP_404_NOT_FOUND)

        return response

# -----------------------------------------
class calcRepairAPIView(APIView):
    """
    維持修繕費用

    """
    def get(self, request, *args, **keywords):
        city_id = filledZero(request.GET.get('city_id', "12100"))

        result = {}

        try:
            result = repair.setRepairData(city_id)
            response = Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            traceback.print_exc()
            response = Response(result, status=status.HTTP_404_NOT_FOUND)

        return response


# -----------------------------------------
'''
class calcDrmAPIView(APIView):
    """
    DRM geojsonデータ作成
    """
    def get(self, request, *args, **keywords):

        result = {}
        try:
            city_id  = filledZero(request.GET.get('city_id', "12100"))  # city_id
            city_ids = request.GET.get('city_ids',"12101,12102,12103,12104,12105,12106") # city_id(行政区)カンマ区切り,, "12100, 12101..."
            city_ids = city_ids.split(",")

            result = drm.setDrmCityRoad(city_id, city_ids)
            response = Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            traceback.print_exc()
            response = Response(result, status=status.HTTP_404_NOT_FOUND)

        return response
'''

# -----------------------------------------
class calcRomenAPIView(APIView):
    """
    路面調査 geojsonデータ作成
    """
    def get(self, request, *args, **keywords):
        city_id = filledZero(request.GET.get('city_id', "12100"))

        result = {}

        try:
            result = romen.setRomenCityRoad(city_id)
            response = Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            traceback.print_exc()
            response = Response(result, status=status.HTTP_404_NOT_FOUND)

        return response


#----------------------------------------------------------------
# location
#----------------------------------------------------------------

# -----------------------------------------
'''
class locationCityAPIView(APIView):
    """
    座標値からリンクデータを取得（データ付き）
    """
    def get(self, request, *args, **keywords):
        city_id = filledZero(request.GET.get('city_id', "12100"))
        lat = float(request.GET.get('lat', "0.0"))   # latitude
        lon = float(request.GET.get('lon', "0.0"))  # longitude

        result = {}

        try:
            result = get_link_city_data(city_id, lon, lat)
            response = Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            traceback.print_exc()
            response = Response(result, status=status.HTTP_404_NOT_FOUND)

        return response
'''
# -----------------------------------------
'''
class locationAPIView(APIView):
    """
    座標値からリンクデータを取得
    """
    def get(self, request, *args, **keywords):
        lat = float(request.GET.get('lat', "0.0"))   # latitude
        lon = float(request.GET.get('lon', "0.0"))  # longitude

        result = {}

        try:
            result = get_link_data(lon, lat)
            response = Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            traceback.print_exc()
            response = Response(result, status=status.HTTP_404_NOT_FOUND)

        return response
'''

#----------------------------------------------------------------
# damage
#----------------------------------------------------------------

# ----------------------------------
class trajectoryApi(APIView):
    '''
    軌跡データ
    '''

    def get(self, request, *args, **keywords):
        try:
            date = request.GET.get('date', "")
            day  = int(request.GET.get('day', 1))

            if not utils.isEmpty(date):
                start = datetime.strptime(date,'%Y-%m-%d')  # datetimeオブジェクトを作成
                end   = start + timedelta(days=day)
            else:
                start = None
                end   = None

            result = trajectory.trajectory(request.user, start, end)
            response = Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            traceback.print_exc()
            logs.error('system error: '.format(e))
            result = {}
            response = Response(result, status=status.HTTP_404_NOT_FOUND)

        return response

# ----------------------------------
class damageApi(APIView):
    '''
    道路損傷データ
    '''

    def get(self, request, *args, **keywords):
        try:
            date = request.GET.get('date', None)
            day  = int(request.GET.get('day', 1))
            name = request.GET.get('name', None)

            if not utils.isEmpty(date):
                start = datetime.strptime(date,'%Y-%m-%d')  # datetimeオブジェクトを作成
                end   = start + timedelta(days=day)
            else:
                start = None
                end   = None

            result = damage.damage(request.user, start, end, name)
            response = Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            traceback.print_exc()
            logs.error('system error: '.format(e))
            result = {}
            response = Response(result, status=status.HTTP_404_NOT_FOUND)

        return response

# ----------------------------------
class damageDataApi(APIView):
    '''
    道路損傷データ(データ指定)
    '''

    def get(self, request, *args, **keywords):
        try:
            dataID = keywords['dataID']
            name = request.GET.get('name', None)

            result = damage.damageData(request.user, dataID, name)
            response = Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            traceback.print_exc()
            logs.error('system error: '.format(e))
            result = {}
            response = Response(result, status=status.HTTP_404_NOT_FOUND)

        return response

# ----------------------------------------------------------------
# damage date correction
# ----------------------------------------------------------------

# ----------------------------------
class setDamageDisableRequestApi(APIView):
    '''
    Annotationデータ(損傷データ無効)リクエスト
    '''

    def post(self, request, *args, **keywords):
        try:
            data = request.data

            data_status  = data["status"]
            data_dataID  = data["dataID"]
            #data_smartphoneID = data["smartphoneID"]
            #data_timestamp    = data["timestamp"]
            #data_location     = data["location"]

            result = damage.setDamagDisableRequest(request.user, data_dataID, data_status)
            response = Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            traceback.print_exc()
            logs.error('system error: '.format(e))
            result = {"status": 404}
            response = Response(result, status=status.HTTP_404_NOT_FOUND)

        return response




#----------------------------------------------------------------
# work: done/recommend
#----------------------------------------------------------------

# -----------------------------------------
class doneAPIView(APIView):
    """
    今日の対応済作業一覧
    """
    def get(self, request, *args, **keywords):
        city_id  = filledZero(request.GET.get('city_id', "12100"))

        result = {}

        try:
            result = done.done(city_id)
            response = Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            traceback.print_exc()
            response = Response(result, status=status.HTTP_404_NOT_FOUND)

        return response

# -----------------------------------------
class recommendAPIView(APIView):
    """
    明日の推奨作業
    """
    def get(self, request, *args, **keywords):
        city_id = filledZero(request.GET.get('city_id', "12100"))

        result = {}

        try:
            result = recommend.recommend(city_id)
            response = Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            traceback.print_exc()
            response = Response(result, status=status.HTTP_404_NOT_FOUND)

        return response


#----------------------------------------------------------------
# cost: cost/evaluation
#----------------------------------------------------------------

# -----------------------------------------
class evaluationAPIView(APIView):
    """
    路線評価
    """
    def get(self, request, *args, **keywords):
        city_id  = filledZero(request.GET.get('city_id', "12100"))
        table_id = request.GET.get('table_id', None)

        result = {}

        try:
            if table_id is None:
                result = eva.evaluation(city_id)
            else:
                table_id = int(table_id)
                result = eva.evaluation_one(city_id,table_id)

            response = Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            traceback.print_exc()
            response = Response(result, status=status.HTTP_404_NOT_FOUND)

        return response

# -----------------------------------------
class costAPIView(APIView):
    """
    維持修繕費用
    """
    def get(self, request, *args, **keywords):
        city_id = filledZero(request.GET.get('city_id', "12100"))

        result = {}

        try:
            result = cost.cost(city_id)
            response = Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            traceback.print_exc()
            response = Response(result, status=status.HTTP_404_NOT_FOUND)

        return response


# -----------------------------------------
class constructionAPIView(APIView):
    """
    舗装工事一覧
    """
    def get(self, request, *args, **keywords):
        city_id = filledZero(request.GET.get('city_id', "12100"))

        result = {}

        try:
            result = construction.construction(city_id)
            response = Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            traceback.print_exc()
            response = Response(result, status=status.HTTP_404_NOT_FOUND)

        return response


#----------------------------------------------------------------
# object detection
#----------------------------------------------------------------

# ----------------------------------
"""
class objectDetectionApi(APIView):
    '''
    物体検知(ディープラーニング)
    '''

    def get(self, request, *args, **keywords):
        try:
            task_id = 0
            threshold = 0.3

            username = get_username(request)
            input_path  = get_upload_path(username)
            output_path = get_download_path(username)

            od_eval_file = os.environ.get('OD_EVAL_FILE', settings.OD_EVAL_FILE)
            csvfile = os.path.join(output_path, od_eval_file)

            od_info = od.object_detection_main(task_id, username, threshold, input_path, output_path)
            od_info.to_csv(csvfile, index=False)

            result = {}
            response = Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            result = {}
            traceback.print_exc()
            logs.error('system error: '.format(e))
            response = Response(result, status=status.HTTP_404_NOT_FOUND)

        return response
"""

#----------------------------------------------------------------
# common
#----------------------------------------------------------------

#-----------------------------------
def getBoundaryGeojsonName(city_id):

    root_dir = settings.ROOT_DIR
    filename = "mlit_boundary_%s.geojson" % (city_id)
    pathname = os.path.join(root_dir.root, 'static', 'data', city_id, filename)

    return pathname

# ----------------------------------
class boundaryApi(APIView):
    """
    行政界
    """
    def get(self, request, *args, **keywords):
        city_id = filledZero(request.GET.get('city_id', "12100"))

        try:
            """
            cursor = connection.cursor()

            city_db = "city.mlit_boundary"

            text = "select ST_AsGeoJson(geom) from " + city_db
            cursor.execute(text)

            rows = cursor.fetchall()

            features = []
            for row in rows:
                encrow = json.loads(row[0])
                feature = {"type": "Feature", "properties": {"city_id": city_id}, "geometry": encrow }
                features.append(feature)

            geojson = {
                "type": "FeatureCollection",
                # "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
                "crs": {"type": "name", "properties": {"name": "EPSG:4326"}},
                "features": features
            }
            """
            pathname = getBoundaryGeojsonName(city_id)
            geojson  = utils.read_json(pathname)
            response = Response(geojson, status=status.HTTP_200_OK)

        except Exception as e:
            logs.error('system error: '.format(e))
            traceback.print_exc()
            response = Response({}, status=status.HTTP_404_NOT_FOUND)

        """
        finally:
            cursor.close()
        """

        return response

# ----------------------------------
class cityRoadApi(APIView):
    """
    路面調査道路データ
    """
    def get(self, request, *args, **keywords):
        city_id = filledZero(request.GET.get('city_id', "12100"))

        try:
            result = romen.getRomenCityRoad(city_id)
            response = Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            result = {}
            traceback.print_exc()
            logs.error('system error: '.format(e))
            response = Response(result, status=status.HTTP_404_NOT_FOUND)

        return response


# ----------------------------------
class drmCityRoadApi(APIView):
    '''
    DRM道路データ
    '''

    def get(self, request, *args, **keywords):
        try:
            city_id = filledZero(request.GET.get('city_id', "12100"))

            result = drm.getDrmCityRoad(city_id)
            response = Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            result = {}
            traceback.print_exc()
            logs.error('system error: '.format(e))
            response = Response(result, status=status.HTTP_404_NOT_FOUND)

        return response

#----------------------------------------------------------------
# Python/Django subroutine
#----------------------------------------------------------------

#---------------------------------------------
"""
def render_json_response(request, data, status=None):
    ''' 
    JSONレスポンス
    @param  request HTTPリクエストパラメータ
    @param  data    レスポンスデータ
    @param  data    レスポンスデータ
    @return HTTPレスポンス
    ''' 

    #json_str = json.dumps(data, ensure_ascii=False, indent=2)
    json_str = json.dumps(data, ensure_ascii=False)
    callback = request.GET.get('callback')
    if not callback:
        callback = request.POST.get('callback')  # POSTでJSONPの場合
    if callback:
        json_str = "%s(%s)" % (callback, json_str)
        response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8', status=status)
    else:
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)

    return response
"""

#----------------------------
"""
def handle_upload_file(input_path, f):
    '''
    handle_upload_file
    '''

    try:
        # ファイルフルパス名作成
        input_path = os.path.join(input_path, f.name)

        # ファイルが存在したら削除
        if os.path.exists(input_path):
            os.remove(input_path)

        # ファイル書き出し
        destination = open(input_path, 'wb+')

        for chunk in f.chunks():
            destination.write(chunk)

        destination.close()

    except Exception as e:
        traceback.print_exc()
        logs.error(str(e))
        raise Exception(str(e))
"""

#----------------------------
def get_username(request):
    '''
    ユーザ名取得
    '''

    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = settings.DEFAULT_IMAGE_USERNAME

    return username

def get_groups(request):
    '''
    グループ名取得
    '''

    glist = request.user.groups.values_list('name',flat=True)
    return list(glist)

#----------------------------
def get_upload_path(username):
    '''
    get_upload_path
    '''

    try:
        # 再帰的にディレクトリを作成
        input_path = os.path.join(settings.MEDIA_ROOT, username, settings.IMAGE_INPUT_PATH)
        if not os.path.exists(input_path):
            os.makedirs(input_path, exist_ok=True)

    except Exception as e:
        traceback.print_exc()
        logs.error(str(e))
        raise Exception(str(e))

    return input_path

#----------------------------
def get_download_path(username):
    '''
    get_download_path
    '''

    try:
        # ディレクトリ名を作成
        output_path = os.path.join(settings.MEDIA_ROOT, username, settings.IMAGE_OUTPUT_PATH)

        # ディレクトリが存在？
        if not os.path.exists(output_path):
            os.makedirs(output_path, exist_ok=True)

    except Exception as e:
        traceback.print_exc()
        logs.error(str(e))
        raise Exception(str(e))

    return output_path
