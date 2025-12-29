# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2025-12-29T10:08:34Z

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
| eos4e40 | chemprop-antibiotic | 🚨 | 2025-12-29T10:13:42Z |
| eos4ex3 | mole-representations | ✅ | 2025-12-29T10:20:35Z |
| eos4f95 | mycetos | ✅ | 2025-12-29T10:31:59Z |
| eos4jcv | cc-signaturizer-3d-e | ✅ | 2025-12-29T10:40:06Z |
| eos4q1a | crem-structure-generation | ✅ | 2025-12-29T10:45:07Z |
| eos4rta | malaria-mmv | ✅ | 2025-12-29T10:54:09Z |
| eos4rw4 | cddd-onnx | ✅ | 2025-12-29T11:00:07Z |
| eos4se9 | smiles2iupac | ✅ | 2025-12-29T11:12:48Z |
| eos4tcc | bayesherg | ✅ | 2025-12-29T11:17:31Z |
| eos4u6p | cc-signaturizer | ✅ | 2025-12-29T11:27:35Z |
