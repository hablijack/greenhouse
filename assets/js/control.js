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
        var identifier = $(this).attr('id')
        if ($(this).hasClass('active')) {
            switchRelay(identifier, false);
        } else {
            switchRelay(identifier, true);
        }
    });
});