# Instagram Follower Tracker

Una herramienta en **Python** para saber **quién te dejó de seguir y quién es nuevo seguidor en Instagram**, usando listas copiadas directamente desde la app.

No usa API, no hace scraping raro, no pide login.  
Solo copiar → pegar → ejecutar

---

## ¿Qué problema resuelve?

Instagram **no te dice claramente**:

- quién te dejó de seguir
- quién es nuevo seguidor

Este proyecto compara listas de seguidores y te da:

- Unfollowers
- Nuevos seguidores

Además, **recuerda automáticamente la última lista**, así no tienes que andar manejando dos archivos cada vez

---

## ¿Cómo funciona (en simple)?

1. Copias tu lista de seguidores desde Instagram
2. La pegas en un archivo `.txt`
3. Ejecutas el programa pasando ese archivo
4. El sistema:
   - Detecta usernames reales
   - Ignora nombres, emojis y puntos medios (`·`)
   - Compara contra la última lista guardada
   - Genera los resultados
   - Guarda la lista actual para la próxima vez

Solo necesitas **un archivo por día**.

---

## Estructura del proyecto

```
Follower-tracker/
├── main.py
├── src/
│   ├── parser.py       # Limpia y detecta usernames reales
│   ├── comparator.py   # Compara sets (día anterior vs hoy)
│   └── writer.py       # Escribe los resultados en archivos
├── data/
│   ├── raw/            # Archivos copiados desde Instagram
│   └── state/
│       └── last_followers.txt  # Base interna (NO TOCAR)
├── output/
│   ├── unfollowers.txt
│   └── new_followers.txt
```

---

## Cómo usarlo

### Paso previo (MUY IMPORTANTE)

1. Abre **Instagram desde el navegador web** (Chrome, Edge, etc.)

   > No funciona correctamente desde la app móvil

2. Ve a tu perfil → **Seguidores**

3. Selecciona **todos los seguidores**, cópialos y pégalos **tal cual** en un archivo `.txt`

4. Guarda el archivo dentro de:
   data/raw/

**No edites ni manipules el texto copiado**  
El sistema está diseñado para limpiar automáticamente los datos.

---

### ¿Cómo se ven los datos copiados?

Instagram copia cosas como:

liliancaroline_28

Carol

samanta73762

·

samanta

boryryss

·

🩹

Detalles importantes:

- A veces viene:
  - username + nombre real
  - username + `·` + nombre
  - emojis
- Todo eso es **normal**
- El sistema:
  - detecta el username real
  - ignora nombres, emojis y separadores

---

### Primera vez que lo ejecutas

```bash
python main.py data/raw/today.txt
```

**En este punto:**

- No hay comparación todavía
- Se guarda la lista como base inicial

### Siguentes ejecuciones

- Haz los mismos pasos de copiar los seguidores.
- Pegalos en el archivo txt dentro de data/raw

- Despues ejecuta lo siguiente

```bash
python main.py data/raw/today.txt
```

**Salida esperada:**

```
Comparación realizada correctamente
Resultados guardados en /output
```

---

## Archivos generados

Después de comparar, encontrarás:

**`output/unfollowers.txt`**  
Usuarios que te dejaron de seguir

**`output/new_followers.txt`**  
Usuarios que empezaron a seguirte

**`data/state/last_followers.txt`**  
La última lista válida usada como base

**No edites este archivo manualmente**, el sistema lo gestiona solo.

---

## Requisitos

- Python 3.10 o superior
- No necesita librerías externas
- Funciona en Windows, Mac y Linux

---

## Autor

Proyecto personal hecho paso a paso, con errores reales, debugging real y aprendizaje real
