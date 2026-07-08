# UK → Spain feature port plan — Intelligent Go first

> Implementation plan produced from a comparison of this fork against the UK
> `HomeAssistant-OctopusEnergy` integration (BottlecapDave) and the Spanish Kraken
> introspection schema (`docs/InstrospectionQuery.json`). Read-only Intelligent Go is the
> primary deliverable; the rest of the portable UK feature set is catalogued below.

## Context

This fork (`custom_components/octopus_spain_fork`) is a **sensor-only** integration on the
shared **Kraken** GraphQL platform (`https://api.oees-kraken.energy/v1/graphql/`). The UK
integration is far richer, and there is a standing request for **Intelligent Octopus Go**
(EV smart-charging / dispatches).

Key finding: **the Spanish endpoint exposes the full SmartFlex / intelligent-dispatch API
surface** — it is simply unused today. Confirmed present in the Spanish schema: query fields
`devices`, `flexPlannedDispatches` (→ `SmartFlexDispatch`), `plannedDispatches` /
`completedDispatches` (→ `UpsideDispatchType`), `registeredKrakenflexDevice`,
`vehicleChargingPreferences`; types `SmartFlexVehicle` / `SmartFlexChargePoint`; mutations
`updateDeviceSmartControl`, `setVehicleChargePreferences`, `deleteBoostCharge`.

**Constraints / decisions:**
- Building this for *other* enrolled users — we cannot validate end-to-end against a live
  enrolled Spanish account. Code must degrade gracefully to **"no entities"** when the account
  has no device / returns empty data.
- **Intelligent Go ships read-only first** (no control mutations in phase 1).
- Plan also covers **every other portable UK feature**.
- **Step 0 is a throwaway read-only probe**; everything after it is gated on that probe
  returning data. If the probe is empty for all test accounts, phase 1 still ships safely
  (creates no entities) but stays unverifiable until an enrolled user tests it.

---

## Compatibility matrix (all UK features → Spain status)

| UK feature | Spain status | Action |
|---|---|---|
| **Intelligent Octopus Go** (dispatches, EV/charger, smart/boost charge) | Schema present, unused | **PORT — primary** |
| Cost tracker (client-side cost of a power sensor, day/week/month) | Not present; API-independent | **PORT — portable** |
| Tariff comparison (compare product vs. consumption) | Partially feasible; Spain product model differs | Port (lower confidence) |
| Target-rate / cheapest-hours sensors | Not present; valuable for 2.0TD/surplus | Optional port (Spain-adapted) |
| "Data last retrieved" diagnostic sensors | Not present; generic | Optional polish |
| Electricity/gas consumption & cost sensors | Consumption statistics already present (Energy Dashboard) | Already covered (Spain form) |
| Rates / standing charge / off-peak | `current_price` + P1/P2/P3 already present | Already covered (Spain form) |
| Gas | `GasFiltersInput` in schema, no gas product wired | Defer (needs a gas user) |
| Octoplus (saving sessions, free electricity, points) | UK loyalty program | **Skip — UK-only** |
| Wheel of Fortune | UK-only | **Skip** |
| Greenness / Greener Nights forecast | UK grid | **Skip** |
| Heat pump / Cosy 6 (climate, water_heater) | UK product | **Skip** |
| Home Mini / Home Pro live consumption | UK hardware | **Skip** |

Net new portable work: **Intelligent Go** (primary), **Cost tracker**, then optional
Tariff comparison / cheapest-hours / diagnostics.

---

## Shared foundation (needed before any new entity platform)

1. **Add platforms.** `__init__.py` `PLATFORMS = [Platform.SENSOR]` → add
   `Platform.BINARY_SENSOR` (and later `SWITCH`, `NUMBER`, `TIME`/`SELECT` for phase-2
   controls). Mirror the eager `importlib.import_module(f"{__name__}.sensor")` for each new
   platform module.
