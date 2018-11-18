/**
 * 初期処理 (コンテンツダウンロード完了後)
 */
window.addEventListener("load",function(e){
    map_draw();
    chart_draw();
    vector_map_draw();
    pie_chart_draw();
    radar_draw();
    calendar_draw();
},false);

$(function(){
});

/* for onsen ui */
document.addEventListener('prechange', function(event) {
  document.querySelector('ons-toolbar .center')
    .innerHTML = event.tabItem.getAttribute('label');
});

/* global value */
var map = null;          /* マップ */
var layerControl = null; /* コントロール */
var snowMarker = null; /* コントロール */

/**--------------------------------------
 * map_draw
 ----------------------------------------*/
function map_draw() {
    // マップ作成
    map = L.map('map');

    // 地理院地図 淡色地図
    /*
    L.tileLayer(
        'https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png',
        {
            id: 'palemap',
            attribution: "<a href='http://portal.cyberjapan.jp/help/termsofuse.html' target='_blank'>国土地理院</a>"
        }
    ).addTo(map);
    */

    // OSM タイル設定
    /*
    L.tileLayer(
        'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        {
            attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
            maxZoom: 18
        }
    ).addTo(map);
    */

    // Other
    /**/
    L.tileLayer(
        //'https://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png',
        //"https://cartodb-basemaps-{s}.global.ssl.fastly.net/dark_all/{z}/{x}/{y}.png",
        //"http://a.tile.stamen.com/toner/${z}/${x}/${y}.png",
        "http://tile.stamen.com/toner/{z}/{x}/{y}.png",
        {
            attribution: 'Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL',
            maxZoom: 18
        }
    ).addTo(map);
    /**/

    // 設定パラメータ取得
    var lon  = 142.463333;
    var lat  = 44.355833;
    var zoom = 14;

    // ビュー設定
    map.setView([lat,lon], zoom);

    // コントロールはオープンにする
    layerControl = L.control.layers(null, null, {collapsed: false}).addTo(map);
    //layerControl = L.control.layers().addTo(map);

    //スケールコントロールを追加（オプションはフィート単位を非表示）
    L.control.scale({imperial: false}).addTo(map);

    /* クリックしたい緯度経度を表示 */
    /**/
    map.on('click', function(e) {
        var latitude = (Math.round(e.latlng.lat * 10000)) /10000;
        var longitude = (Math.round(e.latlng.lng * 10000)) /10000;
        //alert("緯度(latitude):" + latitude + " , " + "経度(latitude):" + latitude);
        //console.log("緯度(latitude):" + latitude + " , " + "経度(longitude):" + longitude);
        console.log("[ " + latitude + ", "  + longitude + "],");
    });
    /**/
    var sampleIcon = L.icon({
        iconUrl: '/static/images/snow.png',   // https://www.monopot-illust.com/illust/503
        iconRetinaUrl: '/static/images/snow.png',
        iconSize: [50, 50],
        iconAnchor: [25, 50],
        popupAnchor: [0, -50],
    });

    var points = [
        [ 44.3546, 142.4625],
        [ 44.3585, 142.4596],
        [ 44.361, 142.4601],
        [ 44.3628, 142.4559],
        [ 44.3634, 142.4543],
        [ 44.3572, 142.4548],
        [ 44.3517, 142.4554],
        [ 44.3431, 142.4628],
        [ 44.3439, 142.4691],
        [ 44.35,   142.4704],
        [ 44.3568, 142.4672],
        [ 44.3643, 142.4656],
        [ 44.3577, 142.4523],
        [ 44.3506, 142.4511],
        [ 44.3495, 142.4466],
        [ 44.3479, 142.4682],
    ];

    var markers = L.markerClusterGroup();
    var length = points.length;
    for (var ii=0; ii<length; ii++) {
        var lon = points[ii][1];
        var lat = points[ii][0];
        var dataID = ii;

        var marker = L.marker(new L.LatLng(lat, lon), { title: dataID,icon: sampleIcon });
        marker.bindPopup("雪降ろしポータル: ハック " + dataID + "");
        markers.addLayer(marker);
    }

    if (length > 0) {
        map.addLayer(markers);
        layerControl.addOverlay(markers, "雪降ろしポータル");

        snowMarker = markers;
    }
    /**/
}

/**--------------------------------------
 * リアルタイムグラフ
 *  https://nagix.github.io/chartjs-plugin-streaming/samples/line-horizontal.html
 * Chart.js (日本語)
 *  https://misc.0o0o.org/chartjs-doc-ja/
 ----------------------------------------*/
var chartColors = {
	red: 'rgb(255, 99, 132)',
	orange: 'rgb(255, 159, 64)',
	yellow: 'rgb(255, 205, 86)',
	green: 'rgb(75, 192, 192)',
	blue: 'rgb(54, 162, 235)',
	purple: 'rgb(153, 102, 255)',
	grey: 'rgb(201, 203, 207)'
};
var color = Chart.helpers.color;

/**
 * chart()
 */
