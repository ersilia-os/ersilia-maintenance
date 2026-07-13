# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-07-13T11:04:17Z

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
| eos3wac | moldeberta-smiles-encoder | ✅ | 2026-07-13T11:11:05Z |
| eos5jv3 | mycopermenet | ✅ | 2026-07-13T11:16:54Z |
| eos69jj | neisseria-gonorrhoeae-activity | ✅ | 2026-07-13T11:24:58Z |
| eos8vud | squid | 🚨 | 2026-07-13T11:28:38Z |
| eos93h2 | image-mol-gpcr | ✅ | 2026-07-13T11:34:14Z |
| eos9f7c | paeruginosa-permeation | ✅ | 2026-07-13T11:42:27Z |
| eos2ta5 | cardiotoxnet-herg | ✅ | 2026-07-13T11:48:30Z |
| eos8lok | s2dv-hbv | ✅ | 2026-07-13T11:52:40Z |
| eos238c | mesh-therapeutic-use | ✅ | 2026-07-13T12:02:23Z |
| eos2a9n | chembl-similarity | ✅ | 2026-07-13T12:13:12Z |
