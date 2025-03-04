# ZapZap - Whatsapp Desktop for Linux 
An unofficial WhatsApp desktop application written in Pyqt6 + PyQt6-WebEngine.

![Zapzap for whatsapp](https://github.com/rafatosta/zapzap/blob/main/share/screenshot/zapzap.png)

## Features
- [x] Features come with Whatsapp web
- [x] System tray icon
- [x] Icon in systray changes if there are new messages
- [x] Fullscreen mode
- [x] Background running

## Future Features
- [ ] Run multiple users

## Contribute

If you want to help make ZapZap better the easiest thing you can do is to [report issues and feature requests](https://github.com/rafatosta/zapzap/issues).
Or you can help in development and translation.


## Using ZapZap

Check out [releases](https://github.com/rafatosta/zapzap/releases) for available packages.

## Development

### Local Development

#### Installing dependencies
```bash
$ pip install PyQt6 PyQt6-WebEngine
```
#### Running the application
```bash
$ git clone https://github.com/rafatosta/zapzap.git
$ cd zapzap
# Running
$ python -m zapzap
```

### Flatpak Development

#### Installing dependencies
It is recommend to use the **Flatpak User Mode** installation method.
In this mode the packages are installed into user space, without affecting the system.

#### Flatpak user mode

```bash
# add flathub remote
$ flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

# installing required packages
$ flatpak install --user --assumeyes flathub org.kde.Platform//6.2 org.kde.Sdk//6.2 io.qt.qtwebengine.BaseApp//6.2
```
#### Flatpak system mode
```bash
# add flathub remote
$ sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

# installing required packages
$ sudo flatpak install flathub org.kde.Platform//6.2 org.kde.Sdk//6.2 io.qt.qtwebengine.BaseApp//6.2
```
### Building and running the application
Youp can be installed on all distributions supporting [Flatpak](http://flatpak.org/) from [Flathub](https://flathub.org/apps/details/com.rtosta.zapzap).

```bash
# Building and install
$ flatpak-builder build com.rtosta.zapzap.yaml --force-clean --ccache --install --user
# Running
$ flatpak-builder --run build com.rtosta.zapzap.yaml zapzap
```

#### Fork
The application is built directly from Github, in case of Fork don't forget to change your Github link in [com.rtosta.zapzap.yaml](https://github.com/rafatosta/zapzap/blob/main/com.rtosta.zapzap.yaml) and commit it first.

### Contact
Maintainer: Rafael Tosta<br/>
E-Mail: *rafa.ecomp@gmail.com*<br/>
Telegram: *@RafaelTosta*<br/>

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/donate/?business=E7R4BVR45GRC2&no_recurring=0&item_name=ZapZap+-+Whatsapp+Desktop+for+linux%0AAn+unofficial+WhatsApp+desktop+application+written+in+Pyqt6+%2B+PyQt6-WebEngine.&currency_code=USD)






