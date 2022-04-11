# CdM-Daily-Rewards
Pequeño script para el juego "Corazón de Melón (Web Version)" que completa 2 de los minijuegos diarios automáticamente.

# Antes de ejecutar
Debes instalar los siguientes paquetes
- colorama
- selenium
- webdriver-manager

Para ello ejecutar el siguiente comando: `pip install colorama selenium webdriver-manager`

# Configurar

Añadir las cuentas dentro de `cuentas.json`:

```json
{
    "Nombre_de_ejemplo": {
        "usuario": "usuario@gmail.com",
        "contraseña": "contraseña"
    },
    "null": {
        "usuario": "",
        "contraseña": ""
    }
}
```
`Puedes añadir las cuentas que necesites siguiendo la estructura ;)`