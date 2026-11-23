# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-11-23T10:08:51Z

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
| eos12x7 | spacial-score-complexity | ✅ | 2026-11-23T10:12:05Z |
| eos43at | molgrad-herg | ✅ | 2026-11-23T10:16:23Z |
| eos6pbf | selfies | ✅ | 2026-11-23T10:19:30Z |
| eos77jk | cc-signaturizer-3d-d | ✅ | 2026-11-23T10:25:32Z |
| eos78ao | mordred | ✅ | 2026-11-23T10:29:41Z |
| eos9bpi | antimicrobial-activity-enterobacter | ✅ | 2026-11-23T10:39:55Z |
| eos9eyo | antimicrobial-activity-hpylori | ✅ | 2026-11-23T10:49:20Z |
| eos2egp | chelating-groups | ✅ | 2026-11-23T10:52:39Z |
| eos4k4f | standardization | ✅ | 2026-11-23T10:56:18Z |
| eos5f0j | checkmol-functional-groups | ✅ | 2026-11-23T10:59:34Z |
