CREATE TABLE `User` (
	`id` int NOT NULL AUTO_INCREMENT,
	`f_name` varchar(30) NOT NULL,
	`l_name` varchar(30) NOT NULL,
    `email` varchar(320) NOT NULL ,
	`password` varchar(255) NOT NULL,
    `date_created` DATE NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Relationship` (
	`user1_id` int NOT NULL,
	`user2_id` int NOT NULL,
	`type` int NOT NULL DEFAULT 0,
	`status` int NOT NULL DEFAULT 0,
	`action_user_id` int NOT NULL,
	PRIMARY KEY (`user1_id`,`user2_id`,`action_user_id`)
);

CREATE TABLE `Post` (
	`id` int NOT NULL AUTO_INCREMENT,
	`posted_by` int NOT NULL,
    `date_posted` DATE NOT NULL,
	`post_image` varchar(255) NOT NULL,
	`post_msg` TEXT NOT NULL,
	PRIMARY KEY (`id`,`posted_by`)
);

CREATE TABLE `Comment` (
	`id` int NOT NULL AUTO_INCREMENT,
	`comment_text` TEXT NOT NULL,
	`posted_by` int NOT NULL,
	`posted_to` int NOT NULL,
	`date_commented` DATE NOT NULL,
	PRIMARY KEY (`id`,`posted_by`,`posted_to`)
);

CREATE TABLE `Group_` (
	`id` int NOT NULL AUTO_INCREMENT,
	`created_by` int NOT NULL,
	`name` varchar(255) NOT NULL,
	PRIMARY KEY (`id`,`created_by`)
);

CREATE TABLE `Group_Relationship` (
	`user_id` int NOT NULL,
	`group_id` int NOT NULL,
	`status` int NOT NULL,
	PRIMARY KEY (`user_id`,`group_id`)
);

CREATE TABLE `Group_Posts` (
	`group_id` int NOT NULL,
	`post_id` int NOT NULL,
	PRIMARY KEY (`group_id`,`post_id`)
);

CREATE TABLE `Profile` (
	`user_id` int NOT NULL,
	`profile_pic` varchar(255),
	`dob` DATE,
	`biography` TEXT,
	`gender` varchar(20),
	PRIMARY KEY (`user_id`)
);	

ALTER TABLE `Relationship` ADD CONSTRAINT `Relationship_fk0` FOREIGN KEY (`user1_id`) REFERENCES `User`(`id`);

ALTER TABLE `Relationship` ADD CONSTRAINT `Relationship_fk1` FOREIGN KEY (`user2_id`) REFERENCES `User`(`id`);

ALTER TABLE `Relationship` ADD CONSTRAINT `Relationship_fk2` FOREIGN KEY (`action_user_id`) REFERENCES `User`(`id`);

ALTER TABLE `Post` ADD CONSTRAINT `Post_fk0` FOREIGN KEY (`posted_by`) REFERENCES `User`(`id`);

ALTER TABLE `Comment` ADD CONSTRAINT `Comment_fk0` FOREIGN KEY (`posted_by`) REFERENCES `User`(`id`);

ALTER TABLE `Comment` ADD CONSTRAINT `Comment_fk1` FOREIGN KEY (`posted_to`) REFERENCES `Post`(`id`);

ALTER TABLE `Group_` ADD CONSTRAINT `Group_fk0` FOREIGN KEY (`created_by`) REFERENCES `User`(`id`);

ALTER TABLE `Group_Relationship` ADD CONSTRAINT `Group_Relationship_fk0` FOREIGN KEY (`user_id`) REFERENCES `User`(`id`);

ALTER TABLE `Group_Relationship` ADD CONSTRAINT `Group_Relationship_fk1` FOREIGN KEY (`group_id`) REFERENCES `Group_`(`id`);

ALTER TABLE `Group_Posts` ADD CONSTRAINT `Group_-Posts_fk0` FOREIGN KEY (`group_id`) REFERENCES `Group_`(`id`);

ALTER TABLE `Group_Posts` ADD CONSTRAINT `Group_-Posts_fk1` FOREIGN KEY (`post_id`) REFERENCES `Post`(`id`);

ALTER TABLE `Profile` ADD CONSTRAINT `Profile_fk0` FOREIGN KEY (`user_id`) REFERENCES `User`(`id`);



/* Neccessary Stored Procedures */



DELIMITER // 

/* Update Profile */
CREATE PROCEDURE UpdateProfile(
	IN id int,
	IN bio text, 
	IN genders varchar(20),
	IN prof_pic varchar(255),
	IN dob_ date
)
BEGIN
	UPDATE PROFILE
	SET
	 biography = bio,
	 gender = genders,
	 profile_pic = prof_pic,
	 dob = dob_
	WHERE user_id = id;
END //

/* Adding a new friend */
CREATE PROCEDURE AddFriend(
	IN id1 int,
	IN id2 int
)

BEGIN 
	INSERT INTO Relationship(user1_id,user2_id,action_user_id) VALUES(id1,id2,id1);
END //

/* Accepting Friend Request */
CREATE PROCEDURE AcceptFriend(
	IN id1 int,
	IN id2 int,
	IN decision int
)

BEGIN 
	UPDATE Relationship
	SET 
		status = decision,
		type = decision,
		action_user_id = id2
	WHERE (user1_id = id1) AND (user2_id = id2);
END //

/* Getting list of friends for specific user */

CREATE PROCEDURE GetFriends(
	IN id1 int
)

BEGIN 
	SELECT user2_id
	FROM Relationship
	WHERE user1_id = id1;	
END //

/* Finding Specific User */

CREATE PROCEDURE FindUser(
	IN id_ int
)

BEGIN 
	SELECT * FROM User
	WHERE id = id_;
END //

/* Searching for a user*/

CREATE PROCEDURE SearchUser(
	IN user_ varchar(255)
)

BEGIN
	SELECT * FROM User
	WHERE f_name LIKE user_ or l_name LIKE user_ ;
END //


/* Get Relevant Posts for User's Feed */ 

CREATE PROCEDURE UserFeed(
	IN user_ int
)

BEGIN 
	SELECT * FROM Post 
	JOIN ( 
		SELECT user2_id
		FROM Relationship
		WHERE user1_id = user_
	) as user_rship
	WHERE posted_by = user2_id;
END // 

/* Get Relevant Comments for Post */

CREATE PROCEDURE PostComments(
	IN post_ int
)
BEGIN 
	SELECT * FROM Comment
	JOIN ( 
		SELECT Post.id 
		FROM Post
		WHERE id = post_
	) as post_comments_rship
	WHERE Comment.posted_to = post_comments_rship.id;
END // 

/* Join a Group_ */

CREATE PROCEDURE JoinGroup(
	IN userid int, 
	IN groupid int
)

BEGIN 
	INSERT INTO Group_Relationship(user_id,group_id,status) VALUES (userid,groupid,1);
END //

/* Show group_ members */

CREATE PROCEDURE GetMembers(
	IN grpid int
)

BEGIN 
	SELECT id, f_name, l_name
	FROM User
	Join (
		Select user_id 
		From Group_Relationship
		WHERE group_id = grpid) as group_members
	WHERE group_members.user_id = User.id;
END //

/* Show group_ posts */

CREATE PROCEDURE GetGrpPosts(
	IN grpid int
)

BEGIN 
	SELECT * 
	FROM Post
	Join (
		Select post_id 
		FROM Group_Posts
		WHERE group_id = grpid) as group_post
	WHERE group_post.post_id = Post.id;
END //
DELIMITER ;
