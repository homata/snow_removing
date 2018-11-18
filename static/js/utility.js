/**
 * 数値チェック関数
 * 入力値が数値 (符号あり小数 (- のみ許容)) であることをチェックする
 * [引数]   numVal: 入力値
 * [返却値] true:  数値
 *          false: 数値以外
 * Note: http://jquery.nj-clucker.com/number-check-function/
 */
function isNumber(numVal) {
    
    if (isNaN(numVal)) {
        return false;
    }

    // チェック条件パターン
    var pattern = /^[-]?([1-9]\d*|0)(\.\d+)?$/;
    // 数値チェック
    return pattern.test(numVal);
}

/**
 * ブラウザーの種類を取得
 * @returns {*}
 */
function getBrowser() {

    var userAgent = window.navigator.userAgent.toLowerCase();

    if (userAgent.indexOf('opera') != -1) {
        return 'opera';
    } else if (userAgent.indexOf('msie') != -1) {
        return 'ie';
    } else if (userAgent.indexOf('chrome') != -1) {
        return 'chrome';
    } else if (userAgent.indexOf('safari') != -1) {
        return 'safari';
    } else if (userAgent.indexOf('gecko') != -1) {
        return 'gecko';
    } else {
    return false;
    }
}

/**
 * 空文字チェック
 **/
function isEmpty(val){
    return !val ?
        !(val===0 || val===false)? true : false
        :false;
}
/**
 * Json -> CSV変換
 * @param json
 * @returns {string}
 */
function json2csv(json) {
    var header = Object.keys(json[0]).join(',') + "\r\n";

    var body = json.map(function(d){
        return Object.keys(d).map(function(key) {
            return d[key];
        }).join(',');
    }).join("\r\n");

    return header + body;
}

/**
 * メッセージダイアログ
 * @param message
 */
function msgDialog(message) {
    var title = "Message";

    // ダイアログのメッセージとタイトルを設定
    $( "#msg_dialog" ).html(message);

    // ダイアログを作成
    $( "#msg_dialog" ).dialog({
        modal: true,
        title: title,
        buttons: {
            "OK": function() {
                $(this).dialog("close");
            }
        }
    });
}

/**
 * エラーダイアログ
 * @param message
 */
function errDialog(message) {
    var title = "Error";

    // ダイアログのメッセージとタイトルを設定
    $( "#msg_dialog" ).html(message);

    // ダイアログを作成
    $( "#msg_dialog" ).dialog({
        modal: true,
        title: title,
        buttons: {
            "OK": function() {
                $(this).dialog("close");
            }
        }
    });
}

/**
 * ファイル名分割
 * @param fullname
 **/
function getFileSplit(fullname) {
    var pattern = /(.*)(?:\.([^.]+$))/;
    var list    = fullname.match(pattern);

    var filename = list[0];
    var basename = list[1];
    var ext      = list[2];
    return [filename, basename, ext];
}