2. **Second coordinator for fast-changing data.** The existing `OctopusCoordinator`
   (`coordinator.py`) polls every `UPDATE_INTERVAL = 2` **hours** — too slow for dispatches.
   Add `OctopusIntelligentCoordinator(DataUpdateCoordinator)` with a ~5-minute interval
   (`INTELLIGENT_UPDATE_MINUTES = 5`). Keep it isolated so a SmartFlex outage never affects
   billing/consumption.
3. **Extend runtime data.** `runtime.py` `OctopusSpainRuntimeData` gains an optional field
   `intelligent: OctopusIntelligentCoordinator | None = None`, set in `async_setup_entry`.
4. **API client methods.** Add methods to `OctopusSpain` (`lib/octopus_spain_fork.py`)
   following the existing per-call pattern exactly: fresh
   `GraphqlClient(endpoint=GRAPH_QL_ENDPOINT, headers={"authorization": self._token})`,
   re-login if `self._token is None`, reuse `_error_message` + the issue-#29 null-guard
   (`(response.get("data") or {}).get(...) or {}`).

---

## Step 0 — Feasibility probe (throwaway, read-only)

Write a small script under `scripts/` (pattern of `scripts/generate_graphql_helpers.py`) or a
one-off pytest that logs in with a real token and runs:

```graphql
query ($account: String!) {
  devices(accountNumber: $account) {
    id name deviceType provider status
    __typename
    ... on SmartFlexVehicle { make model }
    ... on SmartFlexChargePoint { make model }
  }
  plannedDispatches(accountNumber: $account) { start end delta deltaKwh meta { source location } }
  completedDispatches(accountNumber: $account) { start end delta deltaKwh meta { source location } }
}
```

Purpose: confirm which fields resolve (schema has them; entitlement/permission may differ),
learn the real `deviceType`/`provider`/`status` enum values and dispatch shapes for Spain, and
decide whether account-scoped `plannedDispatches` is enough or device-scoped
`flexPlannedDispatches(deviceId:)` is needed. **Do not commit the probe.**

---

## Phase 1 — Intelligent Go, read-only (primary deliverable)

### API client (`lib/octopus_spain_fork.py`)
- `async def devices(self, account)` → list of `{id, name, device_type, provider, status,
  make, model}`. Empty list on no devices / errors (never raise for "no device").
- `async def dispatches(self, account)` → `{"planned": [...], "completed": [...]}`, each item
  normalized to `{start, end, delta_kwh, source, location}`. Tolerate field-level errors.
  Confirm exact `meta`/`delta`/`deltaKwh` fields against the Step-0 probe.

### Coordinator (`coordinator.py`, new class)
`OctopusIntelligentCoordinator`: each ~5-min cycle, per account fetch `devices` + `dispatches`;
store `data[account] = {"devices": [...], "planned": [...], "completed": [...]}`.

### Entities (read-only) — gate creation on ≥1 device; no device ⇒ create nothing
Create `binary_sensor.py`; add sensors to `sensor.py`. Follow `(account)`-suffixed naming and
`unique_id` conventions.

| Entity | Platform | Represents |
|---|---|---|
| `OctopusIntelligentDispatching` | binary_sensor | ON when a dispatch is active now; attrs `planned_dispatches`, `completed_dispatches`, `current_start/end`, `next_start/end`, `provider`. |
| `OctopusIntelligentState` | sensor | Device `status`/`currentState` string. |
| `OctopusIntelligentNextDispatchStart` / `...End` | sensor (timestamp) | Next planned dispatch window. |
| `OctopusIntelligentDeviceInfo` | sensor (diagnostic) | make/model/provider/device_type attrs. |

"Dispatch active now" = any planned/started window where `start <= now < end`; "next" = earliest
future planned window (logic mirrored conceptually from UK
`custom_components/octopus_energy/intelligent/__init__.py`).

### Wiring
- `async_setup_entry`: build `OctopusIntelligentCoordinator`, do a **non-fatal** first refresh
  (a SmartFlex failure must never block the whole entry), store on `runtime_data.intelligent`,
  forward the `BINARY_SENSOR` platform, eager-import the new module.
