$(document).ready(function (){
    $("input#btn_translate").on("click", greet);

    $("input#language_code").on("keydown", function(event) {
        if (event.which === 13){
            greet();
        }
    });
    
    function greet(){
        let value = $("input#language_code").val();
        const url = "https://hellosalut.stefanbohacek.dev/?lang=" + value;
        $.get(url, function(data, res)
        {
            $("DIV#hello").text(data.hello);
        });
    };
});