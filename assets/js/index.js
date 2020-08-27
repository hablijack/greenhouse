$(document).ready(function(){
    $("#light-link-area").mouseover(function(){
        var old_image = $("#greenhouse-display").attr("src");
        $("#greenhouse-display").data("old-image", old_image);
        $("#greenhouse-display").attr("src", "assets/img/greenhouse_light.png");
    });
    $("#light-link-area").mouseout(function(){
        var orig_image = $("#greenhouse-display").data("old-image");
        $("#greenhouse-display").attr("src", orig_image);
    });

    $("#water-link-area").mouseover(function(){
        var old_image = $("#greenhouse-display").attr("src");
        $("#greenhouse-display").data("old-image", old_image);
        $("#greenhouse-display").attr("src", "assets/img/greenhouse_water.png");
    });
    $("#water-link-area").mouseout(function(){
        var orig_image = $("#greenhouse-display").data("old-image");
        $("#greenhouse-display").attr("src", orig_image);
    });
});