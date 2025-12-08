# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2025-12-08T10:09:24Z

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
| eos2ta5 | cardiotoxnet-herg | ✅ | 2025-12-08T10:15:06Z |
| eos2thm | molbert | ✅ | 2025-12-08T10:24:30Z |
| eos2xeq | antibiotics-downselection | ✅ | 2025-12-08T10:27:19Z |
| eos2zmb | hdac1-inhibition | ✅ | 2025-12-08T10:35:20Z |
| eos30f3 | dmpnn-herg | ✅ | 2025-12-08T10:41:32Z |
| eos30gr | deepherg | ✅ | 2025-12-08T10:47:10Z |
| eos31ve | ncats-hlm | ✅ | 2025-12-08T10:52:08Z |
| eos37l0 | chembl-kpneumoniae | ✅ | 2025-12-08T10:58:10Z |
| eos39co | unimol-representation | ✅ | 2025-12-08T11:04:17Z |
| eos39dp | phakinpro | ✅ | 2025-12-08T11:08:40Z |
