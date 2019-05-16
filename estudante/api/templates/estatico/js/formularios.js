function listarHistoricoEstudante(matricula){
    if (matricula == ""){
        $('#resultado').html("Informe a matrícula do estudante").animate();
    }else{
        $.ajaxSetup({
            headers:{
            "X-CSRFToken": $('[name="csrfmiddlewaretoken"]').val()
        }
        });
        $.ajax({
            type: "POST",
            crossDomain: false,
            data: {
                'matricula':matricula
            },
            dataType: "JSON",
            url: $('[name="urlHistorico"]').val(),
            success: function (response) {   
                $('#resultadoModal').removeClass();
                $('#NomeEstudanteModal').html(response['nomeEstudante']).animate();
                $('#listaHistorico').html(response['conteudo']).animate();
            },
            error : function(jqXHR, textStatus, errorThrown){
                console.log(errorThrown);
            }
        });
    }
}

function buscarLivro(codigo){
    if (codigo == ""){
        $('#resultado').html("").animate();
    }else{
        $.ajaxSetup({
            headers:{
            "X-CSRFToken": $('[name="csrfmiddlewaretoken"]').val()
        }
        });
        $.ajax({
            type: "POST",
            crossDomain: false,
            data: {
                'codigo':codigo
            },
            url: $('[name="urlPesquisar"]').val(),
            dataType: "json",
            success: function (response) {
                $('#resultado').html(response['retorno']).animate();
            },
            error : function(jqXHR, textStatus, errorThrown){
                console.log(errorThrown);
            }
        });
    }
}