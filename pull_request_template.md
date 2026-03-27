## What does this PR do?
Brief description.

## Type of change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change (requires migration)
- [ ] Documentation

## Schema migration required?
- [ ] **No**
- [ ] **Yes** — see checklist below

### Migration checklist:
- [ ] Incremented `SCHEMA_VERSION`
- [ ] Added step in `migrateLocalStorage()`
- [ ] Added step in `migrateImport(d)`
- [ ] Only ADDS fields (never delete/rename/overwrite)
- [ ] Idempotent (safe to run multiple times)
- [ ] Updated `DATA SCHEMA & MIGRATION` comment block

## Testing
- [ ] No console errors
- [ ] Data preserved
- [ ] Export/Import works
- [ ] Fees ON/OFF both work
- [ ] Tested Chrome + one other browser
