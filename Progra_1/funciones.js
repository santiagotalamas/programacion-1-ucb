function contarVocalesYPalabras() {
    const texto = document.getElementById('texto').value;

    // Contar palabras
    const palabras = texto.trim().split(/\s+/).filter(Boolean);
    const cantidadPalabras = palabras.length;

    // Contar vocales
    const vocales = ['a', 'e', 'i', 'o', 'u'];
    let contadorVocales = 0;
    for (let letra of texto.toLowerCase()) {
        if (vocales.includes(letra)) {
            contadorVocales++;
        }
    }

    // Mostrar resultados
    document.getElementById('resultado-vocales').textContent = `Número de vocales: ${contadorVocales}`;
    document.getElementById('resultado-palabras').textContent = `Número de palabras: ${cantidadPalabras}`;
}
