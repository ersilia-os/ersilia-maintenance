# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-04-20T10:38:37Z

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
| eos7asg | padel | 🚨 | 2026-04-20T10:45:22Z |
| eos7d58 | admet-ai-percentile | ✅ | 2026-04-20T10:53:21Z |
| eos3zur | molfeat-estate | ✅ | 2026-04-20T11:00:46Z |
| eos42ez | antibiotics-ai-cytotox | 🚨 | 2026-04-20T11:11:14Z |
| eos46ev | chemtb | ✅ | 2026-04-20T11:18:40Z |
| eos481p | grover-toxcast | ✅ | 2026-04-20T11:27:22Z |
| eos4b8j | gdbchembl-similarity | 🚨 | 2026-04-20T11:32:13Z |
| eos4cxk | image-mol-sars-cov2 | ✅ | 2026-04-20T11:40:04Z |
| eos4djh | datamol-basic-descriptors | ✅ | 2026-04-20T11:45:19Z |
| eos4e40 | chemprop-antibiotic | 🚨 | 2026-04-20T11:49:45Z |
