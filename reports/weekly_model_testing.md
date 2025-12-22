# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2025-12-22T10:09:20Z

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
| eos1soi | non-growing-antimicrobial | ✅ | 2025-12-22T10:17:38Z |
| eos3lyd | efflux-pump-avoidance-gram-negative | ✅ | 2025-12-22T10:22:33Z |
| eos3xip | grover-qm8 | ✅ | 2025-12-22T10:30:13Z |
| eos3zur | molfeat-estate | ✅ | 2025-12-22T10:36:40Z |
| eos42ez | antibiotics-ai-cytotox | ✅ | 2025-12-22T10:51:14Z |
| eos46ev | chemtb | ✅ | 2025-12-22T10:57:05Z |
| eos481p | grover-toxcast | ✅ | 2025-12-22T11:04:38Z |
| eos4b8j | gdbchembl-similarity | ✅ | 2025-12-22T11:08:02Z |
| eos4cxk | image-mol-sars-cov2 | ✅ | 2025-12-22T11:14:42Z |
| eos4djh | datamol-basic-descriptors | ✅ | 2025-12-22T11:17:52Z |
