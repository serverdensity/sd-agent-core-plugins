cat /docker-entrypoint-initdb.d/02_serverdensity_test.psql | PGPASSWORD=serverdensity psql -h localhost -p 5432 serverdensity_test -U serverdensity
cat /docker-entrypoint-initdb.d/03_dogs.psql | PGPASSWORD=serverdensity psql -h localhost -p 5432 dogs -U serverdensity
