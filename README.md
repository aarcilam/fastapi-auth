# FastAPI Auth - Microservicio de Autenticación y Gestión de Usuarios

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-teal.svg)](https://fastapi.tiangolo.com/)
[![Neo4j](https://img.shields.io/badge/Neo4j-2025.06-green.svg)](https://neo4j.com/)
[![License](https://img.shields.io/badge/License-Open%20Source-green.svg)](LICENSE)

## 📋 Descripción

**FastAPI Auth** es un microservicio open source desarrollado en Python con Neo4j que proporciona un sistema completo de autenticación y gestión de usuarios. Este proyecto está diseñado para ser modular, escalable y fácil de integrar en arquitecturas de microservicios modernas.

El sistema ofrece capacidades avanzadas de autenticación con soporte para sesiones, roles, capacidades y notificaciones, aprovechando el poder de las bases de datos de grafos para modelar relaciones complejas entre usuarios y sus recursos.

## ✨ Funcionalidades

### 🔐 Autenticación
- **Registro de usuarios**: Creación de nuevas cuentas con validación de datos y asignación de roles (user/admin)
- **Login seguro**: Autenticación mediante username y contraseña con encriptación bcrypt
- **Login OAuth2**: Endpoint compatible con el estándar OAuth2 Password Grant para integración con herramientas y librerías OAuth2
- **Gestión de sesiones**: Control y seguimiento de sesiones activas de usuarios
- **Tokens JWT**: Generación de tokens de acceso y refresh tokens
- **Refresh tokens**: Renovación de tokens de acceso expirados mediante cookies HttpOnly
- **Intentos de login**: Seguimiento de intentos de autenticación fallidos

### 👥 Gestión de Usuarios
- **CRUD de usuarios**: Creación, lectura y gestión de usuarios
- **Estados de usuario**: Control de usuarios activos, bloqueados
- **Metadatos personalizados**: Almacenamiento de información adicional en formato JSON

### 🔑 Control de Acceso
- **Sistema de roles**: Asignación y gestión de roles a usuarios
- **Capacidades**: Control granular de permisos mediante capacidades
- **Relaciones complejas**: Modelado de jerarquías y relaciones entre usuarios

### 📬 Notificaciones
- **Sistema de notificaciones**: Relación entre usuarios y notificaciones
- **Historial de notificaciones**: Seguimiento de notificaciones recibidas

## 🏗️ Arquitectura

El proyecto sigue una arquitectura limpia y modular:

```
src/
├── config/          # Configuración de la aplicación
├── controllers/     # Lógica de controladores
├── dtos/            # Data Transfer Objects (DTOs)
├── models/          # Modelos de Neo4j con neomodel
├── routes/          # Rutas de FastAPI
└── services/        # Lógica de negocio
```

## 🚀 Tecnologías

### Python + FastAPI
Este proyecto utiliza **Python** como lenguaje principal y **FastAPI** como framework web por las siguientes ventajas:

- **Rendimiento excepcional**: FastAPI es uno de los frameworks más rápidos de Python, comparable a NodeJS y Go
- **Documentación automática**: Genera documentación interactiva (Swagger/OpenAPI) automáticamente
- **Type hints nativos**: Soporte completo para type hints, mejorando la mantenibilidad del código
- **Validación automática**: Validación de datos mediante Pydantic integrado
- **Async/Await**: Soporte nativo para operaciones asíncronas, ideal para I/O intensivo
- **Ecosistema maduro**: Acceso a la vasta biblioteca de paquetes de Python
- **Fácil de aprender**: Sintaxis clara y legible, ideal para proyectos open source

### Neo4j (Base de Datos de Grafos)
El proyecto utiliza **Neo4j** como base de datos por las siguientes razones:

- **Relaciones complejas**: Excelente para modelar relaciones entre usuarios, roles, sesiones y notificaciones
- **Consultas intuitivas**: Lenguaje de consulta Cypher es más legible que SQL para relaciones complejas
- **Rendimiento en relaciones**: Optimizado para consultas basadas en relaciones y recorridos de grafos
- **Flexibilidad de esquema**: Permite evolucionar el modelo de datos sin migraciones complejas
- **Trazabilidad**: Ideal para rastrear relaciones como "quién creó qué" o "qué usuarios tienen qué roles"
- **Escalabilidad horizontal**: Neo4j puede escalar para manejar grandes volúmenes de datos relacionados
- **APOC procedures**: Acceso a librerías avanzadas para importación/exportación y análisis

### Stack Tecnológico Completo

- **FastAPI**: Framework web moderno y rápido
- **Neo4j**: Base de datos de grafos
- **neomodel**: ODM (Object Document Mapper) para Neo4j
- **Pydantic**: Validación de datos y configuración
- **JWT (PyJWT)**: Tokens de autenticación
- **bcrypt**: Encriptación de contraseñas
- **Docker & Docker Compose**: Containerización y orquestación

## 📦 Requisitos Previos

- Docker y Docker Compose instalados
- Python 3.8+ (si ejecutas localmente sin Docker)

## 🔧 Instalación

### Opción 1: Docker Compose (Recomendado)

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/fastapi-auth.git
cd fastapi-auth
```

2. Crea un archivo `.env` con la siguiente configuración:
```env
DATABASE_URL=bolt://neo4j:test1234@fastapi-neo4j-db-service:7687
SECRET_KEY=tu-clave-secreta-super-segura-aqui
DEBUG=True
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7
```

3. Inicia los servicios:
```bash
docker-compose up -d
```

El servicio estará disponible en `http://localhost:8000`

### Opción 2: Instalación Local

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

2. Configura Neo4j localmente o usa una instancia remota

3. Configura las variables de entorno (crea un archivo `.env`)

4. Ejecuta la aplicación:
```bash
uvicorn src.main:app --reload
```

## 📚 Documentación de la API

Una vez que el servicio esté en ejecución, puedes acceder a la documentación interactiva:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🔌 Endpoints Disponibles

### Autenticación (`/auth`)

- `POST /auth/register` - Registro de nuevos usuarios
  - **Parámetros**: `name`, `username`, `email`, `password`, `phone` (opcional), `role` (opcional, valores: "user" o "admin", por defecto: "user")
- `POST /auth/login` - Inicio de sesión (retorna Access Token y Refresh Token)
  - **Parámetros**: `username`, `password`, `ip_address`
  - **Respuesta**: 
    ```json
    {
      "message": "Login successful",
      "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
      "token_type": "bearer",
      "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    }
    ```
- `POST /auth/token` - Inicio de sesión compatible con OAuth2 (form-data)
  - **Compatibilidad**: Endpoint estándar OAuth2 para integración con herramientas y librerías que soportan el flujo OAuth2
  - **Formato**: `application/x-www-form-urlencoded`
  - **Parámetros**: `username`, `password` (enviados como form-data)
  - **Respuesta**:
    ```json
    {
      "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
      "token_type": "bearer"
    }
    ```
- `GET /auth/refresh-token` - Renovación de Access Token usando Refresh Token
  - **Método**: Cookie-based (Refresh Token debe enviarse en cookie `refresh_token`)
  - **Respuesta**:
    ```json
    {
      "message": "Token refreshed successfully",
      "token": {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
      }
    }
    ```

### Usuarios (`/users`)

- `GET /users/` - Listar todos los usuarios

## 🔄 Flujo de Autenticación con Tokens

Este microservicio implementa un sistema de autenticación robusto basado en dos tipos de tokens con diferentes tiempos de expiración. Este enfoque proporciona seguridad mejorada y una mejor experiencia de usuario.

### Flujo Completo

#### 1. Inicio de Sesión (Login)

El sistema ofrece **dos endpoints** para autenticación:

**Opción A: `POST /auth/login`** (Recomendado para aplicaciones web)
- Retorna Access Token, Refresh Token y metadata adicional
- Formato JSON estándar
- Permite especificar `ip_address` para seguimiento

**Opción B: `POST /auth/token`** (Compatibilidad OAuth2)
- Compatible con el estándar OAuth2 Password Grant
- Formato form-data (`application/x-www-form-urlencoded`)
- Ideal para integración con librerías OAuth2 y herramientas de testing

Cuando un usuario realiza login exitoso (usando cualquiera de los dos endpoints), el servidor responde con **dos tokens**:

- **Access Token**: Token de corta duración (por defecto: 15 minutos)
- **Refresh Token**: Token de larga duración (por defecto: 7 días)

**Respuesta de `/auth/login`:**
```json
{
  "message": "Login successful",
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Respuesta de `/auth/token`:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

#### 2. Almacenamiento en el Cliente (Frontend)

El cliente debe almacenar los tokens de la siguiente manera:

- **Refresh Token**: Almacenado en una **cookie HttpOnly** (segura contra acceso desde JavaScript)
  - Esto proporciona protección adicional contra ataques XSS
  - El navegador enviará automáticamente la cookie en cada petición al servidor

- **Access Token**: Almacenado en **localStorage** o **sessionStorage**
  - Se utiliza para autenticar las peticiones a las APIs del backend
  - Se envía en el header `Authorization: Bearer <access_token>`

#### 3. Uso Normal de la Aplicación

Durante el uso normal de la aplicación:

- El cliente utiliza el **Access Token** para realizar todas las peticiones a las APIs protegidas
- El token se incluye en el header de autorización: `Authorization: Bearer <access_token>`
- Mientras el token no expire, el usuario puede acceder a los recursos protegidos

#### 4. Renovación de Access Token

Cuando el **Access Token** expira:

1. El cliente detecta que el token ha expirado (generalmente mediante un error 401)
2. El cliente realiza una petición al endpoint `GET /auth/refresh-token` del servidor de autenticación
3. El **Refresh Token** se envía automáticamente en la cookie (HttpOnly)
4. El servidor valida el Refresh Token:
   - Verifica que el token sea válido y no haya expirado
   - Verifica que esté asociado a una sesión activa del usuario
5. Si es válido, el servidor retorna un **nuevo Access Token**
6. El cliente actualiza el Access Token almacenado y continúa operando normalmente

```http
GET /auth/refresh-token
Cookie: refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

Response:
{
  "message": "Token refreshed successfully",
  "token": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
  }
}
```

#### 5. Expiración del Refresh Token

Cuando el **Refresh Token** también expira:

- El servidor rechazará cualquier intento de renovación
- El cliente debe detectar esta situación
- El usuario será **deslogueado automáticamente** y redirigido a la página de login
- El usuario deberá iniciar sesión nuevamente para obtener nuevos tokens

### Ventajas de Este Flujo

✅ **Seguridad mejorada**: Los tokens de acceso de corta duración limitan el tiempo de exposición en caso de robo  
✅ **Experiencia de usuario fluida**: Renovación automática sin interrumpir la sesión del usuario  
✅ **Protección contra XSS**: El Refresh Token en HttpOnly cookie no es accesible desde JavaScript  
✅ **Control granular**: Puedes revocar sesiones específicas sin afectar otras sesiones del usuario  
✅ **Trazabilidad**: Todas las sesiones y renovaciones se registran en Neo4j para auditoría  

### Configuración de Tiempos de Expiración

Los tiempos de expiración se configuran mediante variables de entorno:

```env
ACCESS_TOKEN_EXPIRE_MINUTES=15    # Tiempo de vida del Access Token (minutos)
REFRESH_TOKEN_EXPIRE_DAYS=7       # Tiempo de vida del Refresh Token (días)
```

### Diagrama de Flujo

```
┌─────────┐          ┌──────────────┐          ┌─────────────┐
│ Cliente │          │ Auth Server  │          │   API Backend│
└────┬────┘          └──────┬───────┘          └──────┬───────┘
     │                      │                          │
     │  1. POST /auth/login │                          │
     │─────────────────────>│                          │
     │                      │                          │
     │  Access + Refresh    │                          │
     │<─────────────────────│                          │
     │                      │                          │
     │  2. Almacenar tokens │                          │
     │  (localStorage +     │                          │
     │   HttpOnly cookie)   │                          │
     │                      │                          │
     │  3. GET /api/resource│                          │
     │  Header: Bearer token │                         │
     │─────────────────────────────────────────────────>│
     │                      │                          │
     │                      │       4. Validar token   │
     │                      │<─────────────────────────│
     │                      │                          │
     │                      │    5. Response 200 OK   │
     │                      │─────────────────────────>│
     │  6. Response data    │                          │
     │<─────────────────────────────────────────────────│
     │                      │                          │
     │  7. Token expirado   │                          │
     │  (401 Unauthorized)  │                          │
     │<─────────────────────────────────────────────────│
     │                      │                          │
     │  8. GET /auth/refresh-token                     │
     │  Cookie: refresh_token                          │
     │─────────────────────>│                          │
     │                      │                          │
     │  9. Nuevo Access Token                          │
     │<─────────────────────│                          │
     │                      │                          │
```

## 🔐 Seguridad

- Las contraseñas se encriptan usando **bcrypt**
- Los tokens JWT se utilizan para autenticación stateless
- Soporte para refresh tokens para mayor seguridad
- Variables de entorno para configuración sensible
- Validación de datos en todas las entradas
- **Refresh Tokens en HttpOnly cookies**: Protección adicional contra XSS
- **Tokens de acceso de corta duración**: Minimiza el riesgo de exposición

## 🧪 Desarrollo

### Estructura del Proyecto

El proyecto sigue principios de arquitectura limpia:

- **DTOs**: Definen la estructura de datos de entrada/salida
- **Controllers**: Manejan las peticiones HTTP
- **Services**: Contienen la lógica de negocio
- **Models**: Definen los modelos de Neo4j con neomodel
- **Routes**: Definen los endpoints de la API

### Agregar Nuevas Funcionalidades

1. Define los modelos en `src/models/`
2. Crea los DTOs necesarios en `src/dtos/`
3. Implementa la lógica de negocio en `src/services/`
4. Crea los controladores en `src/controllers/`
5. Define las rutas en `src/routes/`
6. Registra las rutas en `src/main.py`

## 🤝 Contribuir

Este es un proyecto open source y las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto es open source y está disponible bajo la licencia MIT.

## 🆘 Soporte

Para reportar bugs o solicitar features, por favor abre un issue en el repositorio de GitHub.

## 👨‍💻 Autor

Desarrollado con ❤️ por la comunidad open source

---

**Nota**: Este microservicio está diseñado para ser parte de una arquitectura de microservicios más amplia. Asegúrate de configurar adecuadamente los servicios de red y seguridad en tu entorno de producción.

