$(function() {
    $('#id_descripcion').keydown(function(event) {
        if (event.keyCode == '13') {
            event.preventDefault();

            $.ajax({
                        type: "POST",
                        url: $("#form_tarea").attr('action'),
                        data: $("#form_tarea").serialize(),
                        dataType: "json",

                        success: function(data) {
                            $('#lista_tareas').prepend('<li>'
                                    + '<input type="checkbox" name="hecha" value="' + data.id + '" class="hecha-check"> '
                                    + '<span>' +$('#id_descripcion').val() + ' </span>'
                                    +'</li>');
                            $('#id_descripcion').val("");
                        }
                    });
        }
    });

    $('.hecha-check').change(function() {
        $.ajax({
                    type: "POST",
                    url: '/tarea/'+$(this).val()+'/hecha/'
                });


        if ($(this).is(':checked')) {
            $(this).next('span').addClass("tachado");
        } else {
            $(this).next('span').removeClass("tachado");
        }
    });
});