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
    console.log(rgb);
    return JSON.stringify(rgb)
}

function reloadImg() {
    var eyebrows = $('#eyebrows')[0];
    var eyebrows_hex = eyebrows.options[eyebrows.selectedIndex].value;
    var eyebrows_rgba = toRgba(hexToRgb(eyebrows_hex), getOpacity('eyebrows'));
    $("#bg").src("/video_feed?lips="+eyebrows_rgba)
}