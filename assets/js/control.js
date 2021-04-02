function switchRelay(identifier, state) {
    $.post("/control/relay", { identifier: identifier, state: state })
        .done(function (value) {
            if (state) {
                $('#' + identifier).addClass('active')
            } else {
                $('#' + identifier).removeClass('active')
            }
        });
}

$(document).ready(function () {
    $('#control-container button').click(function () {
        var current = $(this);
        if ($(this).hasClass('active')) {
            // ALREADY RUNNING --- SIMPLY SWITCH RELAY OFF
            switchRelay($(current).attr('id'), false);
        } else {
            // NOT RUNNING YET
            $('#control-container button').each(function (index) {
                if ($(this).attr('id') != $(current).attr('id')) {
                    // --- SWITCH OFF OTHER RELAYS
                    if ($(this).hasClass('active')) {
                        switchRelay($(this).attr('id'), false);
                    }
                } else {
                    // --- TURN THIS ON
                    switchRelay($(this).attr('id'), true);
                }
            });
        }
    });
});