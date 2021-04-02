
function getTimefilter(filter) {
    return $('#' + filter + '_timefilter').val();
}
function drawAirTemperatureChart(airInsideMetrics, airOutsideMetrics) {
    filter = getTimefilter('temperature')
    var ctx = document.getElementById('air-temperature').getContext('2d');
    ctx.canvas.width = 1000;
    ctx.canvas.height = 300;

    var color = Chart.helpers.color;
    var cfg = {
        data: {
            datasets: [{
                label: 'Innen',
                backgroundColor: color('blue').alpha(0.5).rgbString(),
                borderColor: 'blue',
                data: airInsideMetrics,
                type: 'line',
                pointRadius: 1,
                fill: false,
                lineTension: 0,
                borderWidth: 3
            },
            {
                label: 'Außen',
                backgroundColor: color('darkblue').alpha(0.5).rgbString(),
                borderColor: 'darkblue',
                data: airOutsideMetrics,
                type: 'line',
                pointRadius: 1,
                fill: false,
                lineTension: 0,
                borderWidth: 3
            }]
        },
        options: {
            animation: {
                duration: 2000
            },
            scales: {
                xAxes: [{
                    type: 'time',
                    distribution: 'series',
                    offset: true,
                    time: {
                        parser: 'YYYY-MM-DDTHH:mm:ssZ',
                        unit: 'minute',
                        displayFormats: {
                            'minute': ((filter === 'today') ? 'HH:mm' : 'D.M HH:mm')
                        }
                    },
                    ticks: {
                        major: {
                            enabled: true,
                            fontStyle: 'bold'
                        },
                        source: 'data',
                        autoSkip: true,
                        autoSkipPadding: 75,
                        maxRotation: 0,
                        sampleSize: 100
                    },
                }],
                yAxes: [{
                    gridLines: {
                        drawBorder: true
                    },
                    scaleLabel: {
                        display: true,
                        labelString: '°C'
                    }
                }]
            },
        }
    };
    var chart = new Chart(ctx, cfg);
}

function drawHumidityChart(humidityMetrics) {
    filter = getTimefilter('humidity')
    var ctx = document.getElementById('humidity').getContext('2d');
    ctx.canvas.width = 1000;
    ctx.canvas.height = 300;
    var color = Chart.helpers.color;
    var cfg = {
        data: {
            datasets: [{
                label: 'Luftfeuchtigkeit',
                backgroundColor: color('aqua').alpha(0.5).rgbString(),
                borderColor: 'aqua',
                data: humidityMetrics,
                type: 'line',
                pointRadius: 1,
                fill: false,
                lineTension: 0,
                borderWidth: 3
            }]
        },
        options: {
            animation: {
                duration: 2000
            },
            scales: {
                xAxes: [{
                    type: 'time',
                    distribution: 'series',
                    offset: true,
                    time: {
                        parser: 'YYYY-MM-DDTHH:mm:ssZ',
                        unit: 'minute',
                        displayFormats: {
                            'minute': ((filter === 'today') ? 'HH:mm' : 'D.M HH:mm')
                        }
                    },
                    ticks: {
                        major: {
                            enabled: true,
                            fontStyle: 'bold'
                        },
                        source: 'data',
                        autoSkip: true,
                        autoSkipPadding: 75,
                        maxRotation: 0,
                        sampleSize: 100
                    },
                }],
                yAxes: [{
                    gridLines: {
                        drawBorder: true
                    },
                    scaleLabel: {
                        display: true,
                        labelString: '%'
                    },
                    ticks: {
                        suggestedMin: 0,
                        min: 0,
                        max: 100,
                        stepsize: 10
                    }
                }]
            },
        }
    };
    var chart = new Chart(ctx, cfg);
}

