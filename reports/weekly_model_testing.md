# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-04-27T10:44:21Z

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
| eos4ex3 | mole-representations | ✅ | 2026-04-27T10:53:09Z |
| eos4f95 | mycetos | ✅ | 2026-04-27T11:00:02Z |
| eos4jcv | cc-signaturizer-3d-e | ✅ | 2026-04-27T11:09:41Z |
| eos4q1a | crem-structure-generation | ✅ | 2026-04-27T11:16:52Z |
| eos4rta | malaria-mmv | ✅ | 2026-04-27T11:26:02Z |
| eos4rw4 | cddd-onnx | ✅ | 2026-04-27T11:33:43Z |
| eos4se9 | smiles2iupac | ✅ | 2026-04-27T11:50:42Z |
| eos4tcc | bayesherg | 🚨 | 2026-04-27T11:56:18Z |
| eos4u6p | cc-signaturizer | 🚨 | 2026-04-27T12:02:34Z |
| eos4r1g | entry-classifier | ✅ | 2026-04-27T12:09:31Z |
