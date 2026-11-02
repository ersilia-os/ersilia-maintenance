# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-11-02T10:10:20Z

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
| eos1bgt | coconut-similarity | ✅ | 2026-11-02T10:14:59Z |
| eos3pu0 | liquid-stock-similarity | ✅ | 2026-11-02T10:20:18Z |
| eos80al | hit-locator-similarity | ✅ | 2026-11-02T10:24:37Z |
| eos8bpb | ecoli-permeation-efflux | ✅ | 2026-11-02T10:30:09Z |
| eos5xng | chemprop-burkholderia | ✅ | 2026-11-02T10:38:01Z |
| eos694w | reinvent4-mol2mol-medium-similarity | ✅ | 2026-11-02T11:35:57Z |
| eos6ao8 | molgrad-ppb | ✅ | 2026-11-02T11:40:08Z |
| eos6aun | rxn-fingerprint | ✅ | 2026-11-02T11:46:41Z |
| eos69p9 | ssl-gcn-tox21 | ✅ | 2026-11-02T11:52:48Z |
| eos5nqn | gneprop-ecoli | 🚨 | 2026-11-02T11:57:33Z |
