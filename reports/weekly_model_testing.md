# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-07-27T11:06:45Z

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
| eos65rt | deepfl-logp | ✅ | 2026-07-27T11:13:41Z |
| eos74bo | ncats-solubility | ✅ | 2026-07-27T11:19:46Z |
| eos8ub5 | chemical-space-projections-coconut | ✅ | 2026-07-27T11:35:37Z |
| eos96f4 | digitization-complexity | ✅ | 2026-07-27T11:43:09Z |
| eos9gg2 | chemical-space-projections-drugbank | ✅ | 2026-07-27T11:51:50Z |
| eos9n1s | hemozoin-inhibition-physchem | ✅ | 2026-07-27T11:57:03Z |
| eos9taz | moler-enamine-fragments | ✅ | 2026-07-27T12:19:06Z |
| eos9tyg | ncats-pampa74 | 🚨 | 2026-07-27T12:25:03Z |
| eos9x3z | gram-negative-permeability-proxy | ✅ | 2026-07-27T12:34:17Z |
| eos9ym3 | mrlogp | ✅ | 2026-07-27T12:42:17Z |
