# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-08-03T11:07:40Z

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
| eos9yui | natural-product-likeness | ✅ | 2026-08-03T11:14:15Z |
| eos11sm | known-antibiotic-resemblance | ✅ | 2026-08-03T11:19:41Z |
| eos18ie | antibiotics-ai-saureus | 🚨 | 2026-08-03T11:28:35Z |
| eos1lb5 | mycobacterium-permeability | 🚨 | 2026-08-03T11:35:24Z |
| eos9yy1 | ncats-hlcs | 🚨 | 2026-08-03T11:41:51Z |
| eos1n4b | hdac3-inhibition | ✅ | 2026-08-03T11:48:05Z |
| eos1ut3 | molfeat-usrcat | ✅ | 2026-08-03T11:56:23Z |
| eos1d7r | small-world-zinc | ✅ | 2026-08-03T12:05:46Z |
| eos1mxi | smiles-pe | ✅ | 2026-08-03T12:10:53Z |
| eos1noy | chembl-sampler | ✅ | 2026-08-03T12:15:43Z |
