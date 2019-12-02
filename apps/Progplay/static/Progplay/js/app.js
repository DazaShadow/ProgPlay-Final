
$(document).ready(function () {
    $("#formulario").validate({

        errorClass: "is-invalid",
        rules: {
            nombre: {
                required: true
            },
            correo: {
                required: true,
                email: true

            }





        },
        messages: {
            nombre: {
                required: "El nombre es obligatorio"
            },
            correo:{

                required: "El correo es obligatorio",
                email:"Debe ingresar un email valido"

            },
            pais:{
                required:"El pais es obligatorio"
            },
            ciudad:{
                required:"La ciudad es obligatoria"
            },
            alias:{
                required:"El alias es obligatorio"
            },
            contraseña:{
                required:"La contraseña es obligatoria"
            }



        }


    })
})

$("#formulario").submit(function(){
if($("#formulario").valid()
){
return true

}else {

    Swal.fire({
        type: 'error',
        title: 'Oops...',
        text: 'Something went wrong!',
        footer: '<a href>Why do I have this issue?</a>'
      })

}





})

function dragstart(caja, event) {
    // el elemento a arrastrar
    document.getElementById(caja.id).className = "in";
    event.dataTransfer.setData('Data', caja.id);
}

function drag() {
    return false;
}

function dragend(caja) {
    document.getElementById(caja.id).className = "out";
    return false;
}

function dragenter() {
    document.getElementById("container").className = "inContainer";
    return false;
}

function dragleave() {
    document.getElementById("container").className = "outContainer";
    return false;
}

function dragover(event) {
    event.preventDefault();

    return false;
}

function drop(target, event) {
    // obtenemos los datos
    var caja = event.dataTransfer.getData('Data');
    document.getElementById("container").className = "outContainer";
    // agregamos el elemento de arrastre al contenedor
    target.appendChild(document.getElementById(caja))
}






