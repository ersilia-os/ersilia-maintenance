# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-02-09T10:28:17Z

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
| eos8a5g | molbloom | ✅ | 2026-02-09T10:31:42Z |
| eos8aa5 | kgpgt-embedding | ✅ | 2026-02-09T10:40:40Z |
| eos8d8a | mycpermcheck | ✅ | 2026-02-09T10:48:36Z |
| eos8fma | stoned-sampler | ✅ | 2026-02-09T10:56:37Z |
| eos8fth | redial-2020 | ✅ | 2026-02-09T11:05:54Z |
| eos8g50 | fastsolv | 🚨 | 2026-02-09T11:11:07Z |
| eos8h6g | avalon | ✅ | 2026-02-09T11:14:51Z |
| eos8ioa | natural-product-score | ✅ | 2026-02-09T11:18:29Z |
| eos8lok | s2dv-hbv | ✅ | 2026-02-09T11:22:56Z |
| eos8ub5 | chemical-space-projections-coconut | 🚨 | 2026-02-09T11:30:40Z |
