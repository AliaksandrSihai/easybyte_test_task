# easybyte_test_task
**Все необходимые зависимости находятся в requirements.txt, образец необходимых настроек в файле .env_sample.**
**Стек**:
- Python 3.10;
- aiogram 3.3;

**Для запуска проекта необходимо:**
- `python3 -m venv venv`
- `git clone git@github.com:AliaksandrSihai/easybyte_test_task.git`
- создать .env файл, тг бота в BotFather `https://t.me/BotFather` и пройти регистрацию для получения API по обмену валюты на `https://app.currencyapi.com/register` 
- после чего добавить токен бота и полученный API key в .env .
## Данный бот умеет конвертировать валюту по актуальному курсу для 5 валют EUR, RUB, GBP, CNY, USD, а также отвечать на приветствия/прощания от пользователя.
## Логирование выполнено на уровне INFO