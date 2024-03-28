$(document).ready(function() {
    $("#toggleButton").click(function() {
        toggleLanguage();
    });

    $("#switchButton").click(function() {
        switchLanguage();
    });

    $("#GETButton").click(function(){
        $.get("http://127.0.0.1:5000/getTest", function(response){
            $("#GETButton").html(response);
        });
    });
    
    $("#POSTButton").click(function() {
        var favoriteCharacter = $("input[name='favorite_character']:checked").val();
        
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5000/postTest",
            contentType: 'application/json',
            data: JSON.stringify({
                'favorite_character': favoriteCharacter
            }),
            success: function(response) {
                alert('Your favorite character is: ' + response.message);
            },
            error: function(xhr, status, error) {
                alert("Error: " + xhr.responseText);
            }
        });
    
        return false;
    });
});
