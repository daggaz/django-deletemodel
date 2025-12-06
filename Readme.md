This project illustrates a potential bug in django migrations.

Run:
```bash
docker compose up
```

You'll see the migrations all succeed.  They probably shouldn't.

Get a db shell:
```bash
docker compose exec db psql -U constraintbug
```

Observe that `constraintbug_jane` is missing the FK constraint.

Reset the database back to empty:
```bash
docker compose down
```
