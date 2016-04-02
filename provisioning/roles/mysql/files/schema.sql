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
