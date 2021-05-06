const formulario = document.getElementById('register-form')
const inputs = document.querySelectorAll('#register-form input')


const expresiones = {
	usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
	correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
//	password: /^.{4,12}$/, // 4 a 12 digitos.
	password: /^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$/, // 4 a 12 digitos.
}

const campos = {

    username: false,
    email: false,
    password1: false,

}

const validarFormulario = (e) => {
    switch (e.target.name){
        case "username":
            validarCampo(expresiones.usuario, e.target, 'username');
//              console.log('Funciona!')
        break;
        case "email":
            validarCampo(expresiones.correo, e.target, 'email');
        break;
        case "password1":
            validarCampo(expresiones.password, e.target, 'password1');
            validarPassword2();

        break;
        case "password2":
            validarPassword2();
        break;

    }
}

const validarCampo = (expresion, input, campo) => {
    if(expresion.test(input.value)){
        document.getElementById(`grupo__${campo}`).classList.remove("formulario__grupo-incorrecto");
        document.getElementById(`grupo__${campo}`).classList.add("formulario__grupo-correcto");
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos[campo] = true;
    }else{
        document.getElementById(`grupo__${campo}`).classList.add("formulario__grupo-incorrecto");
        document.getElementById(`grupo__${campo}`).classList.remove("formulario__grupo-correcto");
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');
        campos[campo] = false;
    }
}

const validarPassword2 = () =>{
    const inputPassword1 = document.getElementById('id_password1')
    const inputPassword2 = document.getElementById('id_password2')
    if(inputPassword1.value !== inputPassword2.value ){
        document.getElementById(`grupo__password2`).classList.add("formulario__grupo-incorrecto");
        document.getElementById(`grupo__password2`).classList.remove("formulario__grupo-correcto");
        document.querySelector(`#grupo__password2 .formulario__input-error`).classList.add('formulario__input-error-activo');
        campos['password1'] = false;
    }else{
        document.getElementById(`grupo__password2`).classList.remove("formulario__grupo-incorrecto");
        document.getElementById(`grupo__password2`).classList.add("formulario__grupo-correcto");
        document.querySelector(`#grupo__password2 .formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos['password1'] = true;
    }
}

inputs.forEach((input) =>{
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
});

formulario.addEventListener('submit', (e)=> {
//    e.preventDefault();
//
//    if(campos.username && campos.email && campos.password1){
//        formulario.reset();
//    }else{
//        document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
//    }
});

