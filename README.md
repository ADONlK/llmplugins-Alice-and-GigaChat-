# llm plugins

## Что потребуется

### Alice (YandexGPT)

- аккаунт Yandex Cloud
- API-ключ
- folder_id

### GigaChat

- API-ключ GigaChat


# Установливаем библиотеку llm

```bash
pip install llm
```

# Установливаем плагины для Алисы и GigaChat

```bash
cd llmalice
pip install -e .
```

```bash
cd ../llm_gigachat
pip install -e .
```

# Добавление ключей

## Alice

```bash
llm keys set alice
```

## GigaChat

```bash
llm keys set gigachat
```

# Использование

## Alice

```bash
llm -m alice "Привет"
```

## GigaChat

```bash
llm -m gigachat "Привет"
```




