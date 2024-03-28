$(document).ready(function() {
    $("#toggleButton").click(function() {
        toggleLanguage();
    });

    $("#switchButton").click(function() {
        switchLanguage();
    });

    
    //$("#GETButton").click(function(){

        //$.get("http://127.0.0.1:5000/getTest",function(data,status){
            //$("#parrafo-1").html(data);

        //});

    //})

    
    $("#GETButton").click(function(){
        $.get("http://127.0.0.1:5000/getTest", function(response){
            $("#GETButton").html(response);
        });
    });
    
});
