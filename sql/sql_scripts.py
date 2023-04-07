CREATE_DB = "CREATE DATABASE IF NOT EXISTS `p22`;"
SHOW_DB = 'SHOW DATABASES;'
CREATE_TABLE_MOVIE = "CREATE TABLE `movie`(" + \
                     "id INT AUTO_INCREMENT PRIMARY KEY," + \
                     "title VARCHAR(255)," + \
                     "release_year YEAR(4)," + \
                     "genre VARCHAR(100));"

CREATE_TABLE_REVIEWER = "CREATE TABLE `reviewer`(" + \
                     "id INT AUTO_INCREMENT PRIMARY KEY," + \
                     "first_name VARCHAR(255)," + \
                     "last_name VARCHAR(255),"

CREATE_TABLE_RATING = "CREATE TABLE `rating`(" + \
                     "move_id INT," + \
                     "reviewer_id INT," + \
                     "rating INT," + \
                     "FOREIGN KEY (move_id) REFERENCES movie(id)" +\
                     "FOREIGN KEY (reviewer_id) REFERENCES reviewer(id)" +\
                     "PRIMARY KEY (move_id, reviewer_id));"

SHOW_TABLE_QUERY = "DESCRIBE {}"
