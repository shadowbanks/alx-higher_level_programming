$(document).ready(function (){
    $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data, statusCode)
    {
        $("Div#hello").text(data.hello);
    });
});