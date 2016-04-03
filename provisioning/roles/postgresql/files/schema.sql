DROP TABLE IF EXISTS pingdom_check;

DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'check_status')
    THEN CREATE TYPE check_status AS ENUM ('up', 'down', 'unconfirmed_down', 'unknown', 'paused');
  END IF;
END$$;

DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'check_type')
    THEN CREATE TYPE check_type AS ENUM('http', 'https');
  END IF;
END$$;

CREATE TABLE pingdom_check (
    id INT PRIMARY KEY NOT NULL,
    name VARCHAR(8192) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL,
    status check_status,
    hostname VARCHAR(8192) NOT NULL,
    type check_type
);
-- INSERT INTO pingdom_check (id, name, created_at, status, hostname, type)
-- VALUES (2057736, 'Test', to_timestamp(1458372620), 'up', 'www.google.com', 'http');

DROP TABLE IF EXISTS pingdom_check_result;

DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'check_results_status')
    THEN CREATE TYPE check_results_status AS ENUM ('up', 'down', 'unconfirmed_down', 'unknown');
  END IF;
END$$;

CREATE TABLE pingdom_check_result (
    id SERIAL PRIMARY KEY,
    check_id INT NOT NULL,
    at TIMESTAMPTZ NOT NULL,
    probe_id smallint NOT NULL,
    status check_results_status,
    status_desc VARCHAR(1024) NOT NULL,
    status_desc_long VARCHAR(8192) NOT NULL,
    response_time INT NOT NULL
);

CREATE INDEX check_result_check_id_at ON pingdom_check_result (check_id, at);
CREATE INDEX check_result_at ON pingdom_check_result (at);

-- INSERT INTO pingdom_check_result (check_id, at, probe_id, status, status_desc, status_desc_long, response_time)
-- VALUES(2057736, to_timestamp(1458376174), 50, 'up', 'OK', 'OK', 582);
