//funcion que valida 
$(function(){
    $("#mi-formulario").validate({
        rules:{
            rut:{
                required:true
            },
            nom:{
                required:true
            },
            username:{
                required:true
            },
            correo:{
                required:true,
                correo:true
            },
            direc:{
                required:true
            },
            pass:{
                required:true
            },
            fono:{
                required:true,
                number:true
            },
            fecha:{
                required:true
            },
            pass2:{
                required:true,
                equalTo:pass
            }
        },
        messages:{
            rut:{
                required:'Ingrese rut del usuario',
                minlength:'Caracteres insuficientes (10)'
                },
            nom:{
                required:'Ingrese nombre completo',
                minlength:'Caracteres insuficientes (3)'
                },
            username:{
                required:'Ingrese nombre de usuario',
                minlength:'Caracteres insuficientes (3)'
                },
            correo:{
                required:'Ingrese correo del usuario',
                email:'Formato incorrecto del correo'
                },
            direc:{
                required:'Ingrese direccion',
                minlength:'Caracteres insuficientes (3)'
                },
            pass:{
                required:'Ingrese una contraseña',
                minlength:'Caracteres insufientes (8)'
                },
            fono:{
                required:'Ingrese un telefono valido',
                minlength:'Cantidad de digitos insuficientes'
                },
            fecha:{
                required:'Seleccione una fecha valida',
                min:'Fecha invalida'
                },
            pass2:{
                required:'Ingrese una contraseña',
                minlength:'Caracteres insufientes (8)',
                equalTo:'Contraseñas no coiciden'
                },
        }//message
    });
});

//funcion hace mayusculas
function upperText(texto)
    {
        const x = texto;
        x.value= x.value.toUpperCase();
    }
;

//funcion reloj
function mueveReloj(){
    momentoActual = new Date()
    hora = momentoActual.getHours()
    minuto = momentoActual.getMinutes()
    segundo = momentoActual.getSeconds()

    str_segundo = new String (segundo)
    if (str_segundo.length == 1)
       segundo = "0" + segundo

    str_minuto = new String (minuto)
    if (str_minuto.length == 1)
       minuto = "0" + minuto

    str_hora = new String (hora)
    if (str_hora.length == 1)
       hora = "0" + hora

    horaImprimible = hora + " : " + minuto + " : " + segundo

    document.form_reloj.reloj.value = horaImprimible

    setTimeout("mueveReloj()",1000)
};

//función que cambia el color de fondo a orange
function colorOrange(obj){
    obj.style.backgroundColor='orange';
};

function colorBlanco(obj){
    obj.style.backgroundColor='white';
};