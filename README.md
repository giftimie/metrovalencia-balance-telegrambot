# Metrovalencia Balance Telegram Bot

Pequeño bot hecho para hacer más fácil la comprobación del saldo de viajes restantes, utilizando la web de metrovalencia. Hecho con Python 3.9

![Utilizacion](https://i.imgur.com/SYZCqH0.gif)

## Instalación

Usa el gestor de paquetes [pip](https://pip.pypa.io/en/stable/) para instalar los requerimientos.

```bash
pip install -r requirements.txt
```

## Uso

Edita el archivo de configuración [config.yaml](https://github.com/giftimie/metrovalencia-balance-telegrambot/blob/main/config.yaml) según tus necesidades.

Consigue tu API key mandándole un mensaje a [BotFather](https://t.me/botfather).

El bot solo contestará a tus mensajes, para ello debes de conseguir tu ID de usuario. Puedes hacerlo mediante [@userinfobot](https://t.me/userinfobot)

Para conseguir los enlaces de tu historial de viajes, debes de crear una cuenta en la web de [metrovalencia](https://www.metrovalencia.es/mimetrovalencia.php), si no tienes una ya. Seguidamente, registra tus tarjetas y en la tabla de tus tarjetas registradas, tendrás un enlace para ver los movimientos.

![Ver movimientos](https://i.imgur.com/zI8yez3.png)

Después de rellenar la configuración, puedes ejecutar el bot mediante:

```python
py echo_bot.py
```

## Contribuye
Las contribuciones son bienvenidas, aunque no necesarias. Tienes la libertad de hacer lo que desees con el código.


## Licencia
[WTFPL](http://www.wtfpl.net/txt/copying/)
