# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-03-02T13:45:26Z

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
| eos9zw0 | molpmofit | 🚨 | 2026-03-02T13:48:41Z |
| eos1d7r | small-world-zinc | 🚨 | 2026-03-02T13:52:16Z |
| eos1mxi | smiles-pe | 🚨 | 2026-03-02T13:54:42Z |
| eos1noy | chembl-sampler | 🚨 | 2026-03-02T13:57:40Z |
