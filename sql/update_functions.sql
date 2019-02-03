CREATE OR REPLACE FUNCTION orange_produce.update_farm(int, text DEFAULT NULL, point DEFAULT NULL, int DEFAULT NULL) RETURNS boolean AS $$
DECLARE
    farm_id             ALIAS FOR $1;
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