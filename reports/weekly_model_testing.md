# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2025-12-12T12:20:33Z

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
| eos2l0q | schisto-swisstph | ✅ | 2025-12-12T12:28:06Z |
| eos2lm8 | smiles-transformer | ✅ | 2025-12-12T12:31:14Z |
| eos2lqb | hob-pre | ✅ | 2025-12-12T12:34:45Z |
| eos2mhp | grover-bace | ✅ | 2025-12-12T12:41:26Z |
| eos2mrz | deepsmiles | ✅ | 2025-12-12T12:43:51Z |
| eos2mxh | cc-signaturizer-3d-b | ✅ | 2025-12-12T12:51:31Z |
| eos2r5a | retrosynthetic-accessibility | ✅ | 2025-12-12T12:55:05Z |
| eos2rd8 | molt5-smiles-to-caption | 🚨 | 2025-12-12T12:55:09Z |
| eos2sbn | cc-signaturizer-3d-a | ✅ | 2025-12-12T13:02:55Z |
| eos2ta5 | cardiotoxnet-herg | ✅ | 2025-12-12T13:07:43Z |
