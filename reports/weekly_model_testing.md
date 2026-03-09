# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-03-09T10:23:39Z

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
| eos1vms | chembl-multitask-descriptor | 🚨 | 2026-03-09T10:28:59Z |
| eos21q7 | inter-dili | ✅ | 2026-03-09T10:37:32Z |
| eos22io | idl-ppbopt | ✅ | 2026-03-09T10:43:58Z |
| eos24ci | drugtax | ✅ | 2026-03-09T10:48:12Z |
| eos24jm | qcrb-tb | ✅ | 2026-03-09T10:52:08Z |
| eos2db3 | chemical-space-projections-chemdiv | 🚨 | 2026-03-09T10:59:16Z |
| eos2gth | maip-malaria-surrogate | ✅ | 2026-03-09T11:04:34Z |
| eos2gw4 | ersilia-compound-embedding | ✅ | 2026-03-09T11:09:24Z |
| eos2h1r | cc-signaturizer-3d-c | ✅ | 2026-03-09T11:20:53Z |
| eos2l0q | schisto-swisstph | ✅ | 2026-03-09T11:29:27Z |
