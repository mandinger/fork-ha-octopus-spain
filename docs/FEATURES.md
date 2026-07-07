# Funcionalidades — Octopus Spain Fork

Referencia completa de todo lo que expone la integración. La actualización de datos se realiza cada **2 horas** contra la API GraphQL de Octopus Energy España (Kraken). La autenticación puede ser por **API key** (recomendado) o email/contraseña; ver [README](../README.md#configuración).

Todos los nombres de entidad se sufijan con la cuenta entre paréntesis, p. ej. `Tarifa (A-12345678)`, y los `entity_id` incluyen el slug de la cuenta.

## Saldos

| Entidad | Estado | Notas |
|---|---|---|
| `sensor.octopus_solar_wallet_<cuenta>` | Saldo de la Solar Wallet (€) | Solo con valor real si tienes Solar Wallet |
| `sensor.octopus_octopus_credit_<cuenta>` | Crédito Octopus (€) | Referidos y bonificaciones |

## Última factura

**Sensor agregado** `sensor.octopus_last_invoice_<cuenta>`: estado = importe (€). Atributos: `Emitida`, `Inicio cargos`, `Total bruto`, `Total neto`, `Impuestos`, `Importe facturado`, `ID`, `PDF` (URL remota firmada), `PDF caduca`, `PDF expirada`, **`PDF local`** y **`PDF local path`**.

**Sensores individuales** (`sensor.octopus_last_invoice_<campo>_<cuenta>`): `invoiced_amount`, `gross_total`, `net_total`, `tax_total` (€); `issued`, `earliest_charge_at` (fecha); `id` (texto); `pdf` (ver abajo).

### PDF de la factura (copia local permanente)

La URL de PDF que devuelve la API es un enlace firmado de S3 **que caduca a los pocos minutos**. Para resolverlo, la integración **descarga el PDF automáticamente** en cada actualización (mientras la URL sigue siendo válida) y lo guarda en:

```
config/www/octopus_spain_fork/<cuenta>/invoice_<id>.pdf
```

Home Assistant lo sirve en una URL permanente: `/local/octopus_spain_fork/<cuenta>/invoice_<id>.pdf`.

- El sensor `..._pdf_...` pasa a estado `downloaded` cuando existe la copia local; atributos `local_url`, `local_path`, `url` (remota), `expires_at`, `is_expired`.
- La copia sobrevive a reinicios y no se vuelve a descargar si ya existe; los PDF de facturas anteriores se eliminan al descargar la nueva.
- ⚠️ **Privacidad**: todo lo que hay en `config/www` se sirve **sin autenticación** a cualquiera que alcance tu instancia. Las facturas contienen datos personales (nombre, dirección, CUPS).
- Nota: si `config/www` no existía al arrancar HA, la URL `/local/...` devuelve 404 hasta el siguiente reinicio (la integración crea la carpeta automáticamente).

Ejemplo en una tarjeta Markdown:

```yaml
type: markdown
content: >-
  [📄 Última factura]({{ state_attr('sensor.octopus_last_invoice_a_12345678', 'PDF local') }})
```

### Servicio `octopus_spain_fork.download_invoice`

Fuerza la (re)descarga del PDF de la última factura. Campo opcional `account` (número de cuenta); sin él, descarga para todas las cuentas.

```yaml
service: octopus_spain_fork.download_invoice
data:
  account: "A-12345678"
```

## Tarifa y contrato

| Entidad | Estado | Atributos |
|---|---|---|
| `sensor.octopus_tariff_<cuenta>` | Nombre de la tarifa | `code`, `full_name`, `valid_from`, `valid_to`, `cups`, `status`, `supplier_change_in_progress` |
| `sensor.octopus_energy_price_<cuenta>` | Precio energía P1 con impuestos (€/kWh) | Listas completas P1..Pn con/sin impuestos, `margin_term` |
| `sensor.octopus_current_price_<cuenta>` | **Precio Actual** (€/kWh) del periodo 2.0TD vigente | `period` (P1/P2/P3), `without_taxes`. Se recalcula cada hora (cambio de periodo) usando [tariff-td](https://pypi.org/project/tariff-td/); solo se crea en tarifas de 3 periodos |
| `sensor.octopus_p1_price_<cuenta>` | Precio Punta con impuestos (€/kWh) | `period`, `without_taxes`, `with_taxes` |
| `sensor.octopus_p2_price_<cuenta>` | Precio Llano con impuestos (€/kWh) | `period`, `without_taxes`, `with_taxes` |
| `sensor.octopus_p3_price_<cuenta>` | Precio Valle con impuestos (€/kWh) | `period`, `without_taxes`, `with_taxes` |
| `sensor.octopus_power_price_<cuenta>` | Precio potencia P1 con impuestos | Listas completas, `daily_fee` |
| `sensor.octopus_surplus_price_<cuenta>` | Compensación de excedentes (€/kWh) | Solo se crea si tu contrato la tiene |
| `sensor.octopus_contracted_power_<cuenta>` | Potencia contratada P1 (kW) | `p1`, `p2`, `all_periods` |
| `sensor.octopus_cups_<cuenta>` | CUPS | `status`, `self_consumption` (diagnóstico) |

Si la API no devuelve los datos de contrato, estos sensores aparecen como *no disponibles* y se recuperan en el siguiente ciclo.

## Ciclo de facturación y previsión de pago

| Entidad | Estado | Atributos |
|---|---|---|
| `sensor.octopus_next_billing_date_<cuenta>` | Próxima fecha de facturación | `period_start`, `period_end`, `is_fixed`, `period_start_day` |
| `sensor.octopus_next_payment_amount_<cuenta>` | Importe previsto del próximo pago (€) | `date` |

En cuentas con facturación flexible la API devuelve nulo y el sensor queda *no disponible* (comportamiento esperado).

## Estadísticas de energía

La integración no ofrece consumo en tiempo real: importa retroactivamente los datos horarios en el sistema de estadísticas de Home Assistant, reimportando el mes natural en curso en cada ciclo para corregir horas publicadas con retraso.

| Estadística | `statistic_id` | Uso en Panel de Energía |
|---|---|---|
| Consumo Electrico | `octopus_spain_fork:energy_consumption_<cuenta>` | Consumo de red |
| Excedente Solar | `octopus_spain_fork:energy_export_<cuenta>` | Retorno a la red |

- Ambas son sumas acumuladas horarias en kWh.
- El sensor de excedentes **solo se crea si la cuenta tiene Solar Wallet**. Como la API omite las horas sin producción (noche), esas horas se rellenan con 0 tras confirmarlas contra los totales diarios.
- **Backfill histórico**: en instalaciones nuevas (sin estadísticas previas) se importan hasta **365 días** de histórico horario, en bloques de 30 días. Las series existentes nunca se retro-rellenan (corrompería las sumas acumuladas).
- Atributos de diagnóstico: `current_month_imported_total_kwh`, `api_data_through`, `hours_not_yet_available`, `current_month_zero_filled_hours`, etc.

## Consumo del último día

`sensor.octopus_last_day_consumption_<cuenta>` ("Consumo Último Día"): total en kWh del último día con datos horarios disponibles, con el atributo `Fecha`. Útil para tarjetas y automatizaciones sin pasar por estadísticas.

## Mejoras previstas

Consulta el backlog en [IMPROVEMENTS.md](IMPROVEMENTS.md).
