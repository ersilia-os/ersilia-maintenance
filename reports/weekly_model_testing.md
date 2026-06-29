# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-06-29T11:43:11Z

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
| eos8451 | grover-esol | 🚨 | 2026-06-29T11:51:30Z |
| eos85a3 | grover-lipo | 🚨 | 2026-06-29T11:59:13Z |
| eos8a4x | rdkit-descriptors | ✅ | 2026-06-29T12:03:05Z |
| eos8a5g | molbloom | ✅ | 2026-06-29T12:06:51Z |
| eos8aa5 | kgpgt-embedding | ✅ | 2026-06-29T12:13:33Z |
| eos8d8a | mycpermcheck | ✅ | 2026-06-29T12:21:26Z |
| eos8fma | stoned-sampler | ✅ | 2026-06-29T12:29:41Z |
| eos8fth | redial-2020 | ✅ | 2026-06-29T12:36:07Z |
| eos8h6g | avalon | ✅ | 2026-06-29T12:39:54Z |
| eos8ioa | natural-product-score | 🚨 | 2026-06-29T12:43:50Z |