function drawWiFiChart(wifiMetrics) {
    filter = getTimefilter('wifi')
    var ctx = document.getElementById('wifi-strength').getContext('2d');
    ctx.canvas.width = 1000;
    ctx.canvas.height = 300;
    var color = Chart.helpers.color;
    var cfg = {
        data: {
            datasets: [{
                label: 'Signalstärke',
                backgroundColor: color('orange').alpha(0.5).rgbString(),
                borderColor: 'orange',
                data: wifiMetrics,
                type: 'line',
                pointRadius: 1,
                fill: false,
                lineTension: 0,
                borderWidth: 3
            }]
        },
        options: {
            animation: {
                duration: 2000
            },
            scales: {
                xAxes: [{
                    type: 'time',
                    distribution: 'series',
                    offset: true,
                    time: {
                        parser: 'YYYY-MM-DDTHH:mm:ssZ',
                        unit: 'minute',
                        displayFormats: {
                            'minute': ((filter === 'today') ? 'HH:mm' : 'D.M HH:mm')
                        }
                    },
                    ticks: {
                        major: {
                            enabled: true,
                            fontStyle: 'bold'
                        },
                        source: 'data',
                        autoSkip: true,
                        autoSkipPadding: 75,
                        maxRotation: 0,
                        sampleSize: 100
                    },
                }],
                yAxes: [{
                    gridLines: {
                        drawBorder: true
                    },
                    scaleLabel: {
                        display: true,
                        labelString: '%'
                    },
                    ticks: {
                        suggestedMin: 20,
                        min: 30,
                        max: 60,
                        stepsize: 10
                    }
                }]
            },
        }
    };
    var chart = new Chart(ctx, cfg);
}


function drawCo2Chart(co2Metrics) {
    filter = getTimefilter('co2')
    var ctx = document.getElementById('co2-history').getContext('2d');
    ctx.canvas.width = 1000;
    ctx.canvas.height = 300;
    var color = Chart.helpers.color;
    var cfg = {
        data: {
            datasets: [{
                label: 'PPM',
                backgroundColor: color('red').alpha(0.5).rgbString(),
                borderColor: 'red',
                data: co2Metrics,
                type: 'line',
                pointRadius: 1,
                fill: false,
                lineTension: 0,
                borderWidth: 3
            }]
        },
        options: {
            animation: {
                duration: 2000
            },
            scales: {
                xAxes: [{
                    type: 'time',
                    distribution: 'series',
                    offset: true,
                    time: {
                        parser: 'YYYY-MM-DDTHH:mm:ssZ',
                        unit: 'minute',
                        displayFormats: {
                            'minute': ((filter === 'today') ? 'HH:mm' : 'D.M HH:mm')
                        }
                    },
                    ticks: {
                        major: {
                            enabled: true,
                            fontStyle: 'bold'
                        },
                        source: 'data',
                        autoSkip: true,
                        autoSkipPadding: 75,
                        maxRotation: 0,
                        sampleSize: 100
                    },
                }],
                yAxes: [{
                    gridLines: {
                        drawBorder: true
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'ppm'
                    }
                }]
            },
        }
    };
    var chart = new Chart(ctx, cfg);
}


function drawBrightnessChart(brightnessMetrics) {
    filter = getTimefilter('brightness')
    var ctx = document.getElementById('brightness-history').getContext('2d');
    ctx.canvas.width = 1000;
    ctx.canvas.height = 300;
    var color = Chart.helpers.color;
    var cfg = {
        data: {
            datasets: [{
                label: 'PPM',
                backgroundColor: color('purple').alpha(0.5).rgbString(),
                borderColor: 'purple',
                data: brightnessMetrics,
                type: 'line',
                pointRadius: 1,
                fill: false,
                lineTension: 0,
                borderWidth: 3
            }]
        },
        options: {
            animation: {
                duration: 2000
            },
            scales: {
                xAxes: [{
                    type: 'time',
                    distribution: 'series',
                    offset: true,
                    time: {
                        parser: 'YYYY-MM-DDTHH:mm:ssZ',
                        unit: 'minute',
                        displayFormats: {
                            'minute': ((filter === 'today') ? 'HH:mm' : 'D.M HH:mm')
                        }
                    },
                    ticks: {
                        major: {
                            enabled: true,
                            fontStyle: 'bold'
                        },
                        source: 'data',
                        autoSkip: true,
                        autoSkipPadding: 75,
                        maxRotation: 0,
                        sampleSize: 100
                    },
                }],
                yAxes: [{
                    gridLines: {
                        drawBorder: true
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'ppm'
                    }
                }]
            },
        }
    };
    var chart = new Chart(ctx, cfg);
}

