# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-01-05T10:09:53Z

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
| eos4r1g | entry-classifier | ✅ | 2026-01-05T10:17:57Z |
| eos4wt0 | morgan-binary-fps | ✅ | 2026-01-05T10:20:33Z |
| eos4x30 | pmapper-3d | ✅ | 2026-01-05T10:26:50Z |
| eos4xb1 | antihypertension-prediction | ✅ | 2026-01-05T10:34:09Z |
| eos4ywv | macaw | ✅ | 2026-01-05T10:37:45Z |
| eos4zfy | maip-malaria | ✅ | 2026-01-05T10:40:47Z |
| eos526j | aizynthfinder | ✅ | 2026-01-05T10:51:09Z |
| eos5505 | ncats-rlm | ✅ | 2026-01-05T10:55:26Z |
| eos57bx | reinvent4-mol2mol-scaffold | ✅ | 2026-01-05T11:45:56Z |
| eos59rr | bidd-molmap-fingerprint | ✅ | 2026-01-05T11:52:35Z |
