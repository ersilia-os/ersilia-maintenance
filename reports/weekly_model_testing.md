# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-10-05T10:13:53Z

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
| eos2srx | synomega | ✅ | 2026-10-05T10:23:16Z |
| eos5j3l | enscondflow-shape | ✅ | 2026-10-05T11:31:43Z |
| eos92m1 | transpharmer | ✅ | 2026-10-05T11:37:51Z |
| eos9p57 | crem-grow | ✅ | 2026-10-05T11:42:54Z |
| eos4rta | malaria-mmv | 🚨 | 2026-10-05T11:47:36Z |
| eos4rw4 | cddd-onnx | ✅ | 2026-10-05T11:54:48Z |
| eos4se9 | smiles2iupac | 🚨 | 2026-10-05T11:56:55Z |
| eos4tcc | bayesherg | 🚨 | 2026-10-05T12:02:23Z |
| eos633t | moler-enamine-blocks | ✅ | 2026-10-05T12:16:17Z |
| eos8g50 | fastsolv | ✅ | 2026-10-05T12:23:13Z |
