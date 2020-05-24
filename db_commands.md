## MySQL Commands

#### Start / Stop / Restart MySQL Server
`sudo /usr/local/mysql/support-files/mysql.server start`
`sudo /usr/local/mysql/support-files/mysql.server stop`
`sudo /usr/local/mysql/support-files/mysql.server restart`


### Homebrew - MySQL

`brew install mysql`

`mysql.server start`

#### Restart password // Strengthening password
`mysql_secure_installation`

`mysql -u root -p`


## MongoDB Commands

### Homebrew - MongoDB Server

#### Uninstall old tap formula
`brew services stop mongodb`
`brew uninstall mongodb`

#### Install custom formula
`brew tap mongodb/brew`
`brew install mongodb-community`
`brew services start mongodb-community`


#### Start / Stop / Restart MongoDB Server
`brew services start mongodb-community`
`brew services stop mongodb-community`
`brew services restart mongodb-community`
