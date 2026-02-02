# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-02-02T11:55:00Z

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
| eos7qga | datamol-smiles2canonical | ✅ | 2026-02-02T11:57:25Z |
| eos7w6n | grover-embedding | ✅ | 2026-02-02T12:01:24Z |
| eos7ye0 | chemfh | ✅ | 2026-02-02T12:09:43Z |
| eos7yti | osm-series4 | ✅ | 2026-02-02T12:14:59Z |
| eos80ch | malaria-mam | ✅ | 2026-02-02T12:17:31Z |
| eos81ew | ncats-pampa5 | ✅ | 2026-02-02T12:20:29Z |
| eos82v1 | smi-ted | ✅ | 2026-02-02T12:26:49Z |
| eos8451 | grover-esol | ✅ | 2026-02-02T12:33:01Z |
| eos85a3 | grover-lipo | ✅ | 2026-02-02T12:38:40Z |
| eos8a4x | rdkit-descriptors | ✅ | 2026-02-02T12:40:52Z |
