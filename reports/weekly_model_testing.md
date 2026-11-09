# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-11-09T10:09:18Z

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
| eos6fza | grover-clintox | ✅ | 2026-11-09T10:15:25Z |
| eos21dr | antimicrobial-activity-abaumannii | ✅ | 2026-11-09T10:27:55Z |
| eos3dys | coadd-antimicrobial-activity | ✅ | 2026-11-09T10:40:02Z |
| eos6m4j | bidd-molmap-desc | ✅ | 2026-11-09T10:47:32Z |
| eos6ojg | antibioticdb-similarity-matches | ✅ | 2026-11-09T10:51:19Z |
| eos6oli | soltrannet-aqueous-solubility | ✅ | 2026-11-09T10:57:17Z |
| eos7iak | antimicrobial-activity-campylobacter | ✅ | 2026-11-09T11:06:11Z |
| eos817d | hyper-dimensional-fingerprints | ✅ | 2026-11-09T11:09:34Z |
| eos8jx6 | antimicrobial-activity-calbicans | ✅ | 2026-11-09T11:25:34Z |
| eos43d6 | antimicrobial-activity-mtuberculosis | 🚨 | 2026-11-09T11:33:02Z |
