### Create a service 

```
sudo vi /etc/systemd/system/note.service

[Unit]
Description=Note Service
After=network.target

[Service]
WorkingDirectory=CLONED_DIRECTORY_PATH
User=$USER
ExecStart=python app.py
SuccessExitStatus=143

[Install]
WantedBy=multi-user.target
```

### Install service

```
sudo systemctl daemon-reload;sudo systemctl enable note.service
```

### Start/Stop/Status:

```
sudo systemctl start note
sudo systemctl stop note
sudo systemctl restart note
sudo systemctl status note
```
