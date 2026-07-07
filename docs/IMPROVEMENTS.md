# Backlog de mejoras

Lista priorizada de mejoras identificadas al revisar el código y la superficie de la API GraphQL de Kraken (esquema completo en `.codex/graphql/` y `docs/InstrospectionQuery.json`). Los ítems no están comprometidos con ninguna versión.

## Nuevas entidades / datos de la API aún sin usar

- **Histórico de facturas**: la query `account.bills` / `ledgers.invoices(first: N)` permite listar más de una factura (con paginación por cursor). Útil para un sensor de "factura anterior" o para descargar el histórico completo de PDFs.
- **`referralsCreated`**: número de referidos creados por la cuenta (sensor numérico simple).
- **`overdueBalance`**: saldo vencido de la cuenta.
- **`currentGiftCreditLeftInEur`**: crédito regalo restante.
- **`account.status`**: estado de la cuenta (diagnóstico).
- **Granularidad media-horaria**: `readingFrequencyType: THIRTY_MIN_INTERVAL` existe en la API; hoy solo se usan `HOUR_INTERVAL` y `DAY_INTERVAL`.
- **Multi-CUPS / multi-propiedad**: `supply_points()` usa el primer punto de suministro de la primera propiedad; cuentas con varios CUPS necesitarían entidades por punto de suministro.
- **Gas**: `GasFiltersInput` existe en el esquema; sin soporte actualmente.

## Robustez / deuda técnica

- **Paginación por cursor en `measurements`**: la query usa `first: 1500` sin `pageInfo { hasNextPage endCursor }`; ventanas grandes truncan datos silenciosamente. El coordinador lo mitiga troceando por días, pero la query debería paginar.
- **Manejo tipado de errores KT-\***: los errores GraphQL de Kraken llevan códigos (`KT-CT-1124` token caducado, etc.); hoy todos los errores se tratan igual. Distinguir auth vs datos permitiría reintentos más inteligentes.
- **Expiración del JWT**: no se decodifica `exp` del token; la re-autenticación es reactiva (`force_login=True` tras fallo). Un refresco proactivo evitaría el primer fallo.
- **Simplificar `_InvoiceRefreshMixin`**: los temporizadores que refrescan la URL firmada 5 min antes de caducar pierden relevancia ahora que el PDF se guarda localmente; se pueden retirar o reducir.
- **Dividir `sensor.py`** (~2000 líneas): separar en `entity.py` / `statistics.py` / `sensor.py`.
- **Eliminar `lib/graphql_helpers/generated.py`**: codegen no usado por el runtime.
- **`DeviceInfo` por cuenta**: agrupar las entidades de cada cuenta bajo un dispositivo en el registro de HA.
- **Almacenamiento privado de PDFs**: opción para guardar en `config/media` (autenticado, accesible vía Media Browser) en lugar de `config/www` (sin autenticación), u opción de ruta configurable.
- **Arreglar los `timedelta` "chapuzas"** señalados en el comentario de `lib/octopus_spain_fork.py` (ventanas de fechas de la query de facturación).
- **Tests**: carpeta `tests/` con `pytest-homeassistant-custom-component` y fixtures de payloads reales (hay una prueba offline de regresión del issue #29 descrita en el mensaje de ese fix).

## Ideas de producto

- Sensor de coste estimado del mes en curso (consumo importado × precios de la tarifa).
- Notificación/evento cuando se emite una factura nueva (trigger sobre el cambio de `ID`).
- Descarga histórica de PDFs de todas las facturas (combina "histórico de facturas" + `InvoicePdfManager`).
