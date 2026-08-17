# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-08-17T10:13:34Z

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
| eos19dk | molcompass | ✅ | 2026-08-17T10:18:45Z |
| eos3f8h | eu-openscreen-hts | ✅ | 2026-08-17T10:36:10Z |
| eos5g6m | glacier-embeddings | ✅ | 2026-08-17T10:43:57Z |
| eos5mnx | sand-shape-descriptor | ✅ | 2026-08-17T10:50:27Z |
| eos69e6 | pgmg-pharmacophore | ✅ | 2026-08-17T11:46:11Z |
| eos6pj2 | nafm-embeddings | ✅ | 2026-08-17T11:52:40Z |
| eos84nf | genmol-scaffold-decoration | ✅ | 2026-08-17T13:57:29Z |
| eos8zvb | pymolgen | ✅ | 2026-08-17T14:03:53Z |
| eos6ost | reinvent4-libinvent | ✅ | 2026-08-17T14:37:34Z |
| eos2l0q | schisto-swisstph | 🚨 | 2026-08-17T14:47:45Z |
