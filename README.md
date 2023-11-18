# BurpScopeCreator.py
🔨 Generador de archivos de configuración para el Scope y Out of Scope para BurpSuite.

## Descripción

🔥 Este script automatiza la tarea de generar un archivo de configuración para el apartado de **Scope** en Burp Suite de modo que al proporcionar los dominios y subdominios del scope y fuera del scope, este script lo automatiza generando el archivo `.json` de forma interactiva para el usuario.

## Modo de uso

✅ Primero se generan los archivos para los dominios y subdominios del Scope y luego lo mismo pero para el Out of Scope

✅ Luego se ejecuta el script y se le proporcionan los argumentos necesarios para realizar la configuración.

✅ **Importante** no incluir los caracteres "*" en el de subdominio.

**En el caso de no haber una lista de dominios o subdominios tanto del scope como out-of-scope simplemente se deja el campo vacío.**

# Preview

![preview_usage](https://raw.githubusercontent.com/mateofumis/BurpScopeCreator.py/main/preview_usage.png)

### Dentro de Burp Suite:

![preview-burpsuite](https://raw.githubusercontent.com/mateofumis/BurpScopeCreator.py/main/preview_burpsuite.png)
