# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2025-11-18T13:50:31Z

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
| eos157v | grover-freesolv | ✅ | 2025-11-18T13:57:24Z |
| eos18ie | antibiotics-ai-saureus | ✅ | 2025-11-18T14:08:04Z |
| eos1af5 | molgrad-caco2 | ✅ | 2025-11-18T14:11:35Z |
