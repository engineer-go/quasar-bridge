# Подробное руководство по Quasar Bridge

Полное руководство перенесено в [wiki](https://github.com/skrashevich/quasar-bridge/wiki).
Документация разбита на 37 тематических страниц с общим оглавлением и боковым меню.

- [Установка на колонку](https://github.com/skrashevich/quasar-bridge/wiki/Установка-на-колонку).
- [Сборка и первый запуск на сервере](https://github.com/skrashevich/quasar-bridge/wiki/Установка-на-сервер).
- [Все разделы](https://github.com/skrashevich/quasar-bridge/wiki).
- [Проверка полноты переноса](https://github.com/skrashevich/quasar-bridge/wiki/Проверка-переноса).

Источник переноса — ветка `cdx/v080-integration` из PR #70 (v0.8.0),
коммит `183f2335c742ad1000911c6512cba83fcafff9da`.
[Полный исходный guide.md](https://github.com/skrashevich/quasar-bridge/blob/183f2335c742ad1000911c6512cba83fcafff9da/docs/guide.md)
сохранён в истории Git. Дальнейшие изменения руководства вносите в wiki.

## Содержание

Старые якоря сохранены ниже для перехода к соответствующим страницам.

| Раздел прежнего руководства | Страница wiki |
| --- | --- |
| <a id="что-потребуется"></a>Что потребуется | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Требования#что-потребуется) |
| <a id="1-получить-и-собрать-проект"></a>1. Получить и собрать проект | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Установка-на-сервер#1-получить-и-собрать-проект) |
| <a id="2-проверить-сервер-в-прозрачном-режиме"></a>2. Проверить сервер в прозрачном режиме | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Установка-на-сервер#2-проверить-сервер-в-прозрачном-режиме) |
| <a id="3-подключить-llm-и-home-assistant"></a>3. Подключить LLM и Home Assistant | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Настройка-LLM#3-подключить-llm-и-home-assistant) |
| <a id="api-llm"></a>API LLM | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Настройка-LLM#api-llm) |
| <a id="обращения-к-модели-в-начале-фразы"></a>Обращения к модели в начале фразы | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Обращения-к-модели#обращения-к-модели-в-начале-фразы) |
| <a id="подписка-chatgptcodex"></a>Подписка ChatGPT/Codex | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Подписка-ChatGPT#подписка-chatgptcodex) |
| <a id="home-assistant-mcp"></a>Home Assistant MCP | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Home-Assistant#home-assistant-mcp) |
| <a id="проверка-обработчиков-без-колонки"></a>Проверка обработчиков без колонки | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Диагностика#проверка-обработчиков-без-колонки) |
| <a id="4-открыть-доступ-колонки-к-серверу"></a>4. Открыть доступ колонки к серверу | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Сеть-и-TLS#4-открыть-доступ-колонки-к-серверу) |
| <a id="5-направить-rooted-колонку-на-go-сервер"></a>5. Направить rooted-колонку на Go-сервер | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Подключение-колонки#5-направить-rooted-колонку-на-go-сервер) |
| <a id="запуск-на-самой-колонке-без-менеджеров-пакетов"></a>Запуск на самой колонке без менеджеров пакетов | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Установка-на-колонку#запуск-на-самой-колонке-без-менеджеров-пакетов) |
| <a id="проверенные-сценарии-установки"></a>Проверенные сценарии установки | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Установка-на-колонку#проверенные-сценарии-установки) |
| <a id="сборка-архива-для-колонки"></a>Сборка архива для колонки | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Сборка-архива-для-колонки#сборка-архива-для-колонки) |
| <a id="ручная-установка-архива"></a>Ручная установка архива | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Установка-на-колонку#ручная-установка-архива) |
| <a id="каталоги-и-управление-службой"></a>Каталоги и управление службой | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Управление-службой#каталоги-и-управление-службой) |
| <a id="подключение-и-возврат-endpoint"></a>Подключение и возврат endpoint | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Управление-службой#подключение-и-возврат-endpoint) |
| <a id="переход-с-yam"></a>Переход с YAM | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Управление-службой#переход-с-yam) |
| <a id="состояние-подписок"></a>Состояние подписок | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Состояние-подписок#состояние-подписок) |
| <a id="журнал-запросов-и-ответов"></a>Журнал запросов и ответов | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Журнал-диалогов#журнал-запросов-и-ответов) |
| <a id="свой-системный-промпт"></a>Свой системный промпт | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Системные-промпты#свой-системный-промпт) |
| <a id="контекст-последовательных-вопросов"></a>Контекст последовательных вопросов | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Контекст-диалога#контекст-последовательных-вопросов) |
| <a id="повтор-предыдущего-вопроса-через-нейросеть"></a>Повтор предыдущего вопроса через нейросеть | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Контекст-диалога#повтор-предыдущего-вопроса-через-нейросеть) |
| <a id="следующий-вопрос-после-локального-ответа"></a>Следующий вопрос после локального ответа | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Контекст-диалога#следующий-вопрос-после-локального-ответа) |
| <a id="долгие-локальные-ответы-и-тайм-аут-колонки"></a>Долгие локальные ответы и тайм-аут колонки | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Долгие-ответы#долгие-локальные-ответы-и-тайм-аут-колонки) |
| <a id="модификаторы-озвучивания"></a>Модификаторы озвучивания | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Озвучка-и-эффекты#модификаторы-озвучивания) |
| <a id="инструменты-локальной-llm"></a>Инструменты локальной LLM | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Инструменты-LLM#инструменты-локальной-llm) |
| <a id="конфигурация-инструментов"></a>Конфигурация инструментов | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Инструменты-LLM#конфигурация-инструментов) |
| <a id="настройки-голосом"></a>Настройки голосом | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Настройки-голосом#настройки-голосом) |
| <a id="изменение-маршрутизации-голосом"></a>Изменение маршрутизации голосом | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Маршрутизация-голосом#изменение-маршрутизации-голосом) |
| <a id="проверка-и-установка-обновлений"></a>Проверка и установка обновлений | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Обновления#проверка-и-установка-обновлений) |
| <a id="звуки-на-колонке"></a>Звуки на колонке | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Звуки-и-музыка#звуки-на-колонке) |
| <a id="диагностика-музыки-с-сайта"></a>Диагностика музыки с сайта | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Звуки-и-музыка#диагностика-музыки-с-сайта) |
| <a id="история-и-ограничения-веб-чтения"></a>История и ограничения веб-чтения | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Инструменты-LLM#история-и-ограничения-веб-чтения) |
| <a id="свои-mcp-серверы"></a>Свои MCP-серверы | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Свои-MCP-серверы#свои-mcp-серверы) |
| <a id="пример-поиск-через-parallel"></a>Пример: поиск через Parallel | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Свои-MCP-серверы#пример-поиск-через-parallel) |
| <a id="авторизация-и-локальные-процессы"></a>Авторизация и локальные процессы | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Свои-MCP-серверы#авторизация-и-локальные-процессы) |
| <a id="выбор-инструментов-и-ограничения"></a>Выбор инструментов и ограничения | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Свои-MCP-серверы#выбор-инструментов-и-ограничения) |
| <a id="правила-маршрутизации"></a>Правила маршрутизации | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Правила-маршрутизации#правила-маршрутизации) |
| <a id="формат-правил"></a>Формат правил | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Правила-маршрутизации#формат-правил) |
| <a id="правила-по-слову-активации"></a>Правила по слову активации | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Слова-активации#правила-по-слову-активации) |
| <a id="протокол-интеграции-для-разработчиков"></a>Протокол интеграции для разработчиков | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Протокол-слов-активации#протокол-интеграции-для-разработчиков) |
| <a id="если-ни-одно-правило-не-совпало"></a>Если ни одно правило не совпало | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Классификатор-и-обработчики#если-ни-одно-правило-не-совпало) |
| <a id="правила-по-умолчанию"></a>Правила по умолчанию | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Классификатор-и-обработчики#правила-по-умолчанию) |
| <a id="что-выполняют-обработчики"></a>Что выполняют обработчики | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Классификатор-и-обработчики#что-выполняют-обработчики) |
| <a id="переход-к-llm-после-отказа-алисы"></a>Переход к LLM после отказа Алисы | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Отказы-Алисы#переход-к-llm-после-отказа-алисы) |
| <a id="проверка-и-применение-изменений-без-перезапуска"></a>Проверка и применение изменений без перезапуска | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Перезагрузка-конфигурации#проверка-и-применение-изменений-без-перезапуска) |
| <a id="особенности-home-assistant"></a>Особенности Home Assistant | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Home-Assistant#особенности-home-assistant) |
| <a id="автозапуск-на-linux-с-systemd"></a>Автозапуск на Linux с systemd | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Автозапуск-systemd#автозапуск-на-linux-с-systemd) |
| <a id="диагностика"></a>Диагностика | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Диагностика#диагностика) |
| <a id="откат"></a>Откат | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Откат#откат) |
| <a id="справочник-конфигурации"></a>Справочник конфигурации | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Справочник-конфигурации#справочник-конфигурации) |
| <a id="лицензия"></a>Лицензия | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Лицензия#лицензия) |
| <a id="airplay"></a>AirPlay | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/AirPlay#airplay) |
| <a id="инструменты-airplay-для-llm"></a>Инструменты AirPlay для LLM | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/AirPlay#инструменты-airplay-для-llm) |
| <a id="требования-и-диагностика-airplay"></a>Требования и диагностика AirPlay | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/AirPlay#требования-и-диагностика-airplay) |
| <a id="панель-управления-в-браузере"></a>Панель управления в браузере | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Веб-панель#панель-управления-в-браузере) |
| <a id="журнал-airplay-в-браузере"></a>Журнал AirPlay в браузере | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Веб-панель#журнал-airplay-в-браузере) |
| <a id="проверка-airplay-командами"></a>Проверка AirPlay командами | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/AirPlay#проверка-airplay-командами) |
| <a id="экспериментальный-автоответ-шёпотом"></a>Экспериментальный автоответ шёпотом | [Открыть раздел](https://github.com/skrashevich/quasar-bridge/wiki/Автоматический-шёпот#экспериментальный-автоответ-шёпотом) |

### Запуск Bridge и Google MCP через Docker Compose

В репозитории есть Compose-стек с двумя контейнерами: `bridge` и локальным
`google-mcp`. Для сборки Bridge используется Go из builder-образа, поэтому Go
на хосте устанавливать не нужно. Удалённый Parallel MCP остаётся внешним HTTP
сервером и не требует отдельного контейнера.

Проверь, что `runtime.env` заполнен и содержит ключ OpenRouter и Google OAuth
client ID/secret/аккаунт. Не публикуй его и не отправляй вывод `docker compose
config`: Compose подставляет секреты в итоговую конфигурацию.

Из корня проекта запусти оба сервиса:

```bash
docker compose --env-file runtime.env up -d --build
docker compose --env-file runtime.env ps
docker compose --env-file runtime.env logs -f --tail=80 bridge google-mcp
```

У обоих контейнеров включён `restart: unless-stopped`: Docker поднимет их после
сбоя и перезапуска Docker daemon. MCP endpoint внутри сети Compose —
`http://google-mcp:8110/mcp`; порт `8110` опубликован только на loopback хоста,
чтобы OAuth callback `http://localhost:8110/oauth2callback` принимался с этого
компьютера. OAuth credentials сохраняются в `private/google-mcp-credentials`,
поэтому пересоздание контейнера не удаляет вход и не требует новой авторизации.
Папка `private/google-mcp-home` сохраняет состояние и логи MCP.

#### Повторная авторизация Google

Access token истекает, а MCP обычно обновляет его автоматически по сохранённому
refresh token. Если refresh token отозван или Google вернул `invalid_grant`,
MCP попросит войти снова. Получи новую одноразовую ссылку из работающего сервера:

```bash
python3 scripts/google-mcp-auth-url.py
```

Открой выведенную ссылку в браузере **на этом же компьютере**, выбери нужный
Google-аккаунт и подтверди доступы. Браузер вернётся на
`http://localhost:8110/oauth2callback`; MCP сам сохранит новые access и refresh
tokens в `private/google-mcp-credentials`. Скопируй URL, но не копируй токены:
вручную переносить или добавлять их в `runtime.env` не нужно. Повтори команду —
сообщение `list_calendars succeeded` подтвердит, что доступ восстановлен.
Перезапуск контейнера для обновления токена не нужен.

Статус контейнера `healthy` подтверждает только, что MCP слушает порт; он не
проверяет действительность Google-токена. Для перезапуска контейнера используй
`docker compose --env-file runtime.env restart google-mcp`. Старый host-скрипт,
который ищет PID процесса на порту `8110`, не подходит: порт занят Docker.

Проверка discovery инструментов из контейнера Bridge:

```bash
docker compose --env-file runtime.env exec bridge \
  /usr/local/bin/quasar-bridge -config /app/config.json -check-mcp
```

Перезапустить сервисы после изменения кода или настроек:

```bash
docker compose --env-file runtime.env up -d --build --force-recreate
```

Перезапустить только Google MCP:

```bash
docker compose --env-file runtime.env restart google-mcp
```

Контейнер Bridge слушает `192.168.2.52:8444`, как текущая конфигурация станции.
Не запускай одновременно host-скрипт `private/start-google-mcp.sh`: он занял бы
тот же порт `8110`.

### Пример: Google Workspace и поиск через Parallel

Скопируйте [config.mcp.example.json](../config.mcp.example.json), задайте свои `llm_base_url` и `llm_model`,
запустите Google MCP sidecar (если используете Google), загрузите `runtime.env` и проверьте подключение:

```sh
cp config.mcp.example.json config.json
set -a
. ./runtime.env
set +a
./bin/quasar-bridge -config config.json -check-config
./bin/quasar-bridge -config config.json -check-mcp
```

В примере включены [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp)
по адресу `https://search.parallel.ai/mcp` с инструментами `web_search` и
`web_fetch`. На момент проверки этот endpoint работает без аккаунта и API-ключа;
у сервиса есть ограничения бесплатного доступа. Подключение к нему не включается
в обычном конфиге автоматически.

Там же есть сервер `google` для Gmail и Google Calendar. Он подключается к
отдельному `workspace-mcp`, который должен быть запущен на **том же хосте, что и
Quasar Bridge**. В `runtime.env` укажите, например,
`QUASAR_GOOGLE_MCP_URL=http://127.0.0.1:8110/mcp`. Если Bridge работает на
колонке, `127.0.0.1` указывает на колонку: MCP-сервер тоже должен быть доступен
с неё по этому адресу или по адресу хоста.

OAuth выполняет сам `workspace-mcp`; Bridge подключается к уже авторизованному
MCP endpoint и не запускает интерактивный Google вход. OAuth client ID/secret и
адрес аккаунта нужны процессу Google MCP, не Quasar Bridge. Передавайте их
защищённо в окружение этого процесса и ограничьте его каталог только нужными
инструментами Gmail/Calendar. После запуска сервера выполните `-check-mcp`, чтобы
увидеть фактический каталог доступных инструментов. В `config.observe.example.json`
Google сервер присутствует с `disabled: true`: observe режим не вызывает MCP;
для использования скопируйте hybrid MCP-пример и оставьте сервер включённым.

Чтобы добавить сервер к существующему конфигу, дополните `assistant_tools`:

```json
{
  "assistant_tools": {
    "enabled": true,
    "mcp_servers": [
      {
        "name": "parallel",
        "transport": "streamable_http",
        "url": "https://search.parallel.ai/mcp",
        "allowed_tools": ["web_search", "web_fetch"],
        "timeout_ms": 20000,
        "max_result_chars": 3000
      }
    ]
  }
}
```

`-check-mcp` выполняет соединение и discovery, показывает имена и количество
доступных инструментов, но **не вызывает их и не обращается к LLM**. При ошибке
сервера возвращает ненулевой exit code. Для проверки полного пути:

```sh
./bin/quasar-bridge -config config.json \
  -query 'Спроси нейросеть: найди в интернете официальную документацию Go по context.WithTimeout'
```

На колонке можно сказать «Алиса, спроси нейросеть: найди официальную документацию
Go по context.WithTimeout». Префикс направляет запрос в локальную LLM. В полном
MCP-примере также добавлено правило для «найди в интернете» и «поищи в интернете».
Для других MCP добавьте свои правила `route: "llm"` или уточните промпт
классификатора. Простое подключение сервера не меняет маршрутизацию музыки,
таймеров и других запросов; правило `home` по-прежнему имеет свою позицию в списке.
Если домашними устройствами должен управлять ваш MCP, поставьте соответствующее
правило `llm` **перед** домашним правилом.
