function hexToRgb(hex) {
    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
    } : null;
}

function getOpacity(key) {
    var options = {"eyebrows": 128, "lips": 128, "eyeliner": 110};
    return options[key]
}

function toRgba(rgb, opacity) {
    rgb["opacity"] = opacity;
    return rgb
}

function updateStyles() {
    var eyebrows = $('#eyebrows')[0];
    var eyebrows_hex = eyebrows.options[eyebrows.selectedIndex].value;
    var eyebrows_rgba = toRgba(hexToRgb(eyebrows_hex), getOpacity('eyebrows'));

    var eyeliner = $('#eyeliner')[0];
    var eyeliner_hex = eyeliner.options[eyeliner.selectedIndex].value;
    var eyeliner_rgba = toRgba(hexToRgb(eyeliner_hex), getOpacity('eyeliner'));

    var lips = $('#lips')[0];
    var lips_hex = lips.options[lips.selectedIndex].value;
    var lips_rgba = toRgba(hexToRgb(lips_hex), getOpacity('lips'));

    $.ajax({
        type: "POST",
        url: "/update_styles",
        dataType: 'json',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'eyebrows': eyebrows_rgba, 'eyeliner': eyeliner_rgba, 'lips': lips_rgba})
    }).done(function () {
    });
}