# Aplikacija za rezervaciju mesta za pab kvizove

Web aplikacija za rezervaciju mesta na pab kvizovima. Sistem omogućava
pregled kvizova, prikaz lokacije na mapi i rezervaciju mesta
putem web interfejsa.

Aplikacija se sastoji iz dva dela:

-   **Backend** -- Django + Django REST Framework (API)
-   **Frontend** -- Next.js (React + TypeScript + Tailwind)
-   **Baza podataka** -- PostgreSQL (Docker) / SQLite (lokalno)
-   **Docker podrška** -- docker + docker-compose

------------------------------------------------------------------------

#  Arhitektura sistema

Frontend (Next.js)

Backend (Django REST API)\

PostgreSQL (Docker container)

------------------------------------------------------------------------

#  5.4 Dokumentacija projekta 

##  Opis aplikacije

Aplikacija omogućava:

-   pregled dostupnih pab kviz događaja
-   prikaz lokacija pomoću Leaflet mape
-   rezervaciju mesta za kviz
-   REST API komunikaciju između frontend i backend dela

Backend obezbeđuje REST API za rad sa podacima, dok frontend koristi taj
API za prikaz i interakciju sa korisnicima.

------------------------------------------------------------------------

### Korišćene tehnologije

# Backend

-   Python
-   Django 6
-   Django REST Framework
-   drf-spectacular (OpenAPI dokumentacija)
-   django-cors-headers
-   PostgreSQL (u Docker okruženju)
-   SQLite (lokalno)
-   psycopg / psycopg2
-   python-dotenv

# Frontend

-   Next.js 16
-   React 19
-   TypeScript
-   Tailwind CSS
-   Leaflet
-   React-Leaflet

# DevOps

-   Docker
-   Docker Compose
-   PostgreSQL 16 (alpine image)

------------------------------------------------------------------------

# ▶ Lokalno pokretanje aplikacije (bez Docker-a)

## Backend


- cd backend
- python -m venv venv
- venv\Scripts\activate
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver


Backend: http://localhost:8000

------------------------------------------------------------------------

## Frontend


- cd frontend
- npm install
- npm run dev


Frontend: http://localhost:3000

------------------------------------------------------------------------

#  Pokretanje pomoću Docker-a


docker-compose up --build


Servisi:

  Servis     Port   Opis
  ---------- ------ --------------------
  db         5432   PostgreSQL baza
  backend    8000   Django REST API
  frontend   3000   Next.js aplikacija

------------------------------------------------------------------------

# 5.5 Dokumentacija grana

## main

-   Stabilna verzija projekta
-   Produkcioni kod

## develop

-   Integraciona grana
-   U nju se merguju sve feature grane

## Feature grane

### feature/maps

-   Implementacija Leaflet mape

### feature/postgresql

-   Konfiguracija PostgreSQL baze i Docker-a

### feature/emails

-   Implementacija email notifikacija

------------------------------------------------------------------------

# Struktura projekta

root\
├── backend\
├── frontend\
├── docker-compose.yml\
└── README.md

------------------------------------------------------------------------


