# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-09-21T10:10:04Z

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
| eos48ue | surrogate-adme | ✅ | 2026-09-21T10:18:53Z |
| eos7jur | retromol-fingerprint | ✅ | 2026-09-21T10:23:22Z |
| eos8gop | monroe-embeddings | ✅ | 2026-09-21T10:28:54Z |
| eos3le9 | hepg2-mmv | ✅ | 2026-09-21T10:36:59Z |
| eos3lyd | efflux-avoidance-gram-negative | 🚨 | 2026-09-21T10:42:44Z |
| eos3mk2 | bbbp-marine-kinase-inhibitors | ✅ | 2026-09-21T10:47:15Z |
| eos3ujl | mtb-permeability | ✅ | 2026-09-21T10:51:43Z |
| eos3xip | grover-qm8 | ✅ | 2026-09-21T10:59:35Z |
| eos3zur | molfeat-estate | ✅ | 2026-09-21T11:06:09Z |
| eos46ev | chemtb | ✅ | 2026-09-21T11:11:40Z |
