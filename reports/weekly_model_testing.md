# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2025-12-11T20:51:15Z

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
| eos1n4b | hdac3-inhibition | ✅ | 2025-12-11T20:55:35Z |
| eos1noy | chembl-sampler | ✅ | 2025-12-11T20:58:18Z |
| eos1pu1 | cardiotox-dictrank | ✅ | 2025-12-11T21:02:42Z |
| eos1ut3 | molfeat-usrcat | ✅ | 2025-12-11T21:09:19Z |
| eos1vms | chembl-multitask-descriptor | ✅ | 2025-12-11T21:12:32Z |
| eos21q7 | inter-dili | ✅ | 2025-12-11T21:19:18Z |
| eos22io | idl-ppbopt | ✅ | 2025-12-11T21:24:43Z |
| eos238c | mesh-therapeutic-use | 🚨 | 2025-12-11T21:24:48Z |
| eos2401 | scaffold-decoration | ✅ | 2025-12-11T22:02:23Z |
| eos24ci | drugtax | ✅ | 2025-12-11T22:05:27Z |
