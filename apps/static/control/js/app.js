
// CONFIRMAR ANTES DE ELIMINAR

document.querySelectorAll(".form-eliminar").forEach(
    function(formulario) {

        formulario.addEventListener("submit", function(evento) {

            let respuesta = confirm(
                "¿Seguro que deseas eliminar este registro?"
            );

            if (!respuesta) {
                evento.preventDefault();
            }

        });

    }
);

// MOSTRAR CAMPOS SEGÚN EL TIPO DE REUNIÓN

let tipo = document.getElementById("id_tipo_reunion");

if (tipo) {

    let direccion = document.getElementById("id_direccion");
    let referencia = document.getElementById("id_referencia");
    let enlace = document.getElementById("id_enlace_virtual");

    function mostrarCampos() {

        let virtual = tipo.value === "Virtual";

        direccion.parentElement.style.display =
            virtual ? "none" : "block";

        referencia.parentElement.style.display =
            virtual ? "none" : "block";

        enlace.parentElement.style.display =
            virtual ? "block" : "none";
    }

    tipo.addEventListener("change", mostrarCampos);

    mostrarCampos();
}
