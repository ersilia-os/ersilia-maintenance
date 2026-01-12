# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-01-12T10:12:47Z

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
| eos4avb | image-mol-embeddings | ✅ | 2026-01-12T10:15:59Z |
| eos694w | reinvent4-mol2mol-medium-similarity | ✅ | 2026-01-12T10:47:38Z |
| eos69p9 | ssl-gcn-tox21 | ✅ | 2026-01-12T10:52:56Z |
| eos6ao8 | molgrad-ppb | ✅ | 2026-01-12T10:56:30Z |
| eos6aun | rxn-fingerprint | ✅ | 2026-01-12T11:02:17Z |
| eos6fza | grover-clintox | ✅ | 2026-01-12T11:08:38Z |
| eos6m2k | mole-antimicrobial | ✅ | 2026-01-12T11:15:39Z |
| eos6m4j | bidd-molmap-desc | ✅ | 2026-01-12T11:23:34Z |
| eos6o0z | grover-qm7 | ✅ | 2026-01-12T11:30:07Z |
| eos6ojg | antibioticdb-similarity-matches | ✅ | 2026-01-12T11:33:51Z |