- Add translations (`strings.json`, `translations/en.json`, `translations/es.json`).

### Tests
`tests/test_intelligent.py` (style of `tests/test_lib.py`): device-present, device-absent,
`{"data": null}` (issue #29), active vs. no-active-dispatch. Assert normalizers + "dispatching
now / next" logic, and that empty `devices` creates zero entities.

---

## Phase 2 — Intelligent Go controls (deferred; documented, not built yet)

When a live enrolled account can validate mutations, add control platforms (`switch.py`,
`number.py`, `time.py`/`select.py`):
- **Smart-charge suspend/resume switch** → `updateDeviceSmartControl(SmartControlAction)`.
- **Boost-charge switch** → boost mutation + `deleteBoostCharge`.
- **Target SoC number / ready-by time+select** → `setVehicleChargePreferences` /
  `vehicleChargingPreferences`.
Mutations write to a user's car/charger — must not ship unvalidated.

---

## Other portable features

- **Cost tracker** (recommended second): port UK `cost_tracker/` conceptually — config sub-entry
  naming a source consumption sensor + price → day/week/month cost sensors. Pure client-side
  math (no Kraken calls). Needs a config-flow "kind" + `update_cost_tracker`/`reset_cost_tracker`
  services.
- **Tariff comparison** (optional, lower confidence): only after confirming Spanish product/tariff
  codes are queryable; Spain's product model (`activeAgreement.product`, `atrTariffs`,
  `currentAtrTariffCode`) differs from UK.
- **Cheapest-hours / target-rate sensor** (optional, Spain-adapted): valuable for 2.0TD/variable +
  surplus; compute cheapest N-hour windows from Spain price data (`current_price` / P1-P3).
  Design fresh, don't port UK code.
- **Diagnostic "data last retrieved" sensors** (optional polish): expose each coordinator's last
  success timestamp.

### Config-flow note
`config_flow.py` currently only handles account auth (email/password or API key) — **no sub-entry
kinds** like the UK flow. Intelligent phase 1 needs **no config change** (auto-discovered from
`devices`). Cost tracker / comparison require introducing an options-driven or sub-entry config
surface; that is part of those features' scope, not the foundation.

---

## Files to create / modify (phase 1)

**Create:** `custom_components/octopus_spain_fork/binary_sensor.py`; `tests/test_intelligent.py`;
(throwaway) `scripts/probe_intelligent.py`.

**Modify:** `lib/octopus_spain_fork.py` (add `devices()`+`dispatches()`), `coordinator.py`
(add `OctopusIntelligentCoordinator`), `runtime.py` (add `intelligent` field), `__init__.py`
(build/refresh coordinator, add `BINARY_SENSOR`, eager-import), `sensor.py` (add intelligent
sensors), `const.py` (`INTELLIGENT_UPDATE_MINUTES`), `strings.json` + `translations/*.json`,
`docs/FEATURES.md`.

---

## Verification

1. **Probe (Step 0):** run `scripts/probe_intelligent.py` with a real token; record whether
   `devices`/`plannedDispatches` return data and the exact enum/field shapes. Gating check.
2. **Unit tests:** `uv run pytest tests/ -q` (CI runs tests + ruff + pylint).
3. **No-device safety:** with a mocked empty `devices` response, `async_setup_entry` loads
   cleanly and creates **zero** intelligent entities (the "building blind" guarantee).
4. **Lint:** `uv run ruff check` and `uv run pylint custom_components/octopus_spain_fork`.
5. **Live (enrolled user, if reachable):** confirm the dispatching binary_sensor toggles across a
   real dispatch window. Otherwise mark phase 1 "ships safe, awaiting live confirmation."

## Open risks
- Entitlement unknown: schema ≠ account access. Step 0 probe resolves this.
- Exact `UpsideDispatchType.meta` / `delta` vs `deltaKwh` shapes must be confirmed from the probe.
- Spanish device `provider`/`status` enum values may differ from UK — read them from the probe,
  don't hardcode UK enum strings.
