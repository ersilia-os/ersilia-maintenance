# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-06-08T11:40:36Z

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
| eos9bpi | antimicrobial-activity-enterobacter | ✅ | 2026-06-08T11:48:56Z |
| eos9eyo | antimicrobial-activity-hpylori | ✅ | 2026-06-08T11:56:08Z |
| eos6pbf | selfies | ✅ | 2026-06-08T11:59:57Z |
| eos74km | antimicrobial-kg-ml | ✅ | 2026-06-08T12:05:21Z |
| eos77jk | cc-signaturizer-3d-d | ✅ | 2026-06-08T12:11:50Z |
| eos77w8 | grover-sider | 🚨 | 2026-06-08T12:19:31Z |
| eos78ao | mordred | ✅ | 2026-06-08T12:24:42Z |
| eos7a45 | coprinet-molecule-price | 🚨 | 2026-06-08T12:33:38Z |
| eos12x7 | spacial-score-complexity | ✅ | 2026-06-08T12:37:44Z |
| eos43at | molgrad-herg | ✅ | 2026-06-08T12:42:30Z |
