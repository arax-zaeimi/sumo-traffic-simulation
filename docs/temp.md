```xml
<configuration>
    <input>
        <net-file value="./downtown/montreal_downtown_3.net.xml" />
        <route-files value="./downtown/montreal_routes_3.rou.xml" />
    </input>
</configuration>
```

To add a change to database:

```
To Tupper St:
python .\reroute.py --vehicle=0 --edge=964696603#0

To Guy St:
python .\reroute.py --vehicle=0 --edge=-165217827#3

```

Run server:

```
python .\sumo_manager.py
```

Run Client:

```
python .\sumo_client.py
```
