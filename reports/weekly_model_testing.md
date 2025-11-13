# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2025-11-13T08:36:46Z

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
| eos21q7 | inter-dili | ✅ | 2025-11-13T08:38:48Z |
| eos22io | idl-ppbopt | ✅ | 2025-11-13T08:43:25Z |
| eos238c | mesh-therapeutic-use | 🚨 | 2025-11-13T08:51:49Z |
| eos2401 | scaffold-decoration | ✅ | 2025-11-13T09:14:04Z |
| eos24jm | qcrb-tb | ✅ | 2025-11-13T09:16:47Z |
| eos24ur | whales-scaled | 🚨 | 2025-11-13T09:22:17Z |
