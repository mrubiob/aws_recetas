var loginForm = document.getElementById('loginForm');

loginForm.onsubmit = function(event){
    /* evet se refiere al evento que estoy escuchando */
    event.preventDefault(); // previene el comportamiento x default de mi formulario
    
    // necesitamos obtener los datos del formulario
    var formulario = new FormData(loginForm);
    // formulario = { "email":#elena@coding.com", "password":"1234"}

        fetch('/login', { method:'POST', body: formulario })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if(data.message == 'correcto') {
                //Todo está correcto y me redirige a dashboard
                window.location.href = "/dashboard";
            } else {
                var mensajeAlerta = document.getElementById('mensajeAlerta');
                mensajeAlerta.innerHTML = data.message;

                //Formato de alerta con colores
                mensajeAlerta.classList.add('alert');
                mensajeAlerta.classList.add('alert-danger');
            }
             //alert(data.message), poner en comentario desde var 19, ver vincular con los modales
            // ver como resaltar el dato del formulario que está equivocado
        })


}
