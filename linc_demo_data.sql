-- Création des tables de base

DROP TABLE IF EXISTS transfers;
DROP TABLE IF EXISTS wallets;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100) UNIQUE,
  password_hash TEXT,
  kyc_level INT DEFAULT 0,
  score INT DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE wallets (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id),
  currency VARCHAR(3),
  balance NUMERIC DEFAULT 0
);

CREATE TABLE transfers (
  id SERIAL PRIMARY KEY,
  sender_wallet_id INT,
  receiver_wallet_id INT,
  amount NUMERIC,
  currency VARCHAR(3),
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  description TEXT
);

-- Insertion de 5 utilisateurs fictifs

INSERT INTO users (name, email, password_hash, kyc_level, score) VALUES
('Alice Mbala', 'alice@linc.cd', 'hashed_pw1', 1, 72),
('Bob Tshisekedi', 'bob@linc.cd', 'hashed_pw2', 2, 85),
('Clara Lumumba', 'clara@linc.cd', 'hashed_pw3', 3, 91),
('David Kabila', 'david@linc.cd', 'hashed_pw4', 1, 64),
('Eva Bemba', 'eva@linc.cd', 'hashed_pw5', 2, 78);

-- 3 wallets par utilisateur (CDF, USD, EUR)

INSERT INTO wallets (user_id, currency, balance) VALUES
(1, 'CDF', 250000), (1, 'USD', 100), (1, 'EUR', 50),
(2, 'CDF', 900000), (2, 'USD', 1200), (2, 'EUR', 0),
(3, 'CDF', 500000), (3, 'USD', 300), (3, 'EUR', 75),
(4, 'CDF', 150000), (4, 'USD', 200), (4, 'EUR', 20),
(5, 'CDF', 800000), (5, 'USD', 800), (5, 'EUR', 45);

-- Historique de quelques transferts

INSERT INTO transfers (sender_wallet_id, receiver_wallet_id, amount, currency, description) VALUES
(1, 4, 50, 'USD', 'Paiement service'),
(5, 2, 70000, 'CDF', 'Envoi fonds famille'),
(9, 7, 20, 'EUR', 'Participation projet'),
(6, 3, 100, 'USD', 'Transfert crypto simulation');