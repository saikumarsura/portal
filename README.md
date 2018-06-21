Download this file.

1) Active environment 
  > Create a forlder envdjango
  commands to run.
	  >virtualenv myenvironment envdjango 
    >source envdjango/bin/active
		>pip install Django==1.9
		>pip install MySQL-python==1.2.5
		>pip install pygeoip==0.3.2

2) Create Data base
	
	with below 
		--
		-- Table structure for table `users_data`
		--

		CREATE TABLE `users_data` (
		  `id` int(11) NOT NULL,
		  `user_name` varchar(50) NOT NULL,
		  `last_name` varchar(50) NOT NULL,
		  `email` varchar(100) NOT NULL,
		  `password` varchar(40) NOT NULL,
		  `created_datetime` datetime NOT NULL,
		  `location` varchar(100) NOT NULL,
		  `attempts` int(1) DEFAULT NULL,
		  `attempts_datetime` datetime DEFAULT NULL
		) ENGINE=InnoDB DEFAULT CHARSET=latin1;


		--
		-- Table structure for table `users_session`
		--

		CREATE TABLE `users_session` (
		  `id` int(11) NOT NULL,
		  `user_id` int(11) NOT NULL,
		  `sessionkey` varchar(32) NOT NULL
		) ENGINE=InnoDB DEFAULT CHARSET=latin1;

3) Run the project with 
	
	below commend 
	> python manage.py makemigrations
	> python manage.py migrate
	> python manage.py runserver
