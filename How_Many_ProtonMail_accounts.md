# How to open many free ProtonMail accounts on Firefox startup

## 0. Context

ProtonMail is super cool, but when you have several free accounts it's restrictive: 

- no IMAP 
- not possible to associate several accounts into one
- etc.

This tutorial solves this problem. It was designed for **Firefox only** (*But can definitely be reproduced on Chrome*).

## 1. Install "Multi-Account Containers" extension

1.1) Install https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/[Multi-Account Containers] Firefox extension.

## 2. Create your containers

2.1) Create your containers. Ex :

* "ProtonMailPro"
* "ProtonMailPerso"
* etc

## 3. Connect to accounts

3.1) Open a tab in each of your container and connect to ProtonMail. (*so you will have the session cookie*)

## 4. Activate external liks 

4.1) Go to `about:config`

4.2) Paste `network.protocol-handler.external.ext+container`

4.3) **Set** a boolean value to `True`

## 5. Install "Open url in container" Firefox extension

5.1) Install https://addons.mozilla.org/en-US/firefox/addon/open-url-in-container/[Open external links in a container] Firefox extension.

## 6. Change Firefox home page

6.1) Go to Firefox settings > Home page div
6.2) To open an `URL` in a `Container` the value has to be : "ext+container:name=**Container**&url=**URL**. +
If you have many containers to open (*which is the purpose of this tutorial*), each record has to be separate by a **" `|` "** character.

6.3) Set (for example) this value :

```
ext+container:name=ProtonMailPro&url=https://mail.proton.me/u/0/inbox|ext+container:name=ProtonmailPerso&url=https://mail.proton.me/u/0/inbox
```
## 7. Close and Open Firefox

## 8. Enjoy 🎉

