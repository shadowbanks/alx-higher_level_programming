$(document).ready(function (){
    $("input#btn_translate").on("click", function(){
        let value = $("input#language_code").val();
        const url = "https://hellosalut.stefanbohacek.dev/?lang=" + value;
        $.get(url, function(data, res)
        {
            $("DIV#hello").text(data.hello);
        });
    });
});