CREATE TABLE IF NOT EXISTS services (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    status VARCHAR(50) NOT NULL,
    port INTEGER NOT NULL
);

INSERT INTO services (name, status, port)
VALUES
    ('Nginx', 'running', 80),
    ('Python API', 'running', 5000),
    ('PostgreSQL', 'running', 5432);
