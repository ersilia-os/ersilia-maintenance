# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-02-24T13:11:05Z

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
| eos65rt | deepfl-logp | ✅ | 2026-02-24T13:18:03Z |
| eos74bo | ncats-solubility | ✅ | 2026-02-24T13:24:16Z |
| eos96f4 | digitization-complexity | ✅ | 2026-02-24T13:30:00Z |
| eos9n1s | hemozoin-inhibition-physchem | ✅ | 2026-02-24T13:33:43Z |
| eos9taz | moler-enamine-fragments | ✅ | 2026-02-24T13:53:06Z |
| eos9tyg | ncats-pampa74 | ✅ | 2026-02-24T13:57:27Z |
| eos9ueu | small-world-enamine-real | 🚨 | 2026-02-24T13:59:37Z |
| eos9x3z | gram-negative-permeability-proxy | ✅ | 2026-02-24T14:14:45Z |
| eos9ym3 | mrlogp | ✅ | 2026-02-24T14:23:10Z |
| eos9yui | natural-product-likeness | ✅ | 2026-02-24T14:28:39Z |
