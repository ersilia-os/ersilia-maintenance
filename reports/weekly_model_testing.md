# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-03-16T10:26:53Z

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
| eos5gge | dili-predictor | ✅ | 2026-03-16T10:33:56Z |
| eos9cvt | permeability-efflux-mtl | ✅ | 2026-03-16T10:42:06Z |
| eos2lm8 | smiles-transformer | ✅ | 2026-03-16T10:45:49Z |
| eos2mrz | deepsmiles | ✅ | 2026-03-16T10:49:15Z |
| eos2mxh | cc-signaturizer-3d-b | ✅ | 2026-03-16T10:59:24Z |
| eos2r5a | retrosynthetic-accessibility | ✅ | 2026-03-16T11:03:56Z |
| eos2rd8 | molt5-smiles-to-caption | ✅ | 2026-03-16T11:24:39Z |
| eos2sbn | cc-signaturizer-3d-a | ✅ | 2026-03-16T11:34:46Z |
| eos2thm | molbert | ✅ | 2026-03-16T11:44:27Z |
| eos2xeq | antibiotics-downselection | ✅ | 2026-03-16T11:49:09Z |
