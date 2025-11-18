# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2025-11-18T17:20:47Z

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
| eos1amr | grover-bbbp | ✅ | 2025-11-18T17:27:37Z |
| eos1d7r | small-world-zinc | 🚨 | 2025-11-18T17:31:36Z |
| eos1mxi | smiles-pe | ✅ | 2025-11-18T17:34:12Z |
| eos1n4b | hdac3-inhibition | ✅ | 2025-11-18T17:38:07Z |
| eos1noy | chembl-sampler | ✅ | 2025-11-18T17:40:41Z |
| eos1pu1 | cardiotox-dictrank | 🚨 | 2025-11-18T17:42:15Z |
| eos1ut3 | molfeat-usrcat | ✅ | 2025-11-18T17:48:34Z |
| eos21q7 | inter-dili | ✅ | 2025-11-18T17:51:36Z |
| eos22io | idl-ppbopt | ✅ | 2025-11-18T17:56:39Z |
| eos238c | mesh-therapeutic-use | 🚨 | 2025-11-18T18:01:55Z |
