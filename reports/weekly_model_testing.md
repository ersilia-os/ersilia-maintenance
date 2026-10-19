# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-10-19T10:10:58Z

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
| eos8c0o | image-mol-bace | ✅ | 2026-10-19T10:14:47Z |
| eos4zfy | maip-malaria | ✅ | 2026-10-19T10:18:23Z |
| eos526j | aizynthfinder | ✅ | 2026-10-19T10:29:04Z |
| eos5505 | ncats-rlm | ✅ | 2026-10-19T10:33:16Z |
| eos57bx | reinvent4-mol2mol-scaffold | ✅ | 2026-10-19T11:49:16Z |
| eos59rr | bidd-molmap-fingerprint | ✅ | 2026-10-19T11:56:12Z |
| eos5axz | morgan-counts | ✅ | 2026-10-19T11:59:24Z |
| eos5bsw | ecoli-retention | 🚨 | 2026-10-19T12:05:55Z |
| eos5cl7 | ngonorrhoeae-inhibition | ✅ | 2026-10-19T12:14:10Z |
| eos2401 | scaffold-decoration | 🚨 | 2026-10-19T12:18:20Z |
