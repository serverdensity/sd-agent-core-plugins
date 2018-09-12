CREATE USER serverdensity WITH PASSWORD 'serverdensity';
GRANT SELECT ON pg_stat_database TO serverdensity;
CREATE DATABASE serverdensity_test;
GRANT ALL PRIVILEGES ON DATABASE serverdensity_test TO serverdensity;
CREATE DATABASE dogs;
