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
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION orange_produce.insert_field(int, int, text) RETURNS int AS $$
DECLARE
    temp_user_id       ALIAS FOR $1;
    farm_id            ALIAS FOR $2;
    field_name         ALIAS FOR $3;
    field_id           int;
BEGIN
    INSERT INTO orange_produce.fields(id, name, contained_in, created_by)
        VALUES (DEFAULT, field_name, farm_id, temp_user_id)
        RETURNING id INTO field_id;
    INSERT INTO orange_produce.field_audit(id, created_date, modified_date)
        VALUES(field_id, now(), now());
    RETURN farm_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION orange_produce.insert_block(int, int, text, int) RETURNS int AS $$
DECLARE
    temp_user_id       ALIAS FOR $1;
    field_id           ALIAS FOR $2;
    block_name         ALIAS FOR $3;
    crop_id            ALIAS FOR $4;
    block_id           int;
BEGIN
    INSERT INTO orange_produce.blocks(id, name, contained_in, created_by, crop)
        VALUES(DEFAULT, block_name, field_id, temp_user_id, crop_id)
        RETURNING id INTO  block_id;
    INSERT INTO orange_produce.blocks_audit(id, created_date, modified_date)
        VALUES(DEFAULT, now(), now());
    RETURN block_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION orange_produce.insert_crop(int, text, money, integer, money, text DEFAULT NULL) RETURNS int AS $$
DECLARE
    temp_user_id        ALIAS FOR $1;
    crop_name           ALIAS FOR $2;
    market_value        ALIAS FOR $3;
    yield_time          ALIAS FOR $4;
    cost_per_unit       ALIAS FOR $5;
    country             ALIAS FOR $6;
    crop_id             int;
BEGIN
    INSERT INTO orange_produce.crops(id, name, country, market_value, yield_time, cost_per, created_by)
        VALUES(DEFAULT, crop_name, country, market_value, yield_time, cost_per_unit, temp_user_id)
        RETURNING id into crop_id;
    INSERT INTO orange_produce.crops_audit(id, created_date, modified_date)
        VALUES(crop_id, now(), now());
    RETURN crop_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION orange_produce.insert_crop_swap_event(int, int, int, timestamptz) RETURNS int AS $$
DECLARE
    temp_user_id        ALIAS FOR $1;
    prev_crop_id        ALIAS FOR $2;
    next_crop_id        ALIAS FOR $3;
    swap_date           ALIAS FOR $4;
    crop_swap_id        int;
BEGIN
    INSERT INTO orange_produce.crop_swap_event(id, previous_crop, new_crop, swap_date, created_by)
        VALUES (DEFAULT, prev_crop_id, new_crop_id, swap_date, temp_user_id)
        RETURNING id INTO crop_swap_id;
    INSERT INTO orange_produce.crop_event_audit(id, created_date, modified_date)
        VALUES(crop_swap_id, now(), now());
    RETURN crop_swap_id;
END;
$$ LANGUAGE plpgsql;