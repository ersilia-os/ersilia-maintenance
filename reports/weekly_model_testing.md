# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-09-28T10:11:30Z

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
| eos481p | grover-toxcast | ✅ | 2026-09-28T10:19:21Z |
| eos4cxk | image-mol-sars-cov2 | ✅ | 2026-09-28T10:23:52Z |
| eos4djh | datamol-basic-descriptors | ✅ | 2026-09-28T10:28:02Z |
| eos3kcw | small-world-wuxi | ✅ | 2026-09-28T10:35:57Z |
| eos4b8j | gdbchembl-similarity | ✅ | 2026-09-28T10:39:45Z |
| eos4ex3 | mole-representations | ✅ | 2026-09-28T10:45:50Z |
| eos4f95 | mycetos | 🚨 | 2026-09-28T10:51:08Z |
| eos4jcv | cc-signaturizer-3d-e | ✅ | 2026-09-28T10:57:19Z |
| eos4q1a | crem-structure-generation | ✅ | 2026-09-28T11:03:35Z |
| eos4r1g | entry-classifier | 🚨 | 2026-09-28T11:08:21Z |
