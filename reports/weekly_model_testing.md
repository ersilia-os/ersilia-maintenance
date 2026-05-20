# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-05-20T08:00:16Z

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
| eos5nqn | gneprop-ecoli | 🚨 | 2026-05-20T08:11:12Z |
| eos5pt8 | druglikeness-unsupervised | ✅ | 2026-05-20T08:19:16Z |
| eos5smc | grover-tox21 | ✅ | 2026-05-20T08:27:33Z |
| eos5xng | chemprop-burkholderia | ✅ | 2026-05-20T08:36:33Z |
| eos4avb | image-mol-embeddings | ✅ | 2026-05-20T08:40:20Z |
| eos694w | reinvent4-mol2mol-medium-similarity | ✅ | 2026-05-20T09:02:47Z |
| eos69p9 | ssl-gcn-tox21 | 🚨 | 2026-05-20T09:09:29Z |
| eos6ao8 | molgrad-ppb | ✅ | 2026-05-20T09:13:48Z |
| eos6aun | rxn-fingerprint | ✅ | 2026-05-20T09:20:42Z |
| eos6fza | grover-clintox | 🚨 | 2026-05-20T09:28:51Z |
