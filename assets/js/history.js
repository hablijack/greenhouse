
function getAirTemperatureTimefilter() {
    return $('#temperature_timefilter').val();
}

function getWiFiTimefilter() {
    return $('#wifi_timefilter').val();
}

function drawAirTemperatureChart(airInsideMetrics, airOutsideMetrics) {
    filter = getAirTemperatureTimefilter()
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

function drawWiFiChart(wifiMetrics) {
    filter = getWiFiTimefilter()
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
                    }
                }]
            },
        }
    };
    var chart = new Chart(ctx, cfg);
}


function getAirTemperaturesInside() {
    var filter = getAirTemperatureTimefilter()
    return $.ajax({
        url: "/history/air_temperature_inside?timefilter=" + filter
    });
}

function getAirTemperaturesOutside() {
    var filter = getAirTemperatureTimefilter()
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
    var filter = getWiFiTimefilter()
    $.ajax({
        url: "/history/wifi_strength?timefilter=" + filter
    }).done(function (value) {
        drawWiFiChart(value);
    });
}

$(document).ready(function () {
    get_temperatures();
    get_wifi();
    $('#temperature_timefilter').change(function () {
        get_temperatures();
    });
    $('#wifi_timefilter').change(function () {
        get_wifi();
    });
});