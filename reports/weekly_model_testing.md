# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2025-12-15T10:10:19Z

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
| eos3b5e | molecular-weight | ✅ | 2025-12-15T10:13:01Z |
| eos3e6s | chembl-decoys | ✅ | 2025-12-15T10:18:46Z |
| eos3ev6 | ncats-cyp3a4 | 🚨 | 2025-12-15T10:18:50Z |
| eos3kcw | small-world-wuxi | 🚨 | 2025-12-15T10:21:11Z |
| eos3l5f | clamp | ✅ | 2025-12-15T10:31:17Z |
| eos3le9 | hepg2-mmv | ✅ | 2025-12-15T10:38:19Z |
| eos3mk2 | bbbp-marine-kinase-inhibitors | ✅ | 2025-12-15T10:41:47Z |
| eos3nn9 | mpro-covid19 | ✅ | 2025-12-15T10:45:34Z |
| eos3ujl | mtb-permeability | ✅ | 2025-12-15T10:49:12Z |
| eos3wzy | qupkake | ✅ | 2025-12-15T11:02:03Z |
