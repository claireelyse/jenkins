# jenkins
This is my notes for setting up Jenkins 10/15/2024 following this documentation
https://www.jenkins.io/doc/book/installing/linux/#debianubuntu

## VM - Ubuntu
Operating system:Linux (ubuntu 24.04)
Size:Standard B2s (2 vcpus, 4 GiB memory)

## Connect
```Bash
ssh -i .\Downloads\Jenkins_key1.pem azureuser@52.228.188.138
```

install the long term release of jenkins
```Bash
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
```

Intall Java
```Bash
sudo apt update
sudo apt install fontconfig openjdk-17-jre
java -version
```
not in notes
```Bash
sudo snap install openjdk
```

not continue the docs
```Bash
openjdk version "17.0.8" 2023-07-18
openjdk Runtime Environment "(build 17.0.8+7-Debian-1deb12u1)"
openjdk 64-Bit Server VM "(build 17.0.8+7-Debian-1deb12u1, mixed mode, sharing)"
```

Turn on the service
```Bash
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins
```

## Troubleshooting

Logs are here if the application hasn't booted yet
```Bash
journalctl -b | grep -i -e jenkins
```
if you get an error here is where the logs are here once the application is running
```Bash
/var/log/jenkins/jenkins.log
```

default application user doesn't have access to java so change User=jenkins to User=root
```Bash
systemctl edit jenkins
```

netstat -pnlt | grep ':8080'

apt list --installed | grep -e jenkins

curl 127.0.0.1:8080