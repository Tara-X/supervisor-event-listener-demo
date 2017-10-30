supervisor-event-listener-demo
====


Reference:


##

``` bash
$ pyenv use 2.7.12
$ virtualenv venv
$ source venv/bin/activate
$ pip install supervisor
$ supervisord -c supervisor.conf
```


Then start or close applicaiton in `http://localhost:9001` (user/123), you will see logs in `event.log` file


## Issures

1. https://github.com/Tara-X/supervisor-event-listener-demo/issues/1


