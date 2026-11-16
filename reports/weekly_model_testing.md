# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-11-16T10:08:43Z

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
| eos8698 | enamine-real-similarity | ✅ | 2026-11-16T10:18:37Z |
| eos9b1c | molport-similarity | ✅ | 2026-11-16T10:24:20Z |
| eos4an7 | antimicrobial-activity-pfalciparum | ✅ | 2026-11-16T10:41:28Z |
| eos5eya | antimicrobial-activity-ecoli | ✅ | 2026-11-16T10:50:30Z |
| eos5q52 | antimicrobial-activity-spneumoniae | ✅ | 2026-11-16T10:58:22Z |
| eos5qya | antimicrobial-activity-ngonorrhoeae | ✅ | 2026-11-16T11:05:18Z |
| eos6wb7 | antimicrobial-activity-kpneumoniae | ✅ | 2026-11-16T11:13:33Z |
| eos81zy | antimicrobial-activity-efaecium | ✅ | 2026-11-16T11:21:19Z |
| eos8lcw | antimicrobial-activity-saureus | ✅ | 2026-11-16T11:31:27Z |
| eos8v1a | antimicrobial-activity-smansoni | ✅ | 2026-11-16T11:38:33Z |
