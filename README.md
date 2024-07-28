# Sitio web

Este sitio web está construido usando [Docusaurus](https://docusaurus.io/), un generador de sitios web estáticos moderno.

## Como agregar soluciones

### Solo el markdown con LaTeX

Si no te manejas con GitHub, puedes dejar tu solucion hecha en Markdown + LaTeX en las [issues](https://github.com/crow-rojas/apuntes-fundamentals/issues)
del repositorio, así las puedo ver y las agrego al sitio web. Aquí tienes un [ejemplo](https://github.com/crow-rojas/apuntes-fundamentals/issues/3).

### Directamente al proyecto (solo si sabes trabajar con GitHub)

Si deseas agregar alguna solución a un ejercicio, haz un fork de este repositorio y edita/agrega un archivo `.mdx` en la
carpeta del ejercicio correspondiente. Por ejemplo, si deseas agregar una solución al ejercicio 21 de Computación de la guía
del 2016-1, deberías editar el archivo `docs/engineering/computing/exercises/2016-1/p21.mdx`. Ahí, puedes agregar tu solución
dentro de la sección `<MDXDetails> y <summary>Solución propuesta</summary>`.

Con lo tengas listo, puedes hacer un Pull Request a este repositorio y se revisará tu solución.

También, puedes contactarme directamente a través de mi [correo electrónico](mailto:cristobal.rojasbrito@gmail.com) si deseas
ser voluntario/a de este lindo proyecto.

## Desarrollo

### Instalación

Instala las dependencias con:

```bash
yarn
```

### Desarrollo local

```bash
yarn start
```

Este comando inicia un servidor de desarrollo local y abre una ventana del navegador. La mayoría de los cambios se reflejan en vivo sin tener que reiniciar el servidor.

### Build

```bash
yarn build
```

Este comando genera contenido estático en el directorio `build` y puede ser servido usando cualquier servicio de hosting de contenido estático.

Con

```bash
yarn serve
```

puedes ver el sitio web generado. Este modo pierde el 'hot-reload'.

### Despliegue

Usando SSH:

```bash
USE_SSH=true yarn deploy
```

Sin usar SSH:

```bash
GIT_USER=<Your GitHub username> yarn deploy
```

Si estás usando otro servicio de hosting, puedes subir el contenido estático generado en el directorio `build`.
