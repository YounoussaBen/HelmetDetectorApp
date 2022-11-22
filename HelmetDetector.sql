create database `helmetDetector`;
use `helmetDetector`;

CREATE TABLE `users` (
  `id` int(11) NOT NULL primary key auto_increment,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  register_date timestamp default current_timestamp
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT into `users` (`name`, `email`, `username`, `password`)VALUES(
'Governor', 'Governor@ait.edu.gh', 'Governor', '1234'
);

CREATE TABLE `drivers` (
  `id` int(11) NOT NULL primary key auto_increment,
  `name` varchar(255) NOT NULL,
  `address` varchar(255),
  `dateOfBirth` datetime,
  `email` varchar(255),
  `phone` varchar(20),
  `licensePlateNumber` varchar(255) NOT NULL,
  register_date timestamp default current_timestamp
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `drivers` (`name`,`address`,`dateOfBirth`, `email`, `phone`, `licensePlateNumber`) VALUES
('motech noel', 'Kasoa','1999-05-2-','mosesnoel02@gmail.com', '+255752541568', 'M10AS1620'),
('Thiago Moses', 'Lapaz', '1989-12-04', 'moses@noel.com', '0712541669', 'M91GR903'),
('Saratex Marie', 'Awoshi', '1997-05-06', 'moses@noel.com', '0712541669', 'M17GR3821'),
('Kamonyo Kiiza', 'Kasoa' , '1982-01-19', 'kamonyomoses@gmail.com', '+255752541568', 'N21OR8054');