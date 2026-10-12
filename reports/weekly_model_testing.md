# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-10-12T10:18:15Z

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
| eos1ltv | simg-chemical-embeddings | 🚨 | 2026-10-12T10:23:54Z |
| eos7eos | synfrag-accessibility | ✅ | 2026-10-12T10:29:24Z |
| eos88ir | chemical-dice-embeddings | ✅ | 2026-10-12T10:35:43Z |
| eos4n4d | gram-negative-accumulation | ✅ | 2026-10-12T10:45:24Z |
| eos4wt0 | morgan-binary-fps | ✅ | 2026-10-12T10:49:09Z |
| eos4x30 | pmapper-3d | ✅ | 2026-10-12T10:56:27Z |
| eos4xb1 | antihypertension-prediction | ✅ | 2026-10-12T11:05:56Z |
| eos4ywv | macaw | ✅ | 2026-10-12T11:11:33Z |
| eos6tg8 | natural-product-fingerprint | ✅ | 2026-10-12T11:16:08Z |
| eos80k1 | bioactivity-similarity-index | ✅ | 2026-10-12T11:21:47Z |
