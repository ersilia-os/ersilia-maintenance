# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-06-22T12:03:47Z

This report summarizes the results of the **weekly shallow tests** run with the `ersilia` CLI on the selected repositories from `picked_weekly.json`.

Each model has been tested using:

```bash
ersilia fetch <repository_name> --from_github
ersilia test <repository_name> --shallow --from_github
```

### 📋 Status Legend
- ✅ **Passed:** All checks completed successfully.
- 🚨 **Failed:** One or more checks failed, or the test did not complete.

🔎 For detailed test outputs, see the file: `reports/weekly_test_summary.txt`.

---

### 📊 Test Results

| 🧬 repository_name | 🪪 slug | 🧭 test | ⏰ test_date |
|--------------------|---------|---------|--------------|
| eos7l5m | efflux-gram-negative | 🚨 | 2026-06-22T12:11:45Z |
| eos7m30 | admet-ai-exact | 🚨 | 2026-06-22T12:18:53Z |
| eos7pw8 | syba-synthetic-accessibility | ✅ | 2026-06-22T12:38:52Z |
| eos7qga | datamol-smiles2canonical | ✅ | 2026-06-22T12:42:50Z |
| eos7w6n | grover-embedding | ✅ | 2026-06-22T12:48:42Z |
| eos7ye0 | chemfh | 🚨 | 2026-06-22T12:54:18Z |
| eos7yti | osm-series4 | ✅ | 2026-06-22T13:03:10Z |
| eos80ch | malaria-mam | ✅ | 2026-06-22T13:07:36Z |
| eos81ew | ncats-pampa5 | 🚨 | 2026-06-22T13:12:23Z |
| eos82v1 | smi-ted | ✅ | 2026-06-22T13:20:16Z |
