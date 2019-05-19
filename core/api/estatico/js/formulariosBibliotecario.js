function pegarCSRF(){
    $.ajax({
        type: "GET",
        url: "/estudante/api/gerarCSRF/",
        crossDomain: false,
        dataType: "json",
        success: function (response) {
            return response['csrf'];
        },
        error : function(jqXHR, textStatus, errorThrown){
            console.log(errorThrown);
        }
    });
}

function cadastrarEstudante(){
    $.ajaxSetup({
        headers:{
           "X-CSRFToken": pegarCSRF()
       }
   });
    $.ajax({
        type: "POST",
        url: "/estudante/api/criando/",
        crossDomain: false,
        data: {
            'email':$('#email').val(),
            'username':$('#username').val(),
            'primeiroNome':$('#primeiroNome').val(),
            'ultimoNome':$('#ultimoNome').val(),
            'senha':$('#repetirSenha').val(),
            'repetirSenha':$('#repetirSenha').val(),
            'matricula':$('#matricula').val()
        },
        dataType: "json",
        success: function (response) {
            $('#resultado').removeClass();
            $('#resultado').addClass('alert alert-'+response['status']);
            $('#resultado').html(response['mensagem']);
        },
        error : function(jqXHR, textStatus, errorThrown){
            console.log(errorThrown);
        }
    });
}

function buscarEstudante(matricula){
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
            success: function (response) {   
                $('#resultado').html(response['retorno']).animate();
            },
            error : function(jqXHR, textStatus, errorThrown){
                console.log(errorThrown);
            }
        });
    }
}

function removerEstudante(matricula){
    $.ajaxSetup({
        headers:{
        "X-CSRFToken": $('[name="csrfmiddlewaretoken"]').val()
    }
    });
    $.ajax({
        type: "POST",
        crossDomain: false,
        url: $('[name="urlRemover"]').val(),
        data: {
            'matricula':matricula
        },
        dataType: "json",
        success: function (response) {
            $('#retorno').removeClass();
            $('#retorno').addClass('alert alert-'+response['status']).animate();
            $('#retorno').html(response['mensagem']).animate();
        },
        error : function(jqXHR, textStatus, errorThrown){
            console.log(errorThrown);
        }
    });
}
function pegarCSRFLivro(){
    $.ajax({
        type: "GET",
        url: "/estudante/api/gerarCSRF/",
        crossDomain: false,
        dataType: "json",
        success: function (response) {
            return response['csrf'];
        },
        error : function(jqXHR, textStatus, errorThrown){
            console.log(errorThrown);
        }
    });
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

function cadastrarLivro(){
    $.ajaxSetup({
        headers:{
           "X-CSRFToken": pegarCSRFLivro()
       }
   });
    $.ajax({
        type: "POST",
        url: "/livro/api/criando/",
        crossDomain: false,
        data: {
            'autor':$('#autor').val(),
            'codigo':$('#codigo').val(),
            'titulo':$('#titulo').val(),
            'versao':$('#versao').val(),
            'volume':$('#volume').val(),
        },
        dataType: "json",
        success: function (response) {
            $('#resultado').removeClass();
            $('#resultado').addClass('alert alert-'+response['status']);
            $('#resultado').html(response['mensagem']);
        },
        error : function(jqXHR, textStatus, errorThrown){
            console.log(errorThrown);
        }
    });
}

function removerLivro(codigo){
    $.ajaxSetup({
        headers:{
        "X-CSRFToken": $('[name="csrfmiddlewaretoken"]').val()
    }
    });
    $.ajax({
        type: "POST",
        crossDomain: false,
        url: $('[name="urlRemover"]').val(),
        data: {
            'codigo':codigo
        },
        dataType: "json",
        success: function (response) {
            $('#retorno').removeClass();
            $('#retorno').addClass('alert alert-'+response['status']).animate();
            $('#retorno').html(response['mensagem']).animate();
        },
        error : function(jqXHR, textStatus, errorThrown){
            console.log(errorThrown);
        }
    });
}

function removerLivro(codigo){
    $.ajaxSetup({
        headers:{
        "X-CSRFToken": $('[name="csrfmiddlewaretoken"]').val()
    }
    });
    $.ajax({
        type: "POST",
        crossDomain: false,
        url: $('[name="urlRemover"]').val(),
        data: {
            'codigo':codigo
        },
        dataType: "json",
        success: function (response) {
            $('#retorno').removeClass();
            $('#retorno').addClass('alert alert-'+response['status']).animate();
            $('#retorno').html(response['mensagem']).animate();
        },
        error : function(jqXHR, textStatus, errorThrown){
            console.log(errorThrown);
        }
    });
}

function emprestandoLivro(codigo){
    $.ajaxSetup({
        headers:{
        "X-CSRFToken": $('[name="csrfmiddlewaretoken"]').val()
    }
    });
    $.ajax({
        type: "POST",
        crossDomain: false,
        url: $('[name="urlEmprestando"]').val(),
        data: {
            'codigo':codigo
        },
        dataType: "json",
        success: function (response) {
            $('#resultado').html();
            $('#resultado').html(response['retorno']).animate();
        },
        error : function(jqXHR, textStatus, errorThrown){
            console.log(errorThrown);
        }
    });
}

function finalizarEmprestimoLivro(){
    $.ajaxSetup({
        headers:{
        "X-CSRFToken": $('[name="csrfmiddlewaretoken"]').val()
    }
    });
    $.ajax({
        type: "POST",
        crossDomain: false,
        url: $('[name="urlFinalizandoEmprestimo"]').val(),
        data: {
            'codigo':$('#codigoCampo').val(),
            'matriculaT': $('#matriculaCampo').val()
        },
        dataType: "json",
        success: function (response) {
            $('#retorno').removeClass();
            $('#retorno').addClass('alert alert-'+response['status']).animate();
            $('#retorno').html(response['mensagem']).animate();
        },
        error : function(jqXHR, textStatus, errorThrown){
            console.log(errorThrown);
        }
    });
}
function buscarEstudanteReceber(matricula){
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
            success: function (response) {   
                $('#resultado').html(response['retorno']).animate();
            },
            error : function(jqXHR, textStatus, errorThrown){
                console.log(errorThrown);
            }
        });
    }
}

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

function confirmarEntregaEmprestimo(idEmprestimo){
    if (idEmprestimo == ""){
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
                'idEmprestimo':idEmprestimo
            },
            dataType: "JSON",
            url: $('[name="urlConfirmaEntrega"]').val(),
            success: function (response) {   
                $('#resultadoModal').removeClass();
                $('#resultadoModal').addClass('alert alert-'+response['status']).animate();
                $('#resultadoModal').html(response['mensagem']).animate();
            },
            error : function(jqXHR, textStatus, errorThrown){
                console.log(errorThrown);
            }
        });
    }
}
