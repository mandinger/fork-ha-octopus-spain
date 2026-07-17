# Roadmap: HACS custom integration → official Home Assistant core integration

Step-by-step TODO list for turning this HACS integration (`octopus_spain_fork`, a fork of
[MiguelAngelLV/ha-octopus-spain](https://github.com/MiguelAngelLV/ha-octopus-spain)) into an
official Home Assistant core integration.

Verified against the Home Assistant developer docs as of **2026-07-10**: the **Bronze quality
tier is mandatory for all new core integrations**
(<https://developers.home-assistant.io/docs/core/integration-quality-scale/checklist>), and
checked against the actual state of this repo.

## Repo-specific gaps found

These drive several TODO items below:

| Gap | Where | Core requirement violated |
|---|---|---|
| API client embedded in integration (~1,020 lines) | `custom_components/octopus_spain_fork/lib/` | ADR-0004: API code must live in a standalone published PyPI library |
| `version` key in manifest | `manifest.json` | Forbidden in core manifests (custom-component-only key) |
| `iot_class: local_polling` | `manifest.json` | It's a cloud GraphQL API → must be `cloud_polling` |
| Fork-branded domain/name | `manifest.json` | Domain must be brand-appropriate (`octopus_spain`), no "fork" |
| Service registered in `async_setup_entry` | `__init__.py` | Bronze rule `action-setup`: register in `async_setup` |
| `importlib` preload hack for sensor module | `__init__.py` | Not accepted in core; platforms load normally |
| PDF download to `config/www/` | `invoice_pdf.py`, `__init__.py` | Writing user-served files to `www` won't pass core review |
| Tests are library-level only (~185 lines) | `tests/` | Bronze rule `config-flow-test-coverage`: 100% config-flow coverage in HA test harness |
| Shipped `translations/es.json` | `translations/` | Core ships only `strings.json`; other languages go through Lokalise |
| Brand images inside component | `custom_components/octopus_spain_fork/brand/` | Must be a PR to `home-assistant/brands` instead |

---

## Phase 0 — Strategic decisions (before writing any code)

- [ ] **Coordinate with the upstream author.** This repo is a fork of `MiguelAngelLV/ha-octopus-spain`. Core submission makes you the long-term code owner of the *brand's* integration. Options: submit jointly, get their blessing, or at minimum credit them per the `LICENSE.txt` terms. Doing this first avoids a public authorship dispute on the core PR.
- [ ] **Pick the final domain.** `octopus_spain_fork` cannot ship. `octopus_spain` is the natural choice (the UK community integration already occupies `octopus_energy` in the brands repo's custom-integrations namespace). Verify availability: no folder in `homeassistant/components/octopus_spain` in core, and no clash in `home-assistant/brands`.
- [ ] **Decide the initial feature scope.** Core reviewers require *small* first PRs: config flow + one platform with a limited set of entities. Recommended initial scope: sensor platform (solar wallet, last invoice, current prices). Defer to follow-up PRs: the `download_invoice` service, recorder statistics backfill, and extra sensors. Recommended to **drop or redesign** for core: the PDF-to-`www` feature (writing user-downloadable files into `config/www` will not pass review — a redesign would target `media_source`/media dirs, or expose the invoice URL as an entity attribute instead).
- [ ] **Accept the maintenance commitment.** You will be listed in `CODEOWNERS`; reviewers expect responsiveness to issues/PRs (Silver tier requires an *active* code owner). Also accept the review timeline: new-integration PRs commonly wait weeks-to-months in the queue.
- [ ] **Sign the Home Assistant CLA** (prompted automatically on your first PR).

## Phase 1 — Extract the API client into a standalone PyPI library

ADR-0004: all protocol/API-specific code must live outside core in a published package.

- [ ] Create a new repo (e.g. `octopus-spain-api`) and move into it:
  - `custom_components/octopus_spain_fork/lib/octopus_spain_fork.py` (772 lines — the GraphQL client)
  - `custom_components/octopus_spain_fork/lib/graphql_helpers/` (generated query helpers, 248 lines)
  - The invoice-PDF fetch logic from `invoice_pdf.py` (the HTTP download part; the file-placement part stays out)
- [ ] Make the library HA-compliant: fully async (`aiohttp`, injectable `ClientSession`), typed (`py.typed` marker), no logging of credentials, its own exceptions for auth-failed vs cannot-connect vs API-changed (the integration maps these to `ConfigEntryAuthFailed` / `ConfigEntryNotReady` / `UpdateFailed`).
- [ ] Keep the existing test suite (`tests/test_lib.py`) with the library; expand it — the *library* repo is where API behavior tests live, core tests mock the library.
- [ ] Dependency transparency (Bronze rule `dependency-transparency`): publish to PyPI **from CI** (e.g. GitHub Actions trusted publishing), public repo, OSI license, pinned version. Audit transitive deps: `python-graphql-client==0.4.3` is stale/unmaintained — prefer plain `aiohttp` GraphQL POSTs inside your library so the integration's only requirement is your own package. Same scrutiny applies to `tariff-td==1.1`.
- [ ] Release `v1.0.0` on PyPI before touching core.

## Phase 2 — Bring the integration code to Bronze tier

Work against the official checklist (developers.home-assistant.io → integration-quality-scale/checklist). Bronze rules and their current status here:

- [ ] `config-flow` — exists ✔; polish: data descriptions in `strings.json` for every field, proper `data`/`options` separation (today `_async_update_options` merges options into data and reloads — reviewers will ask for a cleaner options flow or none at all).
- [ ] `test-before-configure` — config flow already validates credentials ✔ (verify all error paths map to `errors[...]`).
- [ ] `unique-config-entry` — ensure `async_set_unique_id` (account number/email) + `_abort_if_unique_id_configured`.
- [ ] `test-before-setup` — first refresh in `async_setup_entry` must raise `ConfigEntryNotReady`/`ConfigEntryAuthFailed` appropriately (`await coordinator.async_config_entry_first_refresh()`).
- [ ] `runtime-data` — already uses `entry.runtime_data` with typed `OctopusSpainConfigEntry` ✔.
- [ ] `action-setup` — **move** `_async_register_services` from `async_setup_entry` to `async_setup`, validate the target config entry is loaded and raise `ServiceValidationError` otherwise. (Or defer the whole service to a follow-up PR — recommended.)
- [ ] `appropriate-polling` — hourly polling ✔; be ready to justify the interval in review.
- [ ] `entity-unique-id` / `has-entity-name` — audit `sensor.py`: every entity `_attr_has_entity_name = True`, unique IDs based on account id, add `DeviceInfo` grouping entities per account.
- [ ] `entity-event-setup`, `common-modules` (`coordinator.py` ✔, add `entity.py` base class if shared), `parallel-updates` set on platforms.
- [ ] Remove custom-component artifacts: `version` key from manifest, `hacs.json` (stays only in the HACS repo), the `importlib` sensor preload hack, the `www` directory creation.
- [ ] Fix manifest: `iot_class: cloud_polling`, `codeowners: ["@mandinger"]`, `requirements: ["octopus-spain-api==1.0.0"]`, add `quality_scale: bronze`, `integration_type: service` (or `hub`), keep `after_dependencies: ["recorder"]` only if statistics stay in the first PR (recommend deferring; precedent for external statistics injection: the core `opower` integration).
- [ ] Add `quality_scale.yaml` marking every Bronze rule `done`/`exempt` with reasons.
- [ ] Translations: keep only `strings.json` (English). Delete `es.json` from the core copy — Spanish arrives via Lokalise (translate.home-assistant.io) after merge, where you can contribute the translations yourself.

## Phase 3 — Transplant into a home-assistant/core fork and write core-style tests

- [ ] Fork `home-assistant/core`, set up the dev environment (VS Code devcontainer is the supported path; `script/setup` otherwise).
- [ ] Optionally bootstrap with `python -m script.scaffold integration` to generate the skeleton + config-flow test skeleton, then port code into `homeassistant/components/octopus_spain/`.
- [ ] Add the integration to `CODEOWNERS`, `requirements_all.txt`, etc. — all generated: run `python -m script.hassfest` and `python -m script.gen_requirements_all`.
- [ ] Write tests under `tests/components/octopus_spain/`:
  - `test_config_flow.py` — **100% coverage of config_flow.py is a hard gate** (all auth paths: credentials, API key, key-generation toggle, errors, duplicate abort).
  - `conftest.py` with a mocked library client fixture (`mock_octopus_client`) and `MockConfigEntry`.
  - `test_init.py` (setup/unload/auth-failure paths), `test_sensor.py` using **snapshot tests** (`syrupy`) — current reviewer expectation for entity platforms.
  - Port relevant cases from `tests/test_sensor_helpers.py`; API-level tests stay in the library repo.
- [ ] Local CI gate before pushing: `python -m script.hassfest`, `ruff check` / `ruff format`, `mypy` on the component, `pytest tests/components/octopus_spain --cov` (aim ≥ full config-flow coverage; overall coverage requirements per quality scale).

## Phase 4 — Satellite PRs (can go in parallel, before the core PR)

- [ ] **Brands PR** → `home-assistant/brands`: move `custom_components/octopus_spain_fork/brand/{icon.png,icon@2x.png,logo.png,logo@2x.png}` to `core_integrations/octopus_spain/` (verify current size/format rules: 256×256 icon, 512×512 @2x, PNG, trimmed). Bronze rule `brands`.
- [ ] **Documentation PR** → `home-assistant/home-assistant.io`: create `source/_integrations/octopus_spain.markdown` with required front matter (`ha_category: Energy`, `ha_release: <next version>`, `ha_iot_class: Cloud Polling`, `ha_config_flow: true`, `ha_codeowners`, `ha_domain`, `ha_quality_scale: bronze`, `ha_platforms: [sensor]`). Content must satisfy the Bronze `docs-*` rules: high-level description, prerequisites (API key vs credentials — reuse the README's auth explanation), step-by-step setup, every entity, provided actions, known limitations, removal instructions. English; translate the existing Spanish README content.

## Phase 5 — The core PR and review

- [ ] Open the PR against `home-assistant/core` `dev` branch, one integration, minimal scope. Fill the PR template completely; link the brands + docs PRs; check every box of the new-integration checklist honestly.
- [ ] Pass CI (hassfest, CLA bot, coverage, lint, mypy).
- [ ] Respond to review iterations promptly; keep the branch rebased on `dev` (long queue — expect weeks/months; unattended PRs get marked stale). Draft-mark while making requested changes, re-request review when done.
- [ ] After merge: integration ships in the next monthly release (`ha_release` in docs must match).

## Phase 6 — Post-merge follow-ups

- [ ] Add Spanish (and other) translations via Lokalise.
- [ ] Follow-up PRs, one feature each: `download_invoice` action (with `services.yaml` + docs), recorder external-statistics backfill, remaining sensors/entities from [FEATURES.md](FEATURES.md).
- [ ] Migrate HACS users: publish a final HACS release whose README announces the core integration; because the custom domain (`octopus_spain_fork`) differs from the core domain, users reconfigure — document the switch (custom integrations with the *same* domain would shadow core, another reason the rename matters). Then archive/deprecate the HACS repo, or keep it as a beta channel.
- [ ] Climb the quality scale: Silver (reauth flow — the API-key regeneration invalidates old keys, so reauth matters here; log-when-unavailable; entity availability), then Gold/Platinum. Track in `quality_scale.yaml`.

## Verification gates per phase

- **Library**: CI-published PyPI release + green tests in the library repo.
- **Core code**: `python -m script.hassfest` + `pytest tests/components/octopus_spain` green with 100% config-flow coverage.
- **PRs**: HA CI green + reviewer approval on all three PRs (core, brands, docs).

## Key references

- Quality scale + Bronze checklist: <https://developers.home-assistant.io/docs/core/integration-quality-scale/checklist>
- ADR-0004 (external libraries): <https://github.com/home-assistant/architecture/blob/master/adr/0004-webscraping-and-published-packages.md>
- ADR-0010 (config flow required): <https://github.com/home-assistant/architecture/blob/master/adr/0010-integration-configuration.md>
- Submitting work / review process: <https://developers.home-assistant.io/docs/development_submitting>
- Brands repo: <https://github.com/home-assistant/brands>
- Docs repo: <https://github.com/home-assistant/home-assistant.io>
