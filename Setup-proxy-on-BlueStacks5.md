# How to setup **proxy** on **BlueStacks 5**

## 1. Be sure to be root
1.1) Use [BlueStaks Tweaker](https://bstweaker.tk/) to root your BlueStacks 5 program.
⚠ Be careful, BlueStacks 5 needs BlueStacks Tweaker 6 ⚠

## 2. Install **X-plore** application

2.1) Install the application [X-plore](https://x-plore-file-manager.fr.uptodown.com/android). You will need it to edit an XML file.

## 3. Edit a specific configuration file

3.1) Navigate to `/data/system/users/0/settings_global.xml` and add the following code at the end

```
<setting id="100" name="global_proxy_pac_url" value="" package="android" />
<setting id="97" name="global_http_proxy_host" value="192.168.1.2" package="android" />
<setting id="98" name="global_http_proxy_port" value="8888" package="android" />
<setting id="99" name="global_http_proxy_exclusion_list" value="" package="android" />
<setting id="96" name="http_proxy" value="192.168.1.2:8888" package="com.android.shell" />
```
⚠ Be sure :
- To adapt the code, replacing the IP address (here `192.168.1.2`)
- To adapt the code, replacing the destination port (here `8888`)
- That none of the ids is already used in your file (here `96`, `97`, `98`, `99`, `100`)

3.2) Reboot BlueStacks 5

3.3) Enjoy 🎉

---

*Thanks to **ProgramTechie** - [https://www.reddit.com/r/BlueStacks/comments/oe2z02/bluestacks_5_proxy/](https://www.reddit.com/r/BlueStacks/comments/oe2z02/bluestacks_5_proxy/)*