function chart_draw() {
    /* チャート定義 */
    var config = {
        type: 'line',
        data: {
            datasets: [{
                label: "現在の心拍",
    			backgroundColor: color(chartColors.blue).alpha(0.5).rgbString(),
	    		borderColor: chartColors.blue,
                fill: false,
                cubicInterpolationMode: 'monotone',
                data: []
            }]
        },
        options: {
            legend: {
              display: false    // hide dataset labels
            },
            title: {
                display: false,
                text: 'あなたの心拍波形'
            },
            scales: {
                xAxes: [{
                    type: 'realtime',
                    realtime: {
                        duration: 20000,
                        refresh: 1000,
                        delay: 2000,
                        onRefresh: onRefresh
                    }
                }],
                yAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: 'value'
                    }
                }]
            },
            tooltips: {
                mode: 'nearest',
                intersect: false,
                callbacks: {
                    label: function(tooltipItem) {
                        return tooltipItem.yLabel;
                    }
                }
            },
            hover: {
                mode: 'nearest',
                intersect: false
            }
        }
    };

	var ctx = document.getElementById('myChart').getContext('2d');
	window.myChart = new Chart(ctx, config);
}

/* ランダム */
function randomScalingFactor() {
	return (Math.random() > 0.5 ? 1.0 : -1.0) * Math.round(Math.random() * 100);
}

/* リフレッシュ */
function onRefresh(chart) {
	chart.config.data.datasets.forEach(function(dataset) {
		dataset.data.push({
			x: Date.now(),
			y: randomScalingFactor()
		});
	});
}

/**--------------------------------------
 * jVector Maps
 *  http://jvectormap.com/
 * jVectorMap - fast and easy plugin to display vector maps of the world
 *  http://plugindetector.com/jvector-map
 * コピペで(ほぼ)一発！jQueryでオシャレな地図ツールを作ったよ。
 *  http://www.procrasist.com/entry/map-tool
 *  https://github.com/hokekiyoo/map_maker
 ----------------------------------------*/

/**
 * jVector Maps
 * vector_map_draw()
 */
function vector_map_draw() {
    var map2 = new jvm.Map({
        container: $('#my-map-markers'),
        map: 'jp_merc',                     // マップデータ
        normalizeFunction: 'polynomial',
        hoverOpacity     : 0.7,
        hoverColor       : false,
        backgroundColor  : 'transparent',
        regionStyle      : {
          initial      : {
            fill            : 'rgba(210, 214, 222, 1)',
            'fill-opacity'  : 1,
            stroke          : 'none',
            'stroke-width'  : 0,
            'stroke-opacity': 1
          },
          hover        : {
            'fill-opacity': 0.7,
            cursor        : 'pointer'
          },
          selected     : {
            fill: 'yellow'
          },
          selectedHover: {}
        },
        markerStyle      : {
          initial: {
            fill  : '#00a65a',
            stroke: '#111'
          }
        },
        markers : [
          { latLng: [44.355833, 142.463333], name: "名寄", },
          { latLng: [43.062083,141.354389], name: "札幌", },
          { latLng: [43.770639,142.365], name: "旭川", },
          { latLng: [35.689556,139.691722], name: "東京", },
          { latLng: [35, 135], name: "京都", },
          { latLng: [35, 140], name: "茨城", },
          { latLng: [36.16, 136.5], name: "岐阜", },
          //{ latLng: [24.2, 123.5], name: "沖縄", },
        ]
    });
}

/**--------------------------------------
 * pie_chart_draw
 ----------------------------------------*/

/**
 * pie_chart_draw()
 */
function pie_chart_draw() {

    var ctx = document.getElementById("pieChart").getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ["-20℃", "-15℃", "-10℃", "-5℃", "0℃", "5℃", "10℃"],
        datasets: [{
          backgroundColor: [
            "#2ecc71",
            "#3498db",
            "#95a5a6",
            "#9b59b6",
            "#f1c40f",
            "#e74c3c",
            "#34495e"
          ],
          data: [12, 19, 3, 17, 28, 24, 7]
        }]
      }
    });
}

/**--------------------------------------
 * radar_draw
 ----------------------------------------*/

/**
 * radar_draw()
 */
function radar_draw() {
    var ctx = document.getElementById("myRadarChart");
    var myChart = new Chart(ctx, {
      type: 'radar',
      data: {
        labels: ["M", "T", "W", "T", "F", "S", "S"],
        datasets: [{
          label: '2月',
          backgroundColor: "rgba(153,255,51,0.4)",
          borderColor: "rgba(153,255,51,1)",
          data: [12, 19, 3, 17, 28, 24, 7]
        }, {
          label: '1月',
          backgroundColor: "rgba(255,153,0,0.4)",
          borderColor: "rgba(255,153,0,1)",
          data: [30, 29, 5, 5, 20, 3, 10]
        }]
      }
    });
}

/**--------------------------------------
 * calender
 ----------------------------------------*/

/**
 * calendar_draw()
 */
function calendar_draw() {
    $( "#calendar" ).datepicker({
        language: "ja",
        todayHighlight : true,
    });
}
