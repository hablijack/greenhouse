
function getAirTemperaturesInside() {
    return $.ajax({
        url: "/history/air_temperature_inside",
    });
}

function getAirTemperaturesOutside() {
    return $.ajax({
        url: "/history/air_temperature_outside",
    });
}

function drawAirTemperatureChart(airInsideMetrics, airOutsideMetrics) {
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
                pointRadius: 3,
                fill: true,
                lineTension: 0,
                borderWidth: 0
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
                        unitStepSize: 1,
                        displayFormats: {
                            'minute': 'HH:MM:ss'
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

$(document).ready(function () {
    $.when(getAirTemperaturesInside(), getAirTemperaturesOutside()).done(function (air_inside, air_outside) {
        drawAirTemperatureChart(air_inside[0], air_outside[0])
    });
});