# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-03-31T09:25:14Z

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
| eos6hy3 | image-mol-hiv | ✅ | 2026-03-31T09:30:58Z |
| eos9li5 | biosynfoni | ✅ | 2026-03-31T09:35:28Z |
| eos157v | grover-freesolv | ✅ | 2026-03-31T09:44:00Z |
| eos1af5 | molgrad-caco2 | ✅ | 2026-03-31T09:48:41Z |
| eos1amr | grover-bbbp | ✅ | 2026-03-31T09:56:58Z |
| eos1pu1 | cardiotox-dictrank | ✅ | 2026-03-31T10:03:34Z |
| eos2b6f | pkasolver | ✅ | 2026-03-31T10:10:52Z |
| eos2fy6 | s2dv-hepg2-toxicity | ✅ | 2026-03-31T10:15:00Z |
| eos2lqb | hob-pre | ✅ | 2026-03-31T10:19:44Z |
| eos2mhp | grover-bace | ✅ | 2026-03-31T10:27:56Z |
