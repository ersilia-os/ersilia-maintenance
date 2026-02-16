# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-02-16T10:23:29Z

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
| eos92sw | etoxpred | ✅ | 2026-02-16T10:28:58Z |
| eos935d | meta-trans | ✅ | 2026-02-16T10:38:46Z |
| eos96ia | molgrad-cyp3a4 | ✅ | 2026-02-16T10:43:28Z |
| eos9c7k | medchem17-similarity | ✅ | 2026-02-16T10:47:12Z |
| eos9ei3 | sa-score | ✅ | 2026-02-16T10:50:44Z |
| eos9f6t | chemprop-sars-cov-inhibition | ✅ | 2026-02-16T10:58:12Z |
| eos9gg2 | chemical-space-projections-drugbank | 🚨 | 2026-02-16T11:02:46Z |
| eos9ivc | anti-mtb-seattle | ✅ | 2026-02-16T11:10:36Z |
| eos9o72 | chemeleon | ✅ | 2026-02-16T11:15:54Z |
| eos9p4a | deep-dl | ✅ | 2026-02-16T11:20:22Z |
