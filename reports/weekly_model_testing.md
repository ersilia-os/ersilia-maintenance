# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-06-15T12:06:24Z

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
| eos2egp | chelating-groups | ✅ | 2026-06-15T12:10:24Z |
| eos5f0j | checkmol-functional-groups | ✅ | 2026-06-15T12:14:20Z |
| eos7dg4 | ntd-rule | ✅ | 2026-06-15T12:18:16Z |
| eos7nno | ncats-cyp2d6 | ✅ | 2026-06-15T12:24:21Z |
| eos85mn | farm-representation | ✅ | 2026-06-15T12:29:55Z |
| eos4k4f | standardization | ✅ | 2026-06-15T12:34:22Z |
| eos7ike | entry-rules | 🚨 | 2026-06-15T12:40:33Z |
| eos7jio | rdkit-fingerprint | ✅ | 2026-06-15T12:44:32Z |
| eos7jlv | gdbmedchem-similarity | 🚨 | 2026-06-15T12:48:47Z |
| eos7kpb | h3d-virtual-screening-cascade-light | 🚨 | 2026-06-15T12:52:01Z |
