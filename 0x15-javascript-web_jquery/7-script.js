$(document).ready(function (){
    $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data, response)
    {
        const name = data.name;
        $("#character").text(name);
    });
});