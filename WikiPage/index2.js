$(document).ready(function() {
    $("#toggleButton").click(function() {
        toggleLanguage();
    });

    $("#switchButton").click(function() {
        switchLanguage();
    });


    $("#GETButton").click(function(){
        $.get("http://127.0.0.1:5000/getTest", function(){
            var newText = switchLanguage2(); // Call switchLanguage2 to get the new text
            $("#p1").text(newText);
        });
    });
});
