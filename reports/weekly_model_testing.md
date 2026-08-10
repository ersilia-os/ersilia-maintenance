# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-08-10T10:32:27Z

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
| eos9ueu | small-world-enamine-real | ✅ | 2026-08-10T10:41:53Z |
| eos1vms | chembl-multitask-descriptor | ✅ | 2026-08-10T10:47:21Z |
| eos21q7 | inter-dili | 🚨 | 2026-08-10T10:57:53Z |
| eos22io | idl-ppbopt | ✅ | 2026-08-10T11:05:01Z |
| eos24ci | drugtax | ✅ | 2026-08-10T11:10:03Z |
| eos24jm | qcrb-tb | ✅ | 2026-08-10T11:15:21Z |
| eos2db3 | chemical-space-projections-chemdiv | ✅ | 2026-08-10T11:29:27Z |
| eos2gth | maip-malaria-surrogate | ✅ | 2026-08-10T11:35:07Z |
| eos2gw4 | ersilia-compound-embedding | ✅ | 2026-08-10T11:40:14Z |
| eos2h1r | cc-signaturizer-3d-c | ✅ | 2026-08-10T11:47:53Z |
