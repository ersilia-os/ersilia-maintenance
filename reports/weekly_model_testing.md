# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-09-07T10:10:03Z

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
| eos55vx | cocograph-formula | ✅ | 2026-09-07T13:17:55Z |
| eos2b6f | pkasolver | ✅ | 2026-09-07T13:24:12Z |
| eos2fy6 | s2dv-hepg2-toxicity | ✅ | 2026-09-07T13:27:30Z |
| eos2hzy | pubchem-sampler | 🚨 | 2026-09-07T13:30:58Z |
| eos2lqb | hob-pre | ✅ | 2026-09-07T13:34:51Z |
| eos2mhp | grover-bace | ✅ | 2026-09-07T13:42:06Z |
| eos2zmb | hdac1-inhibition | ✅ | 2026-09-07T13:50:12Z |
| eos30f3 | dmpnn-herg | ✅ | 2026-09-07T13:56:29Z |
| eos30gr | deepherg | ✅ | 2026-09-07T14:02:45Z |
| eos31ve | ncats-hlm | ✅ | 2026-09-07T14:06:57Z |
