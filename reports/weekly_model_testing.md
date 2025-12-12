# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2025-12-12T13:16:24Z

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
| eos2thm | molbert | ✅ | 2025-12-12T13:24:41Z |
| eos2xeq | antibiotics-downselection | ✅ | 2025-12-12T13:27:39Z |
| eos2zmb | hdac1-inhibition | ✅ | 2025-12-12T13:35:10Z |
| eos30f3 | dmpnn-herg | ✅ | 2025-12-12T13:41:00Z |
| eos30gr | deepherg | ✅ | 2025-12-12T13:46:41Z |
| eos31ve | ncats-hlm | ✅ | 2025-12-12T13:50:45Z |
| eos3804 | chemprop-abaumannii | ✅ | 2025-12-12T13:56:30Z |
| eos39co | unimol-representation | ✅ | 2025-12-12T14:02:38Z |
| eos39dp | phakinpro | ✅ | 2025-12-12T14:07:03Z |
| eos3ae6 | whales-descriptor | ✅ | 2025-12-12T14:10:29Z |
