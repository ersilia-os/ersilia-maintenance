# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-08-31T10:10:34Z

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
| eos1tt2 | mole-embeddings | ✅ | 2026-08-31T10:22:46Z |
| eos3xhm | hades-oral-druglikeness | ✅ | 2026-08-31T10:30:32Z |
| eos6a1h | cocograph-small | ✅ | 2026-08-31T11:41:04Z |
| eos157v | grover-freesolv | ✅ | 2026-08-31T11:50:12Z |
| eos1af5 | molgrad-caco2 | ✅ | 2026-08-31T11:55:59Z |
| eos1amr | grover-bbbp | ✅ | 2026-08-31T12:04:50Z |
| eos1pu1 | cardiotox-dictrank | ✅ | 2026-08-31T12:11:44Z |
| eos6hy3 | image-mol-hiv | ✅ | 2026-08-31T12:18:08Z |
| eos9li5 | biosynfoni | ✅ | 2026-08-31T12:22:55Z |
| eos19mt | chebifier-antibiotic | 🚨 | 2026-08-31T12:30:29Z |
