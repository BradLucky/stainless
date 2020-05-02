# Database Practices

## Sqitch

Use Sqitch to make changes to the database design.

### Getting started

#### Install Sqitch

On [Ubuntu](https://sqitch.org/download/debian/):
```shell
apt-get install sqitch libdbd-pg-perl postgresql-client
```

### Initialize
```shell
sqitch init stainless --uri https://github.com/BradLucky/stainless/ --engine pg
```

### Configure
```shell
sqitch config --user engine.pg.client $(which psql)
sqitch config --user user.name '<NAME>'
sqitch config --user user.email '<EMAIL>'
```

### Adding a change
```shell
sqitch add <SUMMARY> -n '<SHORT DESCRIPTION OF THE CHANGES>'
```

The `<SUMMARY>` will be used as the filename. In the future, this would be good to tie to an issue-tracking system.

### Deploying a change
Example URI:
```shell
db:engine:[//[user[:password]@][host][:port]/][dbname][?params][#fragment]
```

Realized URI for Stainless:
```shell
sqitch deploy db:pg://stainless:abc123@127.0.0.1:5432/stainless
```
