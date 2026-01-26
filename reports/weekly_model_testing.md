# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-01-26T10:11:05Z

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
| eos12x7 | spacial-score-complexity | ✅ | 2026-01-26T10:13:29Z |
| eos43at | molgrad-herg | ✅ | 2026-01-26T10:17:44Z |
| eos4k4f | standardization | ✅ | 2026-01-26T10:20:20Z |
| eos7ike | entry-rules | ✅ | 2026-01-26T10:24:22Z |
| eos7jio | rdkit-fingerprint | ✅ | 2026-01-26T10:26:45Z |
| eos7jlv | gdbmedchem-similarity | ✅ | 2026-01-26T10:29:24Z |
| eos7kpb | h3d-virtual-screening-cascade-light | ✅ | 2026-01-26T10:33:20Z |
| eos7l5m | efflux-gram-negative | ✅ | 2026-01-26T10:39:56Z |
| eos7m30 | admet-ai-exact | ✅ | 2026-01-26T10:45:00Z |
| eos7pw8 | syba-synthetic-accessibility | ✅ | 2026-01-26T10:59:18Z |