function drawBatteryChart(batteryMetrics) {
    filter = getTimefilter('battery')
    var ctx = document.getElementById('battery-capacity').getContext('2d');
    ctx.canvas.width = 1000;
    ctx.canvas.height = 300;
    var color = Chart.helpers.color;
    var cfg = {
        data: {
            datasets: [{
                label: 'Ladezustand',
                backgroundColor: color('green').alpha(0.5).rgbString(),
                borderColor: 'green',
                data: batteryMetrics,
                type: 'line',
                pointRadius: 1,
                fill: false,
                lineTension: 0,
                borderWidth: 3
            }]
        },
        options: {
            animation: {
                duration: 2000
            },
            scales: {
                xAxes: [{
                    type: 'time',
                    distribution: 'series',
                    offset: true,
                    time: {
                        parser: 'YYYY-MM-DDTHH:mm:ssZ',
                        unit: 'minute',
                        displayFormats: {
                            'minute': ((filter === 'today') ? 'HH:mm' : 'D.M HH:mm')
                        }
                    },
                    ticks: {
                        major: {
                            enabled: true,
                            fontStyle: 'bold'
                        },
                        source: 'data',
                        autoSkip: true,
                        autoSkipPadding: 75,
                        maxRotation: 0,
                        sampleSize: 100
                    },
                }],
                yAxes: [{
                    gridLines: {
                        drawBorder: true
                    },
                    scaleLabel: {
                        display: true,
                        labelString: '%'
                    },
                    ticks: {
                        suggestedMin: 0,
                        min: 0,
                        max: 100,
                        stepsize: 10
                    }
                }]
            },
        }
    };
    var chart = new Chart(ctx, cfg);
}


function getAirTemperaturesInside() {
    var filter = getTimefilter('temperature')
    return $.ajax({
        url: "/history/air_temperature_inside?timefilter=" + filter
    });
}

function getAirTemperaturesOutside() {
    var filter = getTimefilter('temperature')
    return $.ajax({
        url: "/history/air_temperature_outside?timefilter=" + filter
    });
}
function get_temperatures() {
    $.when(getAirTemperaturesInside(), getAirTemperaturesOutside()).done(function (air_inside, air_outside) {
        drawAirTemperatureChart(air_inside[0], air_outside[0]);
    });
}

function get_wifi() {
    var filter = getTimefilter('wifi')
    $.ajax({
        url: "/history/wifi_strength?timefilter=" + filter
    }).done(function (value) {
        drawWiFiChart(value);
    });
}

function get_battery() {
    var filter = getTimefilter('battery')
    $.ajax({
        url: "/history/battery_capacity?timefilter=" + filter
    }).done(function (value) {
        drawBatteryChart(value);
    });
}

function get_co2() {
    var filter = getTimefilter('co2')
    $.ajax({
        url: "/history/co2?timefilter=" + filter
    }).done(function (value) {
        drawCo2Chart(value);
    });
}

function get_humidity() {
    var filter = getTimefilter('humidity')
    $.ajax({
        url: "/history/humidity?timefilter=" + filter
    }).done(function (value) {
        drawHumidityChart(value);
    });
}

function get_brightness() {
    var filter = getTimefilter('brightness')
    $.ajax({
        url: "/history/brightness?timefilter=" + filter
    }).done(function (value) {
        drawBrightnessChart(value);
    });
}

$(document).ready(function () {
    get_temperatures();
    get_wifi();
    get_battery();
    get_co2();
    get_brightness();
    get_humidity();
    $('#temperature_timefilter').change(function () {
        get_temperatures();
    });
    $('#wifi_timefilter').change(function () {
        get_wifi();
    });
    $('#battery_timefilter').change(function () {
        get_battery();
    });
    $('#co2_timefilter').change(function () {
        get_co2();
    });
    $('#brightness_timefilter').change(function () {
        get_brightness();
    });
    $('#humidity_timefilter').change(function () {
        get_humidity();
    });
});