# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2025-11-24T10:10:33Z

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
| eos2401 | scaffold-decoration | ✅ | 2025-11-24T10:50:39Z |
| eos24jm | qcrb-tb | ✅ | 2025-11-24T10:53:31Z |
| eos24ur | whales-scaled | 🚨 | 2025-11-24T10:56:45Z |
| eos2db3 | chemical-space-projections-chemdiv | ✅ | 2025-11-24T11:06:24Z |
| eos2gth | maip-malaria-surrogate | ✅ | 2025-11-24T11:10:24Z |
| eos2gw4 | ersilia-compound-embedding | ✅ | 2025-11-24T11:13:12Z |
| eos2h1r | cc-signaturizer-3d-c | ✅ | 2025-11-24T11:20:34Z |
| eos2hbd | passive-permeability | ✅ | 2025-11-24T11:28:25Z |
| eos2l0q | schisto-swisstph | ✅ | 2025-11-24T11:35:09Z |
| eos2lm8 | smiles-transformer | ✅ | 2025-11-24T11:38:01Z |
