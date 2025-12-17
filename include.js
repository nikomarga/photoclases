document.getElementById("formContacto").addEventListener("submit", async function (e) {
    e.preventDefault();

    const data = {
        nombre : e.target.nombre.value,
        correo : e.target.correo.value,
        mensaje : e.target.mensaje.value
    }

    const response  = await fetch("http://localhost:5000/enviar", {
        method: "POST",
        headers: {
            "Content-Type":"application/json"
        },
        body: JSON.stringify(data)
    });

    const resultado = await response.json();
    alert(resultado.mensaje);
    e.target.reset();
});

