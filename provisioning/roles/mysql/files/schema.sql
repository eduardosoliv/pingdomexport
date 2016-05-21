DROP TABLE IF EXISTS `pingdom_check`;
CREATE TABLE `pingdom_check` (
    `id` INT(4) UNSIGNED NOT NULL,
    `name` VARCHAR(8192) NOT NULL,
    `created_at` TIMESTAMP NOT NULL,
    `status` ENUM('up', 'down', 'unconfirmed_down', 'unknown', 'paused') NOT NULL,
    `hostname` VARCHAR(8192) NOT NULL,
    `type` ENUM('http', 'https') NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

DROP TABLE IF EXISTS `pingdom_check_result`;
CREATE TABLE `pingdom_check_result` (
    `id` BIGINT(8) UNSIGNED NOT NULL AUTO_INCREMENT,
    `check_id` INT(4) UNSIGNED NOT NULL,
    `at` TIMESTAMP NOT NULL,
    `probe_id` SMALLINT(2) UNSIGNED NOT NULL,
    `status` ENUM('up', 'down', 'unconfirmed_down', 'unknown') NOT NULL,
    `status_desc` VARCHAR(1024) NOT NULL,
    `status_desc_long` VARCHAR(8192) NOT NULL,
    `response_time` INT(4) UNSIGNED DEFAULT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `pcr_check_id_at_probe_id` (`check_id`, `at`, `probe_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
