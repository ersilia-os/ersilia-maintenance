# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** 2026-03-02T10:21:43Z

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
| eos9yy1 | ncats-hlcs | ✅ | 2026-03-02T10:27:44Z |
| eos9zw0 | molpmofit | 🚨 | 2026-03-02T10:30:46Z |
| eos11sm | known-antibiotic-resemblance | ✅ | 2026-03-02T10:35:33Z |
| eos18ie | antibiotics-ai-saureus | ✅ | 2026-03-02T10:48:49Z |
| eos1d7r | small-world-zinc | 🚨 | 2026-03-02T10:51:59Z |
| eos1lb5 | mycobacterium-permeability | ✅ | 2026-03-02T10:59:00Z |
| eos1mxi | smiles-pe | 🚨 | 2026-03-02T11:01:26Z |
| eos1n4b | hdac3-inhibition | ✅ | 2026-03-02T11:06:55Z |
| eos1noy | chembl-sampler | 🚨 | 2026-03-02T11:09:47Z |
| eos1ut3 | molfeat-usrcat | ✅ | 2026-03-02T11:18:10Z |
