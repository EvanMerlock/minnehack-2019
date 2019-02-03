CREATE OR REPLACE FUNCTION orange_produce.insert_farm(int, text, point) RETURNS int AS $$
DECLARE
    temp_user_id        ALIAS FOR $1;
    farm_name           ALIAS FOR $2;
    farm_location       ALIAS FOR $3;
    farm_id             bigint;
BEGIN
    INSERT INTO orange_produce.farms(id, name, location, created_by)   
        VALUES (DEFAULT, farm_name, farm_location, temp_user_id)
        RETURNING id INTO farm_id;
    INSERT INTO orange_produce.farm_audit(id, created_date, modified_date)
        VALUES(farm_id, now(), now());
    RETURN farm_id;
END;
$$ LANGUAGE pgplsql;

CREATE OR REPLACE FUNCTION orange_produce.fields(int, int, text) RETURNS int AS $$
DECLARE
    temp_user_id       ALIAS FOR $1;
    farm_name          ALIAS FOR $2;
    