const formulario=document.getElementById('iniciar');
const inputs=document.querySelectorAll("#iniciar input");
const formulario_registrar=document.getElementById('registrar');
const inputs_registrar=document.querySelectorAll('#registrar input');

const expresiones = {
	usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, 
	password: /^.{4,12}$/, // 4 a 12 digitos.
	correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
}
const campos={
    email:false,
    password:false,
}
const campos_registrar={
    nombre:false,
    email1:false,
    password1:false,


}
const validarFormulario=(e)=>{
    switch(e.target.name){
        case "your_email":
            validarCampo(expresiones.correo,e.target,'email');

        break;
        case "your_password":
            validarCampo(expresiones.password,e.target,'password');
        break;
        case "name1":
            validarCampo(expresiones.usuario,e.target,'nombre');
        break;
        case "email":
            validarCampo(expresiones.correo,e.target,'email1');
        break;
        case "password":
            validarCampo(expresiones.password,e.target,'password1');
            validarPassword();
        break;
        case "repeatpassword":
            validarPassword();
        break;

    }

}

const validarCampo = (expresion,input,campo)=>{
    if(expresion.test(input.value)){
        document.getElementById(`formularioContent-${campo}`).classList.remove('formulario__incorrecto');
        document.getElementById(`formularioContent-${campo}`).classList.add('formulario__correcto');
        document.querySelector(`#formularioContent-${campo} i`).classList.add('fa-check-circle');
        document.querySelector(`#formularioContent-${campo} i`).classList.remove('fa-times-circle');
        document.querySelector(`#formularioContent_${campo} .formulario_error`).classList.remove('formulario_error-activo');
        if (campo=='email' || campo=='password'){
                campos[campo]=true;
        }else{
            campos_registrar[campo]=true;
        }


    }else{
        document.getElementById(`formularioContent-${campo}`).classList.remove('formulario__correcto');
        document.getElementById(`formularioContent-${campo}`).classList.add('formulario__incorrecto');
        document.querySelector(`#formularioContent-${campo} i`).classList.remove('fa-check-circle');
        document.querySelector(`#formularioContent-${campo} i` ).classList.add('fa-times-circle');
        document.querySelector(`#formularioContent_${campo} .formulario_error`).classList.add('formulario_error-activo');
        if (campo=='email' || campo=='password'){
            campos[campo]=false;
    }else{
        campos_registrar[campo]=false;
    }

    }
}
const validarPassword = () =>{
    const inputPassword1=document.getElementById("password");
    const inputPassword2=document.getElementById("repeatpassword");

    if(inputPassword1.value !== inputPassword2.value){
        document.getElementById('formularioContent-password2').classList.remove('formulario__correcto');
        document.getElementById(`formularioContent-password2`).classList.add('formulario__incorrecto');
        document.querySelector(`#formularioContent-password2 i`).classList.remove('fa-check-circle');
        document.querySelector(`#formularioContent-password2 i` ).classList.add('fa-times-circle');
        document.querySelector(`#formularioContent_password2 .formulario_error`).classList.add('formulario_error-activo')
        campos_registrar['password1']=false;
    }else{
        document.getElementById('formularioContent-password2').classList.remove('formulario__incorrecto');
        document.getElementById(`formularioContent-password2`).classList.add('formulario__correcto');
        document.querySelector(`#formularioContent-password2 i`).classList.add('fa-check-circle');
        document.querySelector(`#formularioContent-password2 i`).classList.remove('fa-times-circle');
        document.querySelector(`#formularioContent_password2 .formulario_error`).classList.remove('formulario_error-activo')
        campos_registrar['password1']=true;
    }
}
inputs.forEach((input)=>{
    input.addEventListener('keyup',validarFormulario);
    input.addEventListener('blur',validarFormulario);

});
inputs_registrar.forEach((input)=>{
    input.addEventListener('keyup',validarFormulario);
    input.addEventListener('blur',validarFormulario);

})
formulario.addEventListener('submit',(e)=>{
    e.preventDefault()
    if(campos.email && campos.password){
        formulario.reset();
        document.getElementById('formulario_ErrorIniciar').classList.remove('formulario_mensajeError-activo');


        document.getElementById("formulario_mensaje-exitoIniciar").classList.add("formulario_mensaje-exito-activo");
        setTimeout(()=>{
            document.getElementById("formulario_mensaje-exitoIniciar").classList.remove("formulario_mensaje-exito-activo");
        },5000);
        document.querySelectorAll('.formulario__correcto').forEach((icono)=>{
            icono.classList.remove('formulario__correcto');

        });

    }else{
        document.getElementById('formulario_ErrorIniciar').classList.add('formulario_mensajeError-activo');
    }


    
})
formulario_registrar.addEventListener('submit',(e)=>{
    e.preventDefault()
    const politicas=document.getElementById("terminos");
    if(campos_registrar.nombre && campos_registrar.email1 && campos_registrar.password1 && politicas.checked){
        formulario_registrar.reset();
        document.getElementById('formulario_mensajeRegistrar').classList.remove("formulario_mensajeError-activo");
        document.getElementById("formulario_mensaje-exitoRegistrar").classList.add("formulario_mensaje-exito-activo");
        setTimeout(()=>{
        document.getElementById("formulario_mensaje-exitoRegistrar").classList.remove("formulario_mensaje-exito-activo");

        },5000);
        document.querySelectorAll('.formulario__correcto').forEach((icono)=>{
            icono.classList.remove('formulario__correcto');

        });
    }else{
        document.getElementById('formulario_mensajeRegistrar').classList.add("formulario_mensajeError-activo");
    }
});
    




let carrito=[]

