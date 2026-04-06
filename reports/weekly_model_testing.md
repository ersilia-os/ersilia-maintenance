# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-04-06T10:28:54Z

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
| eos2zmb | hdac1-inhibition | ✅ | 2026-04-06T10:38:10Z |
| eos30f3 | dmpnn-herg | ✅ | 2026-04-06T10:44:56Z |
| eos30gr | deepherg | ✅ | 2026-04-06T10:52:25Z |
| eos31ve | ncats-hlm | ✅ | 2026-04-06T10:57:23Z |
| eos3804 | chemprop-abaumannii | ✅ | 2026-04-06T11:04:00Z |
| eos39co | unimol-representation | ✅ | 2026-04-06T11:10:50Z |
| eos39dp | phakinpro | ✅ | 2026-04-06T11:17:08Z |
| eos3ae6 | whales-descriptor | ✅ | 2026-04-06T11:22:25Z |
| eos3b5e | molecular-weight | ✅ | 2026-04-06T11:27:17Z |
| eos3e6s | chembl-decoys | 🚨 | 2026-04-06T11:34:58Z |
