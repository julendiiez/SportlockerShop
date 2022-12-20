const formulario = document.getElementById('iniciar');
const inputs = document.querySelectorAll("#iniciar input");
const formulario_registrar = document.getElementById('registrar');
const inputs_registrar = document.querySelectorAll('#registrar input');
var entraIniciar = false;

const expresiones = {
    usuario: /^[a-zA-Z0-9\_\-]{3,16}$/,
    password: /^.{4,12}$/, // 4 a 12 digitos.
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
}
const campos = {
    email: false,
    password: false,
}
const campos_registrar = {
    nombre: false,
    email1: false,
    password1: false,
    usuarioExistente: false,
    usuarioExistenteValido:false,


}
const validarFormulario = (e) => {
    console.log(campos_registrar.nombre)
    console.log(campos_registrar.email1)
    console.log(campos_registrar.password1)

    switch (e.target.name) {
        case "your_email":
            validarCampo(expresiones.correo, e.target, 'email');

            break;
        case "your_password":
            validarCampo(expresiones.password, e.target, 'password');
            break;
        case "name1":
            validarCampo(expresiones.usuario, e.target, 'nombre');
            break;
        case "email":
            validarCampo(expresiones.correo, e.target, 'email1');
            validarEmail(e.target)
            break;
        case "password":
            validarCampo(expresiones.password, e.target, 'password1');
            validarPassword();
            break;
        case "repeatpassword":
            validarPassword();
            break;

    }

}

const validarCampo = (expresion, input, campo) => {
    if (expresion.test(input.value)) {
        document.getElementById(`formularioContent-${campo}`).classList.remove('formulario__incorrecto');
        document.getElementById(`formularioContent-${campo}`).classList.add('formulario__correcto');
        document.querySelector(`#formularioContent-${campo} i`).classList.add('fa-check-circle');
        document.querySelector(`#formularioContent-${campo} i`).classList.remove('fa-times-circle');
        document.querySelector(`#formularioContent_${campo} .formulario_error`).classList.remove('formulario_error-activo');
        if (campo == 'email' || campo == 'password') {
            campos[campo] = true;
        } else {
            campos_registrar[campo] = true;
        }


    } else {
        document.getElementById(`formularioContent-${campo}`).classList.remove('formulario__correcto');
        document.getElementById(`formularioContent-${campo}`).classList.add('formulario__incorrecto');
        document.querySelector(`#formularioContent-${campo} i`).classList.remove('fa-check-circle');
        document.querySelector(`#formularioContent-${campo} i`).classList.add('fa-times-circle');
        document.querySelector(`#formularioContent_${campo} .formulario_error`).classList.add('formulario_error-activo');
        if (campo == 'email' || campo == 'password') {
            campos[campo] = false;
        } else {
            campos_registrar[campo] = false;
        }

    }
}
const validarPassword = () => {
    const inputPassword1 = document.getElementById("password");
    const inputPassword2 = document.getElementById("repeatpassword");

    if (inputPassword1.value !== inputPassword2.value) {
        document.getElementById('formularioContent-password2').classList.remove('formulario__correcto');
        document.getElementById(`formularioContent-password2`).classList.add('formulario__incorrecto');
        document.querySelector(`#formularioContent-password2 i`).classList.remove('fa-check-circle');
        document.querySelector(`#formularioContent-password2 i`).classList.add('fa-times-circle');
        document.querySelector(`#formularioContent_password2 .formulario_error`).classList.add('formulario_error-activo')
        campos_registrar['password1'] = false;
    } else {
        document.getElementById('formularioContent-password2').classList.remove('formulario__incorrecto');
        document.getElementById(`formularioContent-password2`).classList.add('formulario__correcto');
        document.querySelector(`#formularioContent-password2 i`).classList.add('fa-check-circle');
        document.querySelector(`#formularioContent-password2 i`).classList.remove('fa-times-circle');
        document.querySelector(`#formularioContent_password2 .formulario_error`).classList.remove('formulario_error-activo')
        campos_registrar['password1'] = true;
    }
}

const validarEmail = (input) => {
    campos_registrar['usuarioExistente'] = false;
    campos_registrar['usuarioExistenteValido'] = false;

    $.ajax({
        type: 'GET',
        url: '/informacionEmails',
        success: function (response) {
            const data = response.data
            data.forEach(el => {
                if (el.email == input.value) {
                    campos_registrar['usuarioExistente'] = true;
                    document.getElementById("formularioContent-email1").classList.remove('formulario__correcto');
                    document.getElementById("formularioContent-email1").classList.add('formulario__existe');
                    document.querySelector(`#formularioContent_email1 .formulario_existente`).classList.add('formulario_existente-activo')

            
                    



                }

            })

            if (campos_registrar['usuarioExistente'] == false) {
                campos_registrar['usuarioExistenteValido'] = true;
                document.getElementById("formularioContent-email1").classList.remove('formulario__existe');
                document.querySelector(`#formularioContent_email1 .formulario_existente`).classList.remove('formulario_existente-activo')

            }
        },
        error: function (error) {
            console.log(error)
        }
    });

}
inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);

});
inputs_registrar.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);

})
formulario.addEventListener('submit', (e) => {
    if (!(campos.email && campos.password)) {
        e.preventDefault()
        document.getElementById('formulario_ErrorIniciar').classList.add('formulario_mensajeError-activo');
    }


})




formulario_registrar.addEventListener('submit', (e) => {
    const politicas = document.getElementById("terminos");
    if (!(campos_registrar.nombre && campos_registrar.email1 && campos_registrar.password1 && politicas.checked && campos_registrar.usuarioExistenteValido)) {
            e.preventDefault()
            document.getElementById('formulario_mensajeRegistrar').classList.add("formulario_mensajeError-activo");
    }
});




