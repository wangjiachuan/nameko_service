#install rabbitmq, using apt-get, it will automatically install dependency.
install nameko by clone the nameko project and using python install.
if there is compile error, you need to install a dependency. you can google it.


start the service:

    
nameko run service:ServiceB


in another termial,test the service:

nameko shell
n.dispatch_event("service_a", "event_type", "hello2")
