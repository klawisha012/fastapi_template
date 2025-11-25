# FastAPI Template

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-E92063?logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?logo=prometheus&logoColor=white)](https://prometheus.io/)


Шаблон FastAPI без готовых эндпоинтов, но с полностью настроенной инфраструктурой: асинхронная база данных, система конфигураций и метрики Prometheus.

---

## 🚀 Возможности

* **FastAPI** — современный, быстрый веб‑фреймворк на Python.
* **uv** — чрезвычайно быстрый менеджер пакетов и проектов Python.
* **Async SQLAlchemy / Async DB** — асинхронная работа с базой данных.
* **Настройки через pydantic-settings** — удобная и безопасная конфигурация.
* **Prometheus / Metrics** — встроенная метрика `/metrics` для мониторинга.
* **Структура проекта** — готовая архитектура для масштабирования.

---

## ⚙️ Установка

```bash
uv sync
```

---

## ▶️ Запуск приложения

```bash
python -m src.main
```

## 📊 Метрики Prometheus

После запуска сервиса доступно:

```
/metrics
```

Совместимо с Prometheus и Grafana.

Шаблон подготовлен для быстрого старта проектов на FastAPI.
