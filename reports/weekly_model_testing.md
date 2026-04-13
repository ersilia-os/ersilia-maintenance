# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-04-13T10:37:42Z

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
| eos3ev6 | ncats-cyp3a4 | ✅ | 2026-04-13T10:45:04Z |
| eos3l5f | clamp | ✅ | 2026-04-13T10:50:24Z |
| eos3le9 | hepg2-mmv | ✅ | 2026-04-13T11:00:00Z |
| eos3mk2 | bbbp-marine-kinase-inhibitors | ✅ | 2026-04-13T11:05:26Z |
| eos3nn9 | mpro-covid19 | 🚨 | 2026-04-13T11:08:30Z |
| eos3ujl | mtb-permeability | ✅ | 2026-04-13T11:14:10Z |
| eos3wzy | qupkake | ✅ | 2026-04-13T11:25:02Z |
| eos1soi | non-growing-antimicrobial | ✅ | 2026-04-13T11:32:10Z |
| eos3lyd | efflux-pump-avoidance-gram-negative | ✅ | 2026-04-13T11:38:48Z |
| eos3xip | grover-qm8 | ✅ | 2026-04-13T11:47:20Z |
