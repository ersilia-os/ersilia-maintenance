# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-01-19T10:12:23Z

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
| eos6oli | soltrannet-aqueous-solubility | ✅ | 2026-01-19T10:17:50Z |
| eos6ost | reinvent4-libinvent | ✅ | 2026-01-19T10:48:54Z |
| eos6pbf | selfies | ✅ | 2026-01-19T10:51:21Z |
| eos6tpo | chebifier | 🚨 | 2026-01-19T11:00:04Z |
| eos74km | antimicrobial-kg-ml | ✅ | 2026-01-19T11:04:10Z |
| eos77jk | cc-signaturizer-3d-d | ✅ | 2026-01-19T11:13:01Z |
| eos77w8 | grover-sider | ✅ | 2026-01-19T11:19:51Z |
| eos78ao | mordred | ✅ | 2026-01-19T11:23:44Z |
| eos7a45 | coprinet-molecule-price | ✅ | 2026-01-19T11:32:32Z |
| eos7ack | swiss-adme | 🚨 | 2026-01-19T11:32:37Z |
