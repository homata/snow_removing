/**
 * 初期処理 (コンテンツダウンロード完了後)
 */
window.addEventListener("load",function(e){

},false);


function onButtonClick() {
  /*
  let filters = [];

  let filterService = document.querySelector('#service').value;
  if (filterService.startsWith('0x')) {
    filterService = parseInt(filterService);
  }
  if (filterService) {
    filters.push({services: [filterService]});
  }

  let filterName = document.querySelector('#name').value;
  if (filterName) {
    filters.push({name: filterName});
  }

  let filterNamePrefix = document.querySelector('#namePrefix').value;
  if (filterNamePrefix) {
    filters.push({namePrefix: filterNamePrefix});
  }

  let options = {};
  if (document.querySelector('#allDevices').checked) {
    options.acceptAllDevices = true;
  } else {
    options.filters = filters;
  }
  */

  /*
   > Name:             LINEBeacon
   > Id:               Q+u7gjWCstuq26rWph/1cQ==
   > Connected:        false
  */
  let options = {};
  options.acceptAllDevices = true;

  console.log('Requesting Bluetooth Device...');
  console.log('with ' + JSON.stringify(options));

  navigator.bluetooth.requestDevice(options)
  .then(device => {
    console.log('> Name:             ' + device.name);
    console.log('> Id:               ' + device.id);
    console.log('> Connected:        ' + device.gatt.connected);

    //device.gatt.connect();

    chart_draw();
    update();
    setTimeout("update()", 1000);
    //setInterval("dispDate()",1000);
  })
  .catch(error => {
    console.log('Argh! ' + error);
  });

}


/**
 *
 **/
function update() {

  var val_bpm;   // parseInt($("#score_bpm").text());
  var val_body;  // parseFloat($("#score_body").text());
  var va_mining; // parseInt($("#score_mining").text());

  var min = 60;
  var max = 120 ;
  val_bpm   = Math.floor( Math.random() * (max + 1 - min) ) + min;

  min = 35.5;
  max = 36.0;
  val_body  = sprintf("%.1f", Math.random() * (max + 1 - min) + min);

  va_mining += 1;

  $("#score_bpm").text(val_bpm);
  $("#score_body").text(val_body);
  $("#score_mining").text(va_mining);

  setTimeout("update()", 1000);
}


