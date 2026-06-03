# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-06-01T12:02:20Z

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
| eos2e3s | antimicrobial-activity-paeruginosa | 🚨 | 2026-06-01T12:12:51Z |
| eos43d6 | antimicrobial-activity-mtuberculosis | ✅ | 2026-06-01T12:25:14Z |
| eos4an7 | antimicrobial-activity-pfalciparum | ✅ | 2026-06-01T12:41:29Z |
| eos5eya | antimicrobial-activity-ecoli | ✅ | 2026-06-01T12:50:15Z |
| eos5q52 | antimicrobial-activity-spneumoniae | ✅ | 2026-06-01T12:57:57Z |
| eos5qya | antimicrobial-activity-ngonorrhoeae | ✅ | 2026-06-01T13:04:29Z |
| eos6wb7 | antimicrobial-activity-kpneumoniae | ✅ | 2026-06-01T13:11:31Z |
| eos81zy | antimicrobial-activity-efaecium | ✅ | 2026-06-01T13:18:10Z |
| eos8lcw | antimicrobial-activity-saureus | ✅ | 2026-06-01T13:30:37Z |
| eos8v1a | antimicrobial-activity-smansoni | ✅ | 2026-06-01T13:37:24Z |
