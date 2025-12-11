# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2025-12-11T15:17:39Z

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
| eos11sm | known-antibiotic-ressemblance | ✅ | 2025-12-11T15:20:39Z |
| eos11sr | emfps | ✅ | 2025-12-11T15:23:58Z |
| eos157v | grover-freesolv | ✅ | 2025-12-11T15:30:47Z |
| eos18ie | antibiotics-ai-saureus | ✅ | 2025-12-11T15:41:31Z |
| eos19mt | chebifier-antibiotic | 🚨 | 2025-12-11T15:50:09Z |
| eos1af5 | molgrad-caco2 | ✅ | 2025-12-11T15:53:45Z |
| eos1amr | grover-bbbp | ✅ | 2025-12-11T16:00:22Z |
| eos1d7r | small-world-zinc | 🚨 | 2025-12-11T16:04:13Z |
| eos1lb5 | mycobacterium-permeability | ✅ | 2025-12-11T16:11:41Z |
| eos1mxi | smiles-pe | ✅ | 2025-12-11T16:14:20Z |
