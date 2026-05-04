# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-05-04T10:46:02Z

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
| eos4n4d | gram-negative-accumulation | ✅ | 2026-05-04T11:04:36Z |
| eos60mw | cidalsdb | ✅ | 2026-05-04T11:12:43Z |
| eos6tg8 | natural-product-fingerprint | ✅ | 2026-05-04T11:18:25Z |
| eos80k1 | bioactivity-similarity-index | ✅ | 2026-05-04T11:25:24Z |
| eos8c0o | image-mol-bace | ✅ | 2026-05-04T11:30:39Z |
| eos2401 | scaffold-decoration | 🚨 | 2026-05-04T11:42:51Z |
| eos4wt0 | morgan-binary-fps | ✅ | 2026-05-04T11:47:09Z |
| eos4x30 | pmapper-3d | ✅ | 2026-05-04T11:54:15Z |
| eos4xb1 | antihypertension-prediction | ✅ | 2026-05-04T12:03:00Z |
| eos4ywv | macaw | ✅ | 2026-05-04T12:08:28Z |
