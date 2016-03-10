$( document ).ready(function() { 
    var frm = $('#search_input');
    $('.dl_food').change(function () {
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            success: function (data) {
                $(".resultado").html(data);
            },
            error: function(data) {
                $(".resultado").html("Something went wrong!");
            }
        });
        return false;
    });

    contenido = $("#id_food_all").html();
    $(".datalist-content").html('<datalist id=\"id_food_all\">' + contenido + '</datalist>');
});