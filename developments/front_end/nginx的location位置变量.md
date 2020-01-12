```
    server {
        listen          80 default_server reuseport;
        include         fastcgi_params;
        
        {%- if install_flag == "true" %}
        location = /logtail.sh {
            alias /var/www/html/logtail.sh;
            log_not_found off;
            access_log off;
        }
        location ~ ^/(arm64|x86|windows)/(logtail-linux64.tar.gz|logtail_installer.zip)$ {
            alias /var/www/html/$1/$2;
            log_not_found off;
            access_log off;
        }
        {%- endif %}

        location / {
            fastcgi_pass        unix:/tmp/fastcgi.socket;
            access_log          /apsara/nginx/logs/fastcgi_agent_access.log main;
        }
    }
```

