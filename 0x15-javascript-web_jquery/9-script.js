$(document).ready(function (){
    $.ajx({
        type: 'GET',
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        success: function (data) {
            $('DIV#hello').append(data.hello);
        }
    });
});