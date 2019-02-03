CREATE OR REPLACE FUNCTION orange_produce.remove_farm(int) RETURNS boolean AS $$
DECLARE
    removing_id     ALIAS FOR $1;
BEGIN
    DELETE FROM orange_produce.farms WHERE id = removing_id;
    RETURN true;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION orange_produce.remove_field(int) RETURNS boolean AS $$
DECLARE
    removing_id     ALIAS FOR $1;
BEGIN
    DELETE FROM orange_produce.field WHERE id = removing_id;
    RETURN true;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION orange_produce.remove_block(int) RETURNS boolean AS $$
DECLARE
    removing_id     ALIAS FOR $1;
BEGIN
    DELETE FROM orange_produce.blocks WHERE id = removing_id;
    RETURN true;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION orange_produce.remove_crop(int) RETURNS boolean AS $$
DECLARE
    removing_id     ALIAS FOR $1;
BEGIN
    DELETE FROM orange_produce.crops WHERE id = removing_id;
    RETURN true;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION orange_produce.remove_crop_swap_event(int) RETURNS boolean AS $$
DECLARE
    removing_id     ALIAS FOR $1;
BEGIN
    DELETE FROM orange_produce.crop_swap_event WHERE id = removing_id;
    RETURN true;
END;
$$ LANGUAGE plpgsql;