# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-07-20T11:03:12Z

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
| eos2hbd | passive-permeability | ✅ | 2026-07-20T11:11:51Z |
| eos92sw | etoxpred | ✅ | 2026-07-20T11:18:13Z |
| eos935d | meta-trans | ✅ | 2026-07-20T11:31:01Z |
| eos96ia | molgrad-cyp3a4 | ✅ | 2026-07-20T11:37:30Z |
| eos9c7k | medchem17-similarity | ✅ | 2026-07-20T11:42:25Z |
| eos9ei3 | sa-score | ✅ | 2026-07-20T11:47:31Z |
| eos9f6t | chemprop-sars-cov-inhibition | ✅ | 2026-07-20T11:56:58Z |
| eos9ivc | anti-mtb-seattle | 🚨 | 2026-07-20T12:04:56Z |
| eos9o72 | chemeleon | ✅ | 2026-07-20T12:11:56Z |
| eos9p4a | deep-dl | ✅ | 2026-07-20T12:18:05Z |
