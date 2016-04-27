## maintainence

* get profile status

```sh
$ ansible-playbook -l <hosts> maint.yml -t get_prof -e 'db=<db>' -v
```

* set profile status

```sh
$ ansible-playbook -l <hosts> maint.yml -t set_prof -e 'db=<db> level=<level> slow_ms=<slow_ms>' -v
```
