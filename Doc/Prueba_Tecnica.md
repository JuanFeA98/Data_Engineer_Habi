## 🏠 PRUEBA DATA ENGINEER HABI CO
___

**Importante:** Se recomienda leer todo el documento antes de empezar, en el momento en que usted reciba el correo de la prueba tendrá (3 días) para enviar el correo con las respuestas. Lo que busca esta prueba es evaluar su nivel de entendimiento desarrollando pipelines de datos capaces de ejecutarse en una nube como GCP y su capacidad para buscar documentación para la configuración de los servicios necesarios, así como evaluar sus conocimientos con contenedores Docker. 

**⚒️ PROBLEMA:**

Debe desarrollar un ETL en Python o Java que realice la lectura de un archivo XML (que fue proporcionado junto con este examen), lo transforme, extraiga características y lo persista en una base de datos MySQL. La base de datos destino deberá contener dos entidades: usuarios y propiedades debidamente relacionadas e indexadas. La ejecución del proceso debe hacerse dentro de un contenedor Docker que se conecte con la base de datos que de igual manera deberá estar corriendo en un contenedor Docker. Se permite y se alienta el uso de un orquestador de contenedores.

**📚 Requisitos:**
Dividir el proceso en las siguientes etapas:
●	Pre procesamiento y limpieza de datos del XML origen
●	Pipeline de datos con salida hacia la base de datos
●	Reporte de resultados de ejecución
●	Debe contener documentación clara de cómo ejecutar el proyecto
●	Debe ser entregado en un repositorio público GIT del proveedor de su preferencia

Datos por extraer de los inmuebles:
1.	Ubicación (estado, ciudad, colonia, calle y número exterior)
2.	Tipo de inmueble
3.	Transacción
4.	Precio
5.	Código de proveedor
6.	Correo de contacto
7.	Teléfono de contacto

Datos por extraer de los usuarios:
1.	Correo de contacto

**🏠 PREGUNTAS DE NEGOCIO:**

Cuando tenga el resultado hay que responder a las siguientes preguntas, incluyendo el query utilizado para generar la respuesta: 
1.	¿Cuántos usuarios hay registrados?
2.	¿Cuántas propiedades hay por cada usuario?
3.	¿Cuántas casas y cuántos departamentos hay por estado?
4.	¿Tenemos códigos duplicados? ¿Por qué?

**🚧 Bonus:**
Usa Apache Beam para implementar el pipeline de datos y Kubernetes como orquestador de contenedores.


**📔 ¿Cómo se evalúa?**

- **Funcionalidad:**
Se cumplen las 3 etapas de forma clara, concisa y abstraída. Se cumple con la carga de datos en MySQL y se pueden responder con queries las preguntas de negocio.
- **Ejecución y orquestación:**
La ejecución está configurada para ser ejecutada en contenedores y correctamente orquestada.
- **Calidad del Código:**
Código bien estructurado y fácil de mantener.
- **Manejo de Errores:**
El script maneja correctamente las excepciones y errores posibles.
- **Documentación:**
Documentación clara de toda la solución y de cómo ejecutar el pipeline en local.
- **Entrega en repositorio GIT:**
Se evaluará el correcto uso del repositorios de GIT. Mostrando conocimiento en manejo de branches, commits, comentarios, etc.
