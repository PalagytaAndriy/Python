CREATE TABLE `rating`(
    movie_id INT,
    reviewer_id INT,
    rating INT,
    FOREIGN KEY (move_id) REFERENCES movie(id),
    FOREIGN KEY (reviewer_id) REFERENCES reviewer(id)

)