# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2025-12-12T09:44:43Z

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
| eos24jm | qcrb-tb | ✅ | 2025-12-12T09:47:42Z |
| eos2a9n | chembl-similarity | 🚨 | 2025-12-12T09:54:36Z |
| eos2b6f | pkasolver | ✅ | 2025-12-12T10:00:46Z |
| eos2db3 | chemical-space-projections-chemdiv | ✅ | 2025-12-12T10:11:24Z |
| eos2fy6 | s2dv-hepg2-toxicity | ✅ | 2025-12-12T10:15:04Z |
| eos2gth | maip-malaria-surrogate | ✅ | 2025-12-12T10:19:08Z |
| eos2gw4 | ersilia-compound-embedding | ✅ | 2025-12-12T10:22:06Z |
| eos2h1r | cc-signaturizer-3d-c | ✅ | 2025-12-12T10:31:14Z |
| eos2hbd | passive-permeability | 🚨 | 2025-12-12T10:31:18Z |
| eos2hzy | pubchem-sampler | 🚨 | 2025-12-12T10:34:21Z |
