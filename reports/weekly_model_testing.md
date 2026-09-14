# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-09-14T10:10:21Z

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
| eos9q2i | mol-jepa | ✅ | 2026-09-14T10:18:44Z |
| eos3804 | chemprop-abaumannii | ✅ | 2026-09-14T10:25:03Z |
| eos39co | unimol-representation | ✅ | 2026-09-14T10:31:16Z |
| eos39dp | phakinpro | ✅ | 2026-09-14T10:36:09Z |
| eos3ae6 | whales-descriptor | ✅ | 2026-09-14T10:40:05Z |
| eos3b5e | molecular-weight | ✅ | 2026-09-14T10:43:31Z |
| eos3e6s | chembl-decoys | ✅ | 2026-09-14T10:50:15Z |
| eos1soi | non-growing-antimicrobial | 🚨 | 2026-09-14T10:56:52Z |
| eos3ev6 | ncats-cyp3a4 | ✅ | 2026-09-14T11:02:49Z |
| eos3l5f | clamp | ✅ | 2026-09-14T11:07:04Z |
