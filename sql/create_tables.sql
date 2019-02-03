CREATE SCHEMA orange_produce;

CREATE TABLE orange_produce.farms(
    id      big_serial,
    name    text NOT NULL,
    primary_key(id)
);

