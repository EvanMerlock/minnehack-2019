CREATE OR REPLACE FUNCTION orange_produce.update_farm(int, text DEFAULT NULL, point DEFAULT NULL, int DEFAULT NULL) RETURNS boolean AS $$
DECLARE
    farm_id                 ALIAS FOR $1;
    mod_farm_name           ALIAS FOR $2;
    mod_farm_location       ALIAS FOR $3;
    mod_created_by_id       ALIAS FOR $4;
BEGIN
    UPDATE orange_produce.farms
        SET name = coalesce(mod_farm_name, name),
            location = coalesce(mod_farm_location, location),
            created_by = coalesce(mod_created_by_id, created_by)
    WHERE id = farm_id;
    UPDATE orange_produce.farm_audit
        SET modified_date = now()
    WHERE id = farm_id;
    RETURN true;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION orange_produce.update_field(int, text DEFAULT NULL, int DEFAULT NULL, int DEFAULT NULL) RETURNS boolean AS $$
DECLARE
    field_id                ALIAS FOR $1;
    mod_field_name          ALIAS FOR $2;
    mod_contained_in        ALIAS FOR $3;
    mod_created_by_id       ALIAS FOR $4;
BEGIN
    UPDATE orange_produce.fields
        SET name = coalesce(mod_field_name, name),
            contained_in = coalesce(mod_contained_in, contained_in),
            created_by = coalesce(mod_created_by_id, created_by)
    WHERE id = field_id;
    UPDATE orange_produce.fields_audit
        SET modified_date = now()
    WHERE id = field_id;
    RETURN true;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION orange_produce.update_block(int, text DEFAULT NULL, int DEFAULT NULL, int DEFAULT NULL, int DEFAULT NULL) RETURNS boolean AS $$
DECLARE
    block_id                ALIAS FOR $1;
    mod_block_name          ALIAS FOR $2;
    mod_contained_in        ALIAS FOR $3;
    mod_created_by_id       ALIAS FOR $4;
    mod_crop_id             ALIAS FOR $5;
BEGIN
    UPDATE orange_produce.blocks
        SET name = coalesce(mod_block_name, name),
            contained_in = coalesce(mod_contained_in, contained_in),
            created_by = coalesce(mod_created_by_id, created_by),
            crop = coalesce(mod_crop_id, crop)
    WHERE id = block_id;
    UPDATE orange_produce.blocks_audit
        SET modified_date = now()
    WHERE id = block_id;
    RETURN true;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION orange_produce.update_crop(int, text DEFAULT NULL, text DEFAULT NULL, money DEFAULT NULL, int DEFAULT NULL, money DEFAULT NULL, int DEFAULT NULL) RETURNS boolean AS $$
DECLARE
    crop_id                 ALIAS FOR $1;
    mod_crop_name           ALIAS FOR $2;
    mod_country             ALIAS FOR $3;
    mod_market_value        ALIAS FOR $4;
    mod_yield_time          ALIAS FOR $5;
    mod_cost_per            ALIAS FOR $6;
    mod_created_by          ALIAS FOR $7;
BEGIN
    UPDATE orange_produce.crops
        SET name       = coalesce(mod_crop_name, name),
            country         = coalesce(mod_country, name),
            market_value    = coalesce(mod_market_value, market_value),
            yield_time      = coalesce(mod_yield_time, yield_time),
            cost_per        = coalesce(mod_cost_per, cost_per),
            created_by      = coalesce(mod_created_by, created_by)
    WHERE id = crop_id;
    UPDATE orange_produce.crops_audit
        SET modified_date = now()
    WHERE id = crop_id;
    RETURN true;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION orange_produce.update_crop_swap_event(int, int DEFAULT NULL, int DEFAULT NULL, timestamptz DEFAULT NULL, int DEFAULT NULL) RETURNS boolean AS $$
DECLARE
    crop_swap_id            ALIAS FOR $1;
    mod_crop_swap_prev      ALIAS FOR $2;
    mod_crop_swap_next      ALIAS FOR $3;
    mod_time_swap           ALIAS FOR $4;
    mod_created_by          ALIAS FOR $5;
BEGIN
    UPDATE orange_produce.crop_swap_event
        SET previous_crop = coalesce(mod_crop_swap_prev, previous_crop),
            new_crop     = coalesce(mod_crop_swap_next, new_crop),
            created_by    = coalesce(mod_created_by, created_by),
            swap_date     = coalesce(mod_time_swap, swap_date)
    WHERE id = crop_swap_id;
    UPDATE orange_produce.crop_event_audit
        SET modified_date = now()
    WHERE id = crop_swap_id;
    RETURN true;
END;
$$ LANGUAGE plpgsql;