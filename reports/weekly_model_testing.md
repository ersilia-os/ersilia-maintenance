# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-10-26T10:14:13Z

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
| eos531m | hlm-half-life | ✅ | 2026-10-26T10:18:30Z |
| eos7s53 | mtbaim | ✅ | 2026-10-26T10:25:43Z |
| eos80sj | annalog | ✅ | 2026-10-26T10:36:39Z |
| eos8nyg | reference-library-similarity | ✅ | 2026-10-26T10:41:02Z |
| eos4u6p | cc-signaturizer | ✅ | 2026-10-26T10:49:55Z |
| eos42ez | antibiotics-ai-cytotox | ✅ | 2026-10-26T11:00:27Z |
| eos4e40 | chemprop-antibiotic | ✅ | 2026-10-26T11:06:20Z |
| eos9zw0 | molpmofit | ✅ | 2026-10-26T11:13:52Z |
| eos5pt8 | druglikeness-unsupervised | ✅ | 2026-10-26T11:19:32Z |
| eos5smc | grover-tox21 | ✅ | 2026-10-26T11:26:42Z |
