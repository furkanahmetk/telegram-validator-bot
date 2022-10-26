# Casper Validator Bot

Casper Validator Bot is a Telegram bot that provides information about active validators working on Casper Network.

### Prerequisites

Python3, pip and make packages should be installed on your system.

#### Install MongoDB

Download and run the mongo db server from official [website](https://www.mongodb.com/docs/manual/administration/install-community/).

Also, in the [Install DB File](assets/INSTALL%20DB.md) it is explained how to install and configure DB on MacOS as an example.

### How to set-up

1. Run [back-end](https://github.com/furkanahmetk/Casper-Bot-Optimized-API).

2. Clone the repository.
```
$ git clone https://github.com/furkanahmetk/telegram-validator-bot
```

<<<<<<< Updated upstream
2. Create a `.env` file from the `example.env` template:
=======
3. Navigate to repository folder.
```
$ cd telegram-validator-bot
```
4. Create a `.env` file from the `example.env` template:
>>>>>>> Stashed changes

```shell
$ cp example.env .env
```

<<<<<<< Updated upstream
3. Create a new Telegram bot. See [how to](assets/telegram.md)

4. Copy your Telegram bot token to .env file.

5. Run MongoDB.
=======
5. Create a new Telegram bot. See [how to](assets/telegram.md)

6. Copy your Telegram bot token to .env file.

7. Edit `src/config.py`.

``
Add your back-end URL and port to BASE_URL varieble. By default it is set to 'http://localhost:5555/'
``


8. Run MongoDB.
>>>>>>> Stashed changes

````shell
$ mongosh
````

6. Run app.py

```shell
$ python src/app.py
```