# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-05-25T11:25:37Z

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
| eos21dr | antimicrobial-activity-abaumannii | ✅ | 2026-05-25T11:33:47Z |
| eos3dys | coadd-antimicrobial-activity | ✅ | 2026-05-25T11:44:01Z |
| eos7iak | antimicrobial-activity-campylobacter | ✅ | 2026-05-25T11:50:45Z |
| eos817d | hyper-dimensional-fingerprints | ✅ | 2026-05-25T11:55:50Z |
| eos8jx6 | antimicrobial-activity-calbicans | ✅ | 2026-05-25T12:04:36Z |
| eos6m2k | mole-antimicrobial | 🚨 | 2026-05-25T12:11:10Z |
| eos6m4j | bidd-molmap-desc | ✅ | 2026-05-25T12:20:02Z |
| eos6o0z | grover-qm7 | 🚨 | 2026-05-25T12:27:44Z |
| eos6ojg | antibioticdb-similarity-matches | ✅ | 2026-05-25T12:32:57Z |
| eos6oli | soltrannet-aqueous-solubility | ✅ | 2026-05-25T12:39:20Z |
