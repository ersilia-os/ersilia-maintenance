# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-01-08T14:23:18Z

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
| eos5axz | morgan-counts | ✅ | 2026-01-08T14:25:54Z |
| eos5bsw | ecoli-retention | ✅ | 2026-01-08T14:33:59Z |
| eos5cl7 | ngonorrhoeae-inhibition | ✅ | 2026-01-08T14:41:58Z |
| eos5guo | erg-fingerprints | ✅ | 2026-01-08T14:44:34Z |
| eos5jz9 | ncats-cyp2c9 | ✅ | 2026-01-08T14:50:57Z |
| eos5nqn | gneprop-ecoli | ✅ | 2026-01-08T15:02:45Z |
| eos5pt8 | druglikeness-unsupervised | ✅ | 2026-01-08T15:08:34Z |
| eos5smc | grover-tox21 | ✅ | 2026-01-08T15:16:02Z |
| eos5xng | chemprop-burkholderia | ✅ | 2026-01-08T15:23:39Z |
| eos633t | moler-enamine-blocks | 🚨 | 2026-01-08T15:34:26Z |
