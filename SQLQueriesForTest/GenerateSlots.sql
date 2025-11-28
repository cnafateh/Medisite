DELIMITER $$

DROP PROCEDURE IF EXISTS insert_week_slots$$

CREATE PROCEDURE insert_week_slots()
BEGIN
    DECLARE slot_start DATETIME;
    DECLARE slot_end DATETIME;
    DECLARE day_counter INT DEFAULT 0;

    -- شروع از امروز
    SET slot_start = CONCAT(CURDATE(), ' 09:00:00');
    SET slot_end = CONCAT(CURDATE(), ' 10:00:00');

    WHILE day_counter < 7 DO
        -- حلقه 9 صبح تا 5 عصر هر روز
        WHILE slot_start < CONCAT(DATE_ADD(CURDATE(), INTERVAL day_counter DAY), ' 17:00:00') DO
            INSERT IGNORE INTO appointments_availableslot (start_time, end_time, is_booked)
            VALUES (slot_start, slot_end, FALSE);

            -- حرکت به اسلات بعدی
            SET slot_start = DATE_ADD(slot_start, INTERVAL 1 HOUR);
            SET slot_end = DATE_ADD(slot_end, INTERVAL 1 HOUR);
        END WHILE;

        -- آماده شدن برای روز بعد
        SET day_counter = day_counter + 1;
        SET slot_start = CONCAT(DATE_ADD(CURDATE(), INTERVAL day_counter DAY), ' 09:00:00');
        SET slot_end = CONCAT(DATE_ADD(CURDATE(), INTERVAL day_counter DAY), ' 10:00:00');
    END WHILE;
END$$

DELIMITER ;

CALL insert_week_slots();

