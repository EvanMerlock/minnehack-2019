CREATE OR REPLACE FUNCTION orange_produce.update_farm(int, text DEFAULT NULL, point DEFAULT NULL, int DEFAULT NULL) RETURNS boolean AS $$
DECLARE
    farm_id                 ALIAS FOR $1;
    mod_farm_name           ALIAS FOR $2;
    mod_farm_location       ALIAS FOR $3;
    mod_created_by_id       ALIAS FOR $4;
BEGIN
    UPDATE orange_produce.farms
        SET farm_name = coalesce(mod_farm_name, farm_name),
            location = coalesce(mod_farm_location, location),
            created_by = coalesce(mod_created_by_id, created_by),
        WHERE id = farm_id;
    UPDATE orange_produce.farm_audit
        SET modified_date = now(),
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
        SET field_name = coalesce(mod_field_name, field_name),
            contained_in = coalesce(mod_contained_in, contained_in),
            created_by = coalesce(mod_created_by_id, created_by),
        WHERE id = field_id;
    UPDATE orange_produce.fields_audit
        SET modified_date = now(),
        WHERE id = field_id;
    RETURN true;
END;
$$ LANGUAGE plpgsql;