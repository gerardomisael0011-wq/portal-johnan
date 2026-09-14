function scrollToAreas() {
    document.getElementById("areas").scrollIntoView({
        behavior: "smooth"
    });
}


function abrirArea(nombre) {

    // Convertimos el nombre del área en un formato
    // adecuado para utilizarlo dentro de la URL.

    const nombreUrl = encodeURIComponent(nombre);

    // Enviamos al usuario a la página dinámica del área.
    window.location.href = "/area/" + nombreUrl;
